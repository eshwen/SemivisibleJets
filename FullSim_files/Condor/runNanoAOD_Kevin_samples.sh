#!/usr/bin/env bash
# Script to run FullSim CMSSW chain

if [ -z $1 ]; then
    usr_msg="Usage ./runFullSim_condor.sh WORKING_DIRECTORY GEN_FRAGMENT_BASENAME PATH_TO_LHE_FILES MODEL_NAME N_EVENTS SEED"
    $SVJ_TOP_DIR/Utils/printBashScriptUsage.sh "$usr_msg"
    exit
fi

work_space=$(readlink -m $1)
input_file_path="$2"
model_name=$3
n_events=$4
seed=$5 # index for job

# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

cd $work_space
source /cvmfs/cms.cern.ch/cmsset_default.sh

# If script above cannot be sourced, manually set cmsenv alias
if ! type cmsenv > /dev/null; then
    alias cmsenv='eval `scramv1 runtime -sh`'
fi

cd CMSSW_9_4_4/src
cmsenv

cmsDriver.py --filein file:${input_file_path} --fileout file:${model_name}_NANOAOD_${seed}.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:run2_mc -s NANO --era Run2_2016,run2_miniAOD_80XLegacy --python_filename ${model_name}_NANOAOD_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_NANOAOD_${seed}.py
echo -e "\e[1;35m**** CREATED NANOAOD FILE ****\e[0m"

mv ${model_name}_NANOAOD_${seed}.root $work_space/output/

exit
