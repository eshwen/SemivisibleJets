#!/bin/bash

# This script allows a new version of Pythia not present in the architecutre for a given CMSSW version to be downloaded and linked to CMSSW.

if [ -z $1 ]; then
    usr_msg="Usage ./sourceNewPythiaVer.sh WORK_SPACE CMSSW_VER CALL_DIR"
    $SVJ_TOP_DIR/utils/print_bash_script_usage.sh "$usr_msg"
    exit
fi

work_space=$1
cmssw_ver=$2
call_dir=$3 # directory script is called from, so as to return to it after running

# Unset env variables otherwise Pythia module compilation fails
unset CXX
unset COMPILER_PATH
unset CC

# Allow use of aliases (specifically cvmfs ones)
shopt -s expand_aliases

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd $work_space/$cmssw_ver
cmsenv

if [[ "$PYTHIA8DATA" == "${work_space}/${cmssw_ver}/"* ]]; then
    echo -e "\e[1;35mThe new version of Pythia has already been installed. No need to do it again.\e[0m"
else
    # For Pythia 8.230
    cp $SVJ_TOP_DIR/utils/install_pythia8230.sh .
    ./install_pythia8230.sh
    scram b
    cmsenv
    cd $CMSSW_BASE/src
    echo -e "\e[1;35mInstalled Pythia 8.230, replacing the pre-installed version that ships with $cmssw_ver and $SCRAM_ARCH.\e[0m"
fi

cd $call_dir
exit
