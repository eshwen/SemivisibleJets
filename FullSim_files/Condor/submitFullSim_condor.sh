#!/bin/bash

if [ -z $1 ]; then
    echo "-----------------------------------------------------------------------------------------------------
Usage ./runFullSim_condor.sh work_space lhe_file_path model_name n_events n_jobs Lambda_d config_file
-----------------------------------------------------------------------------------------------------"
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
model_name=$3
declare -a lhe_file_list=( $(echo ${lhe_file_path}/${model_name}_split*.lhe | tr ' ' '\n' | sort -h) ) # Need to fix sorting
n_lhe_files=`echo ${#lhe_file_list[@]}`

n_events=$4
n_jobs=$5

if (( $n_jobs > $n_lhe_files )); then
    echo "Number of jobs exceeds number of LHE files in directory. Try again."
    exit
fi

Lambda_d=$6
config_file=$7

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
if [[ ! -d $work_space/{logs{,"/$model_name"},output,submission_scripts{,"/$model_name"}} ]]; then
    mkdir $work_space/{logs{,"/$model_name"},output,submission_scripts{,"/$model_name"}}
fi

# Create the GS fragment
gen_frag_path=$(python $submission_dir/writers/write_GS_fragment.py -c $config_file -l $Lambda_d)

# Write Condor submission file for each job and execute
for seed in $(seq 0 1 $(( $n_jobs-1 ))); do
    seed=$(echo $seed | bc)
    lhe_file_for_job=${lhe_file_list[$seed]}

    # Write Condor submission script and execute
    job_path=$($submission_dir/writers/write_submission_script.sh $work_space $gen_frag_path $lhe_file_for_job $model_name $n_events $seed $submission_dir)
    condor_submit $job_path
done

# Create scripts to hadd output files and resubmit failed jobs
python $submission_dir/writers/write_combine_script.py -w $work_space -m $model_name
python $submission_dir/writers/write_resubmitter_script.py -w $work_space -m $model_name -n $n_jobs

exit
