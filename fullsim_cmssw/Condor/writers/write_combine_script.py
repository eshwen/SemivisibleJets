#!/usr/bin/env python2
""" Write bash script to hadd output nanoAOD files """
from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from colorama import Fore, Style
import os
from subprocess import call


def write_combine_script(work_space, model_name, cmssw_ver):
    svj_top_dir = os.environ['SVJ_TOP_DIR']

    # Noticed weird problem where trying to use PyROOT in a CMSSW_10_X_Y environment fails (possible GCC 7.X problem). So use GCC8 instead
    if cmssw_ver.startswith('CMSSW_10_'):
        gcc_setup = "source /cvmfs/sft.cern.ch/lcg/views/LCG_94/x86_64-centos7-gcc8-opt/setup.sh"
    else:
        gcc_setup = ""

    file_path = os.path.join(work_space, "combine_components_{}.sh".format(model_name))
    with open(file_path, "w") as f:
        # Write bash combine script
        f.write("""#!/bin/bash
echo -e "\e[1;33mWarning: May take a while to hadd if many files are present.\e[0m"
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh
work_space="{work_space}"
cd $work_space/{cmssw_ver}/src
cmsenv
cd $work_space
{gcc_setup}
# Capture output of hadding command in file to check for errors
temp_file=$(mktemp)

{SVJ_top_dir}/utils/haddnano.py $work_space/output/{model}_nanoAOD_final.root $work_space/output/{model}*NANOAOD*.root 2>&1 | tee $temp_file

if [ ! -d $work_space/output/components ]; then
    mkdir $work_space/output/components
fi

if grep -rq "Error in <TFile\|has size 0\|AttributeError\|Traceback\|Offending" $temp_file > /dev/null; then
    echo -e "\e[1;32mFound an error while combining files. Check the output and try again. If you're struggling to locate the offending file (and getting an error related to missing leaves), try doing 'ls -alrth {work_space}/output/{model}_NANOAOD_*.root' and check the files with the smallest sizes.\e[0m"
    rm $work_space/output/{model}_nanoAOD_final.root
else
    mv $work_space/output/{model}_NANOAOD_*.root $work_space/output/components
fi

exit
""".format(work_space=work_space, SVJ_top_dir=svj_top_dir, model=model_name, cmssw_ver=cmssw_ver, gcc_setup=gcc_setup)
        )

    call("chmod +x {}".format(file_path), shell=True)
    print(Fore.MAGENTA + "Hadding script written!", Style.RESET_ALL)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("work_space", type=str, help="Work space containing CMSSW releases, input and output files")
    parser.add_argument("model_name", type=str, help="Identifying name of model")
    parser.add_argument("-c", "--cmssw_ver", type=str, default="CMSSW_9_4_4", help="CMSSW version under which output files are stored")
    args = parser.parse_args()

    write_combine_script(args.work_space, args.model_name, args.cmssw_ver)
