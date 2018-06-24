#!/usr/bin/env bash

# Run Kevin's miniAODs through to nanoAOD locally

work_space=/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor_v6
model=step4_MINIAOD_mZprime-4000_mDark-20_rinv-0.3_alpha-0.2_n-1000
n_files=100
n_events=500

python writers/write_combine_script.py -w $work_space -m $model_name

for seed in $(seq 1 1 $n_files); do seed=$(echo $seed | bc); ./runNanoAOD_Kevin_samples.sh $work_space root://cmseos.fnal.gov///store/user/lpcsusyhad/SVJ2017/ProductionV2/MINIAOD/${model}_part-${seed}.root $model $n_events $seed; done