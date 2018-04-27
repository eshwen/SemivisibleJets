#!/bin/bash

if [ -z $1 ]; then
    echo "-------------------------------------------------------------------------------------------------------------
Usage ./runFullSim_condor.sh work_space lhe_file_path model_name n_events n_jobs Lambda_d m_d n_f r_inv x_sec
-------------------------------------------------------------------------------------------------------------"
    exit
fi

: "${SVJ_TOP_DIR:?Certain environment variables do not exist. Please source the setup script first.}; exit"
submission_dir=$SVJ_TOP_DIR/FullSim_files/Condor

work_space=$(readlink -m $1)
if [ ! -d $work_space ]; then
    echo "Work space doesn't exist. Creating it now..."
    mkdir -p $work_space
fi

# For simplicity, use the splitLHE.py script on the large LHE file to generate the smaller ones to be given to the jobs
lhe_file_path=$(readlink -m $2)
declare -a lhe_file_list=( $(echo ${lhe_file_path}/*.lhe | tr ' ' '\n' | sort -h) ) # Need to fix sorting
n_lhe_files=`echo ${#lhe_file_list[@]}`

model_name=$3
n_events=$4
n_jobs=$5

if (( $n_jobs > $n_lhe_files )); then
    echo "Number of jobs exceeds number of LHE files in directory. Try again."
    exit
fi

Lambda_d=$6
m_d=$7
n_f=$8
r_inv=$9
x_sec=${10}

cd $work_space
# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

# Set up CMSSW environments
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
if [ -r $work_space/CMSSW_8_0_21/src ]; then
    echo "CMSSW_8_0_21 release already exists!"
else
    cmsrel CMSSW_8_0_21
fi

cd CMSSW_8_0_21/src
cmsenv
scram b

cd ../..
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r $work_space/CMSSW_9_4_4/src ]; then
    echo "CMSSW_9_4_4 release already exists!"
else
    cmsrel CMSSW_9_4_4
fi

cd CMSSW_9_4_4/src
cmsenv
scram b

cd ../..
export SCRAM_ARCH=slc6_amd64_gcc481
if [ -r $work_space/CMSSW_7_1_30/src ]; then
    echo "CMSSW_7_1_30 release already exists!"
else
    cmsrel CMSSW_7_1_30
fi

# Create directories for logs, submissions scripts and GS fragments
if [[ ! -d $work_space/{logs,submission_scripts,GS_fragments} ]]; then
    mkdir $work_space/{logs,submission_scripts,GS_fragments}
fi

# Write Condor submission files for each job and execute
for seed in $(seq 1 1 $n_jobs); do
    seed=$(echo $seed | bc)
    lhe_file_for_job=${lhe_file_list[$seed]}

    # Create the GS fragment
    gen_frag_path=$($submission_dir/write_GS_fragment.sh $model_name $seed $n_f $Lambda_d $r_inv $x_sec $m_d $work_space)
    
    $submission_dir/write_submission_script.sh $work_space $gen_frag_path $lhe_file_for_job $model_name $n_events $seed $submission_dir
    condor_submit $work_space/submission_scripts/condor_submission_${seed}.job
done

echo "#!/bin/bash
echo \"Warning: May take a while to hadd if many files are present\"
${SVJ_TOP_DIR}/Utils/haddnano.py $work_space/output/${model_name}_nanoAOD_final.root $work_space/output/${model_name}*NANOAOD*.root
mkdir $work_space/output/components
mv $work_space/output/${model_name}*NANOAOD*.root $work_space/output/components/
" > $work_space/combineOutput_${model_name}.sh

chmod +x $work_space/combineOutput_${model_name}.sh

exit