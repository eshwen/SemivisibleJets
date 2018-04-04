#!/bin/bash

if [ -z $1 ]; then
echo "----------------------------------------------------------------------------------------------
Usage ./runFullSim_condor.sh WORKING_DIRECTORY PATH_TO_GEN_FRAGMENT PATH_TO_LHE_FILE_WITH_COMMON_BASENAME MODEL_NAME N_EVENTS N_JOBS
----------------------------------------------------------------------------------------------"
    exit
fi

submission_dir=$PWD

work_space=$(readlink -m $1)
if [ ! -d work_space ]; then
    echo "Work space doesn't exist. Creating it now..."
    mkdir -p $work_space
fi

# GEN fragment should include hadroniser as GEN-SIM is first step
gen_frag_path=$(readlink -m $2)
# This should be the path to the LHE files with the common basename associated, e.g., for ./lheFile_XXX.lhe, the argument should be ./lheFile
# For simplicity, use the splitLHE.py script on the large LHE file to generate the smaller ones to be given to the jobs
lhe_file_path=$(readlink -m $3)
model_name=$4
n_events=$5 # number of events per job
n_jobs=$6

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

# Create directories for logs and submissions scripts
if [ ! -d $work_space/logs ]; then
		    mkdir $work_space/logs
	fi

if [ ! -d $work_space/submission_scripts ]; then
		    mkdir $work_space/submission_scripts
	fi

# Write Condor submission files for each job and execute
for seed in $(seq 1 1 $n_jobs); do
    seed=$(echo $seed | bc)
    lhe_file_for_job=${lhe_file_path}_${seed}.lhe
    
    $submission_dir/write_submission_script.sh $work_space $gen_frag_path $lhe_file_for_job $model_name $n_events $seed $submission_dir
	condor_submit $work_space/submission_scripts/condor_submission_${seed}.job
    done

echo "#!/bin/bash 
$submission_dir/../../Utils/haddnano.py $work_space/output/${model_name}_nanoAOD_final.root $work_space/output/*NANOAOD*.root
mkdir $work_space/output/components
mv $work_space/output/*NANOAOD*.root $work_space/output/components/
" > $work_space/combineOutput.sh

chmod +x $work_space/combineOutput.sh

exit