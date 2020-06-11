#!/usr/bin/env python2
""" Write bash script to clean up logs, submission scripts, and stray output from a model whose jobs have finished """
from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from colorama import Fore, Style
import os
from subprocess import call


def write_cleanup_script(work_space, model_name):
    svj_top_dir = os.environ['SVJ_TOP_DIR']

    file_path = os.path.join(work_space, "cleanup_residue_{}.sh".format(model_name))
    with open(file_path, "w") as f:
        # Write bash combine script
        f.write("""#!/bin/bash
echo -e "\e[1;33mCleaning up logs, submission scripts, and stray output for {model}...\e[0m"
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh
work_space="{work_space}"
cd $work_space

rm $work_space/output/components/{model}_*.root
rm -rf $work_space/logs/{model}
rm -rf $work_space/submission_scripts/{model}
rm $work_space/CMSSW_*/src/{model}_*.py
rm $work_space/CMSSW_*/src/{model}_*.root
exit
""".format(work_space=work_space, model=model_name)
        )

    call("chmod +x {}".format(file_path), shell=True)
    print(Fore.MAGENTA + "Cleanup script written!", Style.RESET_ALL)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("work_space", type=str, help="Work space containing CMSSW releases, input and output files")
    parser.add_argument("model_name", type=str, help="Identifying name of model")
    args = parser.parse_args()

    write_cleanup_script(args.work_space, args.model_name)
