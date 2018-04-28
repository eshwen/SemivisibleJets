#!/bin/bash

# Write the HTCondor submission script for sample generation

work_space=$1
gen_frag_path=$2
lhe_file_path=$3
model_name=$4
n_events=$5
seed=$6
submission_dir=$7

job_path="$work_space/submission_scripts/$model_name/condor_submission_${seed}.job"

echo "# HTCondor submission script
Universe   = vanilla
cmd        = $submission_dir/runFullSim_condor.sh
args       = $work_space $gen_frag_path $lhe_file_path $model_name $n_events $seed
Log        = $work_space/logs/$model_name/condor_job_${seed}.log
Output     = $work_space/logs/$model_name/condor_job_${seed}.out
Error      = $work_space/logs/$model_name/condor_job_${seed}.error
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT_OR_EVICT
" > $job_path

if [[ "$HOSTNAME" == "soolin"* ]]; then          
    echo "use_x509userproxy = true" >> $job_path
fi

echo "# Resource requests (disk storage in kB, memory in MB)
request_cpus = 1
# Disk request size determined by n_events (1 GB per 100 events)
request_disk = $(( 10000*${n_events} ))
request_memory = 2500
# Max runtime determined by n_events in job (4 hrs per 100 events)
+MaxRuntime = $(( 144*${n_events} ))
# Number of instances of job to run
queue 1
" >> $job_path

chmod +x $job_path

# Basically return statement
echo $job_path