#!/usr/bin/env bash

if [ -z $1 ]; then
    usr_msg="Usage ./run_singularity.sh COMMAND"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

command=$1
echo -e "\e[1mRunning singularity to create a Docker container with an SLC6 environment, allowing the execution of the following: $command\e[0m"

# Allow reusing of cache dir if it exists. Speeds up creation of Docker container
cachedir="/tmp/$(whoami)/singularity_$(date +%Y%m%d%H)"
if [ -d "$cachedir" ]; then
    :
else
    cachedir=$(mkdir -p /tmp/$(whoami)/singularity_$(date +%Y%m%d))
fi
export SINGULARITY_CACHEDIR="$cachedir"

# For singularity >3.0
singularity exec -B /afs,/eos,/cvmfs docker://cmssw/slc6:latest $command
# For singularity <3.0
#singularity shell -B /afs -B /eos -B /cvmfs docker://cmssw/slc6:latest -c "$command"
