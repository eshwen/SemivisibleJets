#!/usr/bin/env bash

# Run Kevin's miniAODs through to nanoAOD locally

for seed in $(seq 1 1 100); do seed=$(echo $seed | bc); ./runFullSim_condor_Kevin_samples.sh /afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor_v6 dummy root://cmseos.fnal.gov///store/user/lpcsusyhad/SVJ2017/ProductionV2/MINIAOD/step4_MINIAOD_mZprime-3000_mDark-50_rinv-0.3_alpha-0.2_n-1000_part-${seed}.root step4_MINIAOD_mZprime-3000_mDark-50_rinv-0.3_alpha-0.2_n-1000 500 $seed; done