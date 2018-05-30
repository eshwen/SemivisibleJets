#!/usr/bin/env python2
import argparse
from colorama import Fore, Style
import os
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--work_space", type = str, required = True, help = "Work space containing CMSSW releases, input and output files")
parser.add_argument("-m", "--model_name", type = str, required = True, help = "Identifying name of model")
args = parser.parse_args()

def main():
    """
    Write bash script to hadd output nanoAOD files
    """

    work_space = args.work_space
    model_name = args.model_name
    svj_top_dir = os.environ['SVJ_TOP_DIR']

    filePath = os.path.join(work_space, "combineOutput_{0}.sh".format(model_name))
    writeFile = open(filePath, "w")

    # Write bash combine script
    writeFile.write("""#!/bin/bash
printf "\e[1;33mWarning: May take a while to hadd if many files are present\n\e[0m"
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh 
cd {0}/CMSSW_9_4_4/src
cmsenv
cd {0}
{1}/Utils/haddnano.py {0}/output/{2}_nanoAOD_final.root {0}/output/{2}*NANOAOD*.root

if [ ! -d {0}/output/components ]; then
    mkdir {0}/output/components
fi

mv {0}/output/{2}_NANOAOD_*.root {0}/output/components
    """.format(work_space, svj_top_dir, model_name)
    )
    writeFile.close()

    call("chmod +x {0}".format(filePath), shell = True)
    print Fore.MAGENTA + "Hadding script written!", Style.RESET_ALL


if __name__ == '__main__':
    main()

