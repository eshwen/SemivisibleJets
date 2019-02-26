#!/usr/bin/env bash

# Run Kevin's miniAODs through to nanoAOD locally. Re-run if command gets interrupted. Checks should take care of everything

work_space="/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor_Kevin"
ext_dir="root://cmseos.fnal.gov///store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD"
model="step4_MINIAOD_mZprime-1000_mDark-20_rinv-0.3_alpha-peak_n-1000"
n_files=100
n_events=1000

python writers/write_combine_script.py -w $work_space -m $model

# Starting file should be 1 if running from beginning. But if command gets interrupted, will start from most recent file
n_completed=$(ls -l ${work_space}/output/${model}*.root | wc -l)
if (( $n_completed > 0 )); then
    starting_file=$n_completed
else
    starting_file=1
fi

for seed in $(seq $starting_file 1 $n_files); do seed=$(echo $seed | bc); ./runNanoAOD_Kevin_samples_2016.sh $work_space ${ext_dir}/${model}_part-${seed}.root $model $n_events $seed; done
