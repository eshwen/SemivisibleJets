#!/usr/bin/env bash
# Script to run FullSim CMSSW chain

if [ -z $1 ]; then
echo "----------------------------------------------------------------------------------------------
Usage ./runFullSim_condor.sh WORKING_DIRECTORY PATH_TO_GEN_FRAGMENT PATH_TO_LHE_FILE MODEL_NAME N_EVENTS SEED
----------------------------------------------------------------------------------------------"
    exit
fi


work_space=$(readlink -m $1)
gen_frag_path=$(readlink -m $2)
gen_frag_file=$(basename $gen_frag_path)
lhe_file_path=$(readlink -m $3)
model_name=$4
n_events=$5
seed=$6 # index for job

cd $work_space
source /cvmfs/cms.cern.ch/cmsset_default.sh
# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

cd CMSSW_7_1_30/src
cmsenv
if [ -r Configuration/GenProduction/python ]; then
:
else
    mkdir -p Configuration/GenProduction/python
fi

cp $gen_frag_path Configuration/GenProduction/python
scram b
cmsenv


# Run the cmsDriver and cmsRun commands for each step in the chain

cmsDriver.py Configuration/GenProduction/python/${gen_frag_file} --filein file:${lhe_file_path} --fileout file:${model_name}_GEN_SIM_${seed}.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename ${model_name}_GEN_SIM_${seed}.py --no_exec -n $n_events

# Add the following string to CMSSW config in case stringent hadronisation cuts remove all events from a job
sed -i "s/process.options = cms.untracked.PSet(/process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring(\'ProductNotFound\'),/g" ${model_name}_GEN_SIM_${seed}.py

cmsRun ${model_name}_GEN_SIM_${seed}.py
echo "**** CREATED GEN-SIM FILE ****"

cp ${model_name}_GEN_SIM_${seed}.root ../../CMSSW_8_0_21/src/
cd ../../CMSSW_8_0_21/src
cmsenv

cmsDriver.py step1 --filein file:${model_name}_GEN_SIM_${seed}.root --fileout file:${model_name}_AOD_step1_${seed}.root --pileup_input filelist:/afs/cern.ch/user/e/ebhal/Semi-visible_jets/SemivisibleJets/pileup_filelist.txt --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --datamix PreMix --era Run2_2016 --python_filename ${model_name}_AOD_step1_${seed}.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $n_events
cmsRun ${model_name}_AOD_step1_${seed}.py
echo "**** CREATED AOD (STEP 1) FILE ****"

cmsDriver.py step2 --filein file:${model_name}_AOD_step1_${seed}.root --fileout file:${model_name}_AOD_step2_${seed}.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --era Run2_2016 --python_filename ${model_name}_AOD_step2_${seed}.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $n_events
cmsRun ${model_name}_AOD_step2_${seed}.py
echo "**** CREATED AOD (STEP 2) FILE ****"

cmsDriver.py --filein file:${model_name}_AOD_step2_${seed}.root --fileout file:${model_name}_MINIAOD_${seed}.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --era Run2_2016 --python_filename ${model_name}_MINIAOD_${seed}.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $n_events
cmsRun ${model_name}_MINIAOD_${seed}.py
echo "**** CREATED MINIAOD FILE ****"

cp ${model_name}_MINIAOD_${seed}.root ../../CMSSW_9_4_4/src/
cd ../../CMSSW_9_4_4/src
cmsenv

cmsDriver.py --filein file:${model_name}_MINIAOD_${seed}.root --fileout file:${model_name}_NANOAOD_${seed}.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:run2_mc -s NANO --era Run2_2016,run2_miniAOD_80XLegacy --python_filename ${model_name}_NANOAOD_${seed}.py --no_exec -n $n_events
cmsRun ${model_name}_NANOAOD_${seed}.py
echo "**** CREATED NANOAOD FILE ****"

mv ${model_name}_NANOAOD.root ../../

echo "**** CLEANING UP OBSELETE DIRECTORIES AND FILES ****"
rm -rf CMSSW_*

exit
