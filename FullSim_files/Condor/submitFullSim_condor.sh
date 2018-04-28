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

source /cvmfs/cms.cern.ch/cmsset_default.sh
# Declare arrays for looping over CMSSW versions and respective architectures
declare -a cmssw_vers=("8_0_21" "9_4_4" "7_1_30")
declare -a gcc_for_archs=("530" "630" "481") # each element corresponds to respective CMSSW version above
arch_counter=0 # for looping over array gcc_for_archs

# Set up CMSSW environments
for each_ver in "${cmssw_vers[@]}"; do    
    export SCRAM_ARCH=slc6_amd64_gcc${gcc_for_archs[$arch_counter]}

    if [ -r $work_space/CMSSW_${each_ver}/src ]; then
	echo "CMSSW_${each_ver} release already exists!"
    else
	cmsrel CMSSW_${each_ver}
    fi

    cd CMSSW_${each_ver}/src
    cmsenv
    scram b
    cd $work_space
    let "arch_counter+=1" # increment to export next architecture
done

# Create directories for gen fragments to occupy
cd CMSSW_7_1_30/src
if [ ! -d Configuration/GenProduction/python ]; then
    mkdir -p Configuration/GenProduction/python
fi
scram b
cd $work_space

# Create directories for logs, submission scripts and GS fragments
if [[ ! -d $work_space/{logs{,"/$model_name"},output,submission_scripts{,"/$model_name"},GS_fragments} ]]; then
    mkdir $work_space/{logs{,"/$model_name"},output,submission_scripts{,"/$model_name"},GS_fragments}
fi

# Write Condor submission files for each job and execute
for seed in $(seq 0 1 $(( $n_jobs-1 ))); do
    seed=$(echo $seed | bc)
    lhe_file_for_job=${lhe_file_list[$seed]}

    # Create the GS fragment
    gen_frag_path=$($submission_dir/write_GS_fragment.sh $model_name $seed $n_f $Lambda_d $r_inv $x_sec $m_d $work_space)
    
    # Write Condor submission script and execute
    job_path=$($submission_dir/write_submission_script.sh $work_space $gen_frag_path $lhe_file_for_job $model_name $n_events $seed $submission_dir)
    condor_submit $job_path
done

# Move the following code to their own scripts?

# Create script to hadd output files
echo "#!/bin/bash
echo \"Warning: May take a while to hadd if many files are present\"
${SVJ_TOP_DIR}/Utils/haddnano.py $work_space/output/${model_name}_nanoAOD_final.root $work_space/output/${model_name}*NANOAOD*.root
mkdir $work_space/output/components
mv $work_space/output/${model_name}*NANOAOD*.root $work_space/output/components/
" > $work_space/combineOutput_${model_name}.sh

chmod +x $work_space/combineOutput_${model_name}.sh

# Create script to check for failed jobs and resubmit
echo "#!/bin/bash
# Resubmit failed jobs by running this script. It checks to see if the output nanoAOD file is present for each seed. 
# Note that this should only be performed when all jobs have finished running.
for i in \$(seq 0 1 $(( $n_jobs-1 ))); do
    if [ ! -r $work_space/output/${model_name}_NANOAOD_\$i.root ]; then
        condor_submit $work_space/submission_scripts/$model_name/condor_submission_\$i.job
    fi
done
" > $work_space/resubmit_${model_name}.sh

chmod +x $work_space/resubmit_${model_name}.sh

exit
