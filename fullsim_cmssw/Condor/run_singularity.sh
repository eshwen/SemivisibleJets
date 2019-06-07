#!/bin/bash

if [ -z $1 ]; then
    usr_msg="Usage ./run_singularity.sh COMMAND"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

command="$1"

cachedir=$(mktemp -d -t sing-XXXX --tmpdir=/tmp/$(whoami)/singularity)
export SINGULARITY_CACHEDIR="$cachedir"
singularity shell -B /afs -B /eos -B /cvmfs docker://cmssw/slc6:latest -c "$command"
