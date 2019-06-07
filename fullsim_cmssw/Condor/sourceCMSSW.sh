#!/bin/bash

if [ -z $1 ]; then
    usr_msg="Usage ./sourceCMSSW.sh CMSSW_VER ARCH TOP_DIR"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

cmssw_ver=$1
arch=$2
top_dir=$(readlink -m $3)

pushd $top_dir >/dev/null 2>&1

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