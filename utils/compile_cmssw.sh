#!/usr/bin/env bash
# Compile a CMSSW release
if [ -z $3 ]; then
    usr_msg="./compile_cmssw.sh WORK_SPACE CMSSW_VERSION ARCH"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

work_space=$1
cmssw_ver=$2

shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=$3

pushd $work_space/$cmssw_ver/src >/dev/null 2>&1
cmsenv
scram b
popd >/dev/null 2>&1
exit
