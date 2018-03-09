#!/usr/bin/env bash
# Script to run FullSim CMSSW chain

if [ -z $1 ]; then
echo "----------------------------------------------------------------------------------
Usage ./runFullSim.sh WORKING_DIRECTORY PATH_TO_GEN_FRAGMENT MODEL_NAME NUM_EVENTS
----------------------------------------------------------------------------------"
    exit
fi


work_space=$(readlink -m $1)
if [ ! -d work_space ]; then
    echo "Work space doesn't exist. Creating it now..."
    mkdir -p $work_space
fi

# GEN fragment should include hadroniser as LHE-GEN-SIM are done in one step
gen_frag_path=$(readlink -m $2)
gen_frag_file=$(basename $gen_frag_path)
model_name=$3
n_events=$4

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

cmsDriver.py Configuration/GenProduction/python/${gen_frag_file} --fileout file:${model_name}_LHE_GEN_SIM.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename ${model_name}_LHE_GEN_SIM.py --no_exec -n $n_events
cmsRun ${model_name}_LHE_GEN_SIM.py
echo "**** CREATED GEN-SIM FILE ****"

cp ${model_name}_LHE_GEN_SIM.root ../../CMSSW_8_0_21/src/
cd ../../CMSSW_8_0_21/src
cmsenv

# Grid certificate required for querying PU dataset
voms-proxy-init --voms cms --valid 168:00

cmsDriver.py step1 --filein file:${model_name}_LHE_GEN_SIM.root --fileout file:${model_name}_AOD_step1.root --pileup_input /store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/100000/001EB167-3781-E611-BE3C-0CC47A4D75F4.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --datamix PreMix --era Run2_2016 --python_filename ${model_name}_AOD_step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $n_events
cmsRun ${model_name}_AOD_step1.py
echo "**** CREATED AOD (STEP 1) FILE ****"

cmsDriver.py step2 --filein file:${model_name}_AOD_step1.root --fileout file:${model_name}_AOD_step2.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --era Run2_2016 --python_filename ${model_name}_AOD_step2.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $n_events
cmsRun ${model_name}_AOD_step2.py
echo "**** CREATED AOD (STEP 2) FILE ****"

cmsDriver.py --filein file:${model_name}_AOD_step2.root --fileout file:${model_name}_MINIAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --era Run2_2016 --python_filename ${model_name}_MINIAOD.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $n_events
cmsRun ${model_name}_MINIAOD.py
echo "**** CREATED MINIAOD FILE ****"

cp ${model_name}_MINIAOD.root ../../CMSSW_9_4_4/src/
cd ../../CMSSW_9_4_4/src
cmsenv

cmsDriver.py --filein file:${model_name}_MINIAOD.root --fileout file:${model_name}_NANOAOD.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:run2_mc -s NANO --era Run2_2016,run2_miniAOD_80XLegacy --python_filename ${model_name}_NANOAOD.py --no_exec -n $n_events
cmsRun ${model_name}_NANOAOD.py
echo "**** CREATED NANOAOD FILE ****"

exit
