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
echo -e "\e[1;33mWarning: May take a while to hadd if many files are present.\e[0m"
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh 
cd {work_space}/CMSSW_9_4_4/src # Try to make this not hardcoded in case that version doesn't exist
cmsenv
cd {work_space}

# Capture output of hadding command in file to check for errors
temp_file=$(mktemp)

{SVJ_top_dir}/Utils/haddnano.py {work_space}/output/{model}_nanoAOD_final.root {work_space}/output/{model}*NANOAOD*.root 2>&1 | tee $temp_file

if [ ! -d {work_space}/output/components ]; then
    mkdir {work_space}/output/components
fi

if grep -rq "Error in <TFile\|has size 0\|AttributeError\|Traceback" $temp_file > /dev/null; then
    echo -e "\e[1;32mFound an error while combining files. Check the output and try again.\e[0m"
else
    mv {work_space}/output/{model}_NANOAOD_*.root {work_space}/output/components
fi

exit
    """.format(work_space=work_space, SVJ_top_dir=svj_top_dir, model=model_name)
                    )
    writeFile.close()

    call("chmod +x {0}".format(filePath), shell = True)
    print Fore.MAGENTA + "Hadding script written!", Style.RESET_ALL


if __name__ == '__main__':
    main()

