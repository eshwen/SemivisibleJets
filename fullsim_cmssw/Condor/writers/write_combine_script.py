#!/usr/bin/env python2
""" Write bash script to hadd output nanoAOD files """
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from colorama import Fore, Style
import os
from subprocess import call


def write_combine_script(work_space, model_name):
    svj_top_dir = os.environ['SVJ_TOP_DIR']

    file_path = os.path.join(work_space, "combine_components_{}.sh".format(model_name))
    with open(file_path, "w") as f:
        # Write bash combine script
        f.write("""#!/bin/bash
echo -e "\e[1;33mWarning: May take a while to hadd if many files are present.\e[0m"
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh
work_space="{work_space}"
cd $work_space/CMSSW_9_4_4/src # Try to make this not hardcoded in case that version doesn't exist
cmsenv
cd $work_space

# Capture output of hadding command in file to check for errors
temp_file=$(mktemp)

{SVJ_top_dir}/utils/haddnano.py $work_space/output/{model}_nanoAOD_final.root $work_space/output/{model}*NANOAOD*.root 2>&1 | tee $temp_file

if [ ! -d $work_space/output/components ]; then
    mkdir $work_space/output/components
fi

if grep -rq "Error in <TFile\|has size 0\|AttributeError\|Traceback" $temp_file > /dev/null; then
    echo -e "\e[1;32mFound an error while combining files. Check the output and try again. If you're struggling to locate the offending file (and getting an error related to missing leaves), try doing `ls -alrth <files>` and check the files with the smallest sizes.\e[0m"
else
    mv $work_space/output/{model}_NANOAOD_*.root $work_space/output/components
fi

exit
""".format(work_space=work_space, SVJ_top_dir=svj_top_dir, model=model_name)
        )

    call("chmod +x {}".format(file_path), shell=True)
    print Fore.MAGENTA + "Hadding script written!", Style.RESET_ALL


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("work_space", type=str, help="Work space containing CMSSW releases, input and output files")
    parser.add_argument("model_name", type=str, help="Identifying name of model")
    args = parser.parse_args()

    write_combine_script(args.work_space, args.model_name)
