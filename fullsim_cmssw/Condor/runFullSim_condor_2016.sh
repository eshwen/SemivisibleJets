#!/usr/bin/env bash
# Script to run FullSim CMSSW chain on one LHE file

if [ -z $6 ]; then
    usr_msg="Usage ./runFullSim_condor_2016.sh WORKING_DIRECTORY GEN_FRAGMENT_BASENAME LHE_FILE MODEL_NAME N_EVENTS SEED CMSSW_GS CMSSW_AOD CMSSW_NANO"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

work_space=$(readlink -m $1)
gen_fragment=$2
lhe_file=$(readlink -m $3)
model_name=$4
n_events=$5
seed=$6 # index for job
cmssw_gs="$7"
cmssw_aod="$8"
cmssw_nano="$9"

# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

cd $work_space
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481  # see if I can avoid hardcoding

# If script above cannot be sourced, manually set cmsenv alias
if ! type cmsenv > /dev/null; then
    alias cmsenv='eval `scramv1 runtime -sh`'
fi

cd $cmssw_gs/src
cmsenv
#scram b


# Run the cmsDriver and cmsRun commands for each step in the chain

cmsDriver.py Configuration/GenProduction/python/${gen_fragment} --filein file:${lhe_file} --fileout file:${model_name}_GEN_SIM_${seed}.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V3::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename ${model_name}_GEN_SIM_${seed}.py --no_exec -n $n_events

# Add to CMSSW config in case stringent hadronisation cuts remove all events from a job
sed -i "s/process.options = cms.untracked.PSet(/process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring(\'ProductNotFound\'),/g" ${model_name}_GEN_SIM_${seed}.py
# Add to CMSSW config to ensure Z2 and dark quark filters are used
sed -i "s/seq = process.generator/seq = (process.generator + process.darkhadronZ2filter + process.darkquarkFilter)/g" ${model_name}_GEN_SIM_${seed}.py

cmsRun ${model_name}_GEN_SIM_${seed}.py
echo -e "\e[1;35m**** CREATED GEN-SIM FILE ****\e[0m"

mv ${model_name}_GEN_SIM_${seed}.root ../../$cmssw_aod/src/
cd ../../$cmssw_aod/src
cmsenv

cmsDriver.py step1 --filein file:${model_name}_GEN_SIM_${seed}.root --fileout file:${model_name}_AOD_step1_${seed}.root --pileup_input filelist:"${SVJ_TOP_DIR}/pileup_filelist_2016.txt" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --datamix PreMix --era Run2_2016 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_AOD_step1_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_AOD_step1_${seed}.py
echo -e "\e[1;35m**** CREATED AOD (STEP 1) FILE ****\e[0m"
rm ${model_name}_GEN_SIM_${seed}.root

cmsDriver.py step2 --filein file:${model_name}_AOD_step1_${seed}.root --fileout file:${model_name}_AOD_step2_${seed}.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --era Run2_2016 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_AOD_step2_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_AOD_step2_${seed}.py
echo -e "\e[1;35m**** CREATED AOD (STEP 2) FILE ****\e[0m"
rm ${model_name}_AOD_step1_${seed}.root

cmsDriver.py --filein file:${model_name}_AOD_step2_${seed}.root --fileout file:${model_name}_MINIAOD_${seed}.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --era Run2_2016 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_MINIAOD_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_MINIAOD_${seed}.py
echo -e "\e[1;35m**** CREATED MINIAOD FILE ****\e[0m"
rm ${model_name}_AOD_step2_${seed}.root

mv ${model_name}_MINIAOD_${seed}.root ../../$cmssw_nano/src/
cd ../../$cmssw_nano/src
cmsenv

cmsDriver.py --filein file:${model_name}_MINIAOD_${seed}.root --fileout file:${model_name}_NANOAOD_${seed}.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:run2_mc -s NANO --era Run2_2016,run2_miniAOD_80XLegacy --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_NANOAOD_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_NANOAOD_${seed}.py
echo -e "\e[1;35m**** CREATED NANOAOD FILE ****\e[0m"
rm ${model_name}_MINIAOD_${seed}.root

mv ${model_name}_NANOAOD_${seed}.root $work_space/output/

echo -e "\e[1;36m**** CLEANING UNNECESSARY FILES ****\e[0m"
rm $work_space/$cmssw_gs/src/${model_name}_GEN_SIM_${seed}.py
rm $work_space/$cmssw_aod/src/${model_name}_{AOD_step1,AOD_step2,MINIAOD}_${seed}.py
rm $work_space/$cmssw_nano/src/${model_name}_NANOAOD_${seed}.py

exit
