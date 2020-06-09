#!/bin/bash

# Create SVJ_TOP_DIR environment variable if setup.sh hasn't been sourced
if [ -z $SVJ_TOP_DIR ]; then
    SVJ_TOP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
fi

CondaVer=3
PythonVer=2  # Using Python 2. Python 3 is not supported by MadGraph and possibly older versions of CMSSW used in FullSim production
MINICONDA_DIR=$SVJ_TOP_DIR/external/miniconda${CondaVer}

if [ -d $MINICONDA_DIR ]; then
    echo "Directory for conda environment already exists. Will use it"
else
    wget https://repo.continuum.io/miniconda/Miniconda${CondaVer}-latest-Linux-x86_64.sh
    bash Miniconda${CondaVer}-latest-Linux-x86_64.sh -b -p $MINICONDA_DIR
    rm Miniconda${CondaVer}-latest-Linux-x86_64.sh
fi

cd $MINICONDA_DIR
source $MINICONDA_DIR/etc/profile.d/conda.sh
conda update -y -n base -c defaults conda
export PYTHONNOUSERSITE=true

conda create -y -n svj_env python=${PythonVer}.7 pip
conda activate svj_env

if (( $PythonVer == 2 )); then
    echo -e "\e[1mInstalling backports.lmza\e[0m"
    conda install -y -c conda-forge backports.lzma  # unneeded with Python 3 as it's included in standard library
fi

echo -e "\e[1mInstalling xrootd\e[0m"
conda install -y -c conda-forge xrootd
echo -e "\e[1mInstalling ROOT\e[0m"
conda install -y -c conda-forge ROOT

cd $SVJ_TOP_DIR
echo -e "\e[1mInstalling requirements for repository\e[0m"
pip install -r requirements.txt

echo -e "\e[1mSuccessfully set up conda environment in $MINICONDA_DIR\e[0m"
