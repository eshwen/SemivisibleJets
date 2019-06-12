#!/usr/bin/env bash

if [ -z $1 ]; then
    usr_msg="Usage ./run_singularity.sh COMMAND"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

command=$1
echo "Running singularity to create a Docker container with an SLC6 environment, allowing the execution of the following: $command"

cachedir=$(mktemp -d -t sing-XXXX --tmpdir=/tmp/$(whoami)/singularity)
export SINGULARITY_CACHEDIR="$cachedir"
# For singularity >3.0
singularity exec -B /afs,/eos,/cvmfs docker://cmssw/slc6:latest $command
# For singularity <3.0
#singularity shell -B /afs -B /eos -B /cvmfs docker://cmssw/slc6:latest -c "$command"
