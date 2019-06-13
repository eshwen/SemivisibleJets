#!/bin/bash

if [ -z $3 ]; then
    usr_msg="Usage ./sourceCMSSW.sh CMSSW_VER ARCH WORK_SPACE"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

cmssw_ver=$1
arch=$2
work_space=$(readlink -m $3)

pushd $work_space >/dev/null 2>&1

# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=$arch
cmsrel $cmssw_ver
cd ${cmssw_ver}/src
cmsenv
scram b

popd >/dev/null 2>&1
exit
