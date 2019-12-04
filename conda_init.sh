#!/bin/bash

# Create SVJ_TOP_DIR if setup.sh not sourced
if [ -z $SVJ_TOP_DIR ]; then
    SVJ_TOP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
fi

CondaVer=3  # do CondaVer=2 for Python 2
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

conda create -y -n svj_env python=$CondaVer pip
conda activate svj_env

if (( $CondaVer == 2 )); then
    echo -e "\e[1mInstalling backports.lmza\e[0m"
    conda install -y -c conda-forge backports.lzma  # unneeded with Python 3 as it's included in standard library
fi

echo -e "\e[1mInstalling xrootd\e[0m"
conda install -y -c conda-forge xrootd
echo -e "\e[1mInstalling ROOT\e[0m"
conda install -y -c conda-forge ROOT

cd $SVJ_TOP_DIR
pip install -r requirements.txt

echo -e "\e[1mSuccessfully set up conda environment in $MINICONDA_DIR\e[0m"
