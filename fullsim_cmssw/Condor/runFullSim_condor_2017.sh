#!/usr/bin/env bash
# Script to run FullSim CMSSW chain

if [ -z $7 ]; then
    usr_msg="Usage ./runFullSim_condor_2017.sh WORKING_DIRECTORY GEN_FRAGMENT_BASENAME LHE_FILE MODEL_NAME N_EVENTS SEED PU_FILE"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

work_space=$(readlink -m $1)
gen_fragment=$2
lhe_file=$(readlink -m $3)
model_name=$4
n_events=$5
seed=$6 # index for job
pu_file=$(readlink -m $7)

# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

cd $work_space
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc630

# If script above cannot be sourced, manually set cmsenv alias
if ! type cmsenv > /dev/null; then
    alias cmsenv='eval `scramv1 runtime -sh`'
fi

# Write so CMSSW versions aren't hardcoded, but can take from dict in submitFullSim_condor.py or something
cmssw_gs="CMSSW_9_3_15"
cmssw_aod="CMSSW_9_4_7"
cmssw_nano="CMSSW_10_2_15"
cd $cmssw_gs/src
cmsenv
#scram b


# Run the cmsDriver and cmsRun commands for each step in the chain

cmsDriver.py Configuration/GenProduction/python/${gen_fragment} --filein file:${lhe_file} --fileout file:${model_name}_GEN_SIM_${seed}.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_GEN_SIM_${seed}.py --no_exec -n $n_events

# Add to CMSSW config in case stringent hadronisation cuts remove all events from a job
sed -i "s/process.options = cms.untracked.PSet(/process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring(\'ProductNotFound\'),/g" ${model_name}_GEN_SIM_${seed}.py
# Add to CMSSW config to ensure Z2 and dark quark filters are used
sed -i "s/seq = process.generator/seq = (process.generator + process.darkhadronZ2filter + process.darkquarkFilter)/g" ${model_name}_GEN_SIM_${seed}.py

cmsRun ${model_name}_GEN_SIM_${seed}.py
echo -e "\e[1;35m**** CREATED GEN-SIM FILE ****\e[0m"

mv ${model_name}_GEN_SIM_${seed}.root ../../$cmssw_aod/src/
cd ../../$cmssw_aod/src
cmsenv

cmsDriver.py step1 --filein file:${model_name}_GEN_SIM_${seed}.root --fileout file:${model_name}_AOD_step1_${seed}.root --pileup_input filelist:$pu_file --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --datamix PreMix --era Run2_2017 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_AOD_step1_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_AOD_step1_${seed}.py
echo -e "\e[1;35m**** CREATED AOD (STEP 1) FILE ****\e[0m"
rm ${model_name}_GEN_SIM_${seed}.root

cmsDriver.py step2 --filein file:${model_name}_AOD_step1_${seed}.root --fileout file:${model_name}_AOD_step2_${seed}.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --era Run2_2017 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_AOD_step2_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_AOD_step2_${seed}.py
echo -e "\e[1;35m**** CREATED AOD (STEP 2) FILE ****\e[0m"
rm ${model_name}_AOD_step1_${seed}.root

cmsDriver.py --filein file:${model_name}_AOD_step2_${seed}.root --fileout file:${model_name}_MINIAOD_${seed}.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_MINIAOD_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_MINIAOD_${seed}.py
echo -e "\e[1;35m**** CREATED MINIAOD FILE ****\e[0m"
rm ${model_name}_AOD_step2_${seed}.root

mv ${model_name}_MINIAOD_${seed}.root ../../$cmssw_nano/src/
cd ../../$cmssw_nano/src
cmsenv

cmsDriver.py --filein file:${model_name}_MINIAOD_${seed}.root --fileout file:${model_name}_NANOAOD_${seed}.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_mc2017_realistic_v7 --step NANO --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${model_name}_NANOAOD_${seed}.py --no_exec -n $n_events

cmsRun ${model_name}_NANOAOD_${seed}.py
echo -e "\e[1;35m**** CREATED NANOAOD FILE ****\e[0m"
rm ${model_name}_MINIAOD_${seed}.root

mv ${model_name}_NANOAOD_${seed}.root $work_space/output/

echo -e "\e[1;36m**** CLEANING UNNECESSARY FILES ****\e[0m"
rm $work_space/$cmssw_gs/src/${model_name}_GEN_SIM_${seed}.py
rm $work_space/$cmssw_aod/src/${model_name}_{AOD_step1,AOD_step2,MINIAOD}_${seed}.py
rm $work_space/$cmssw_nano/src/${model_name}_NANOAOD_${seed}.py

exit
