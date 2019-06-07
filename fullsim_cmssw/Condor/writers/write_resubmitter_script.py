#!/usr/bin/env python2
""" Write bash script to resubmit failed jobs """
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from colorama import Fore, Style
import os
from subprocess import call


def write_resubmitter_script(work_space, model_name, n_jobs):
    n_jobs_for_loop = n_jobs - 1

    file_path = os.path.join(work_space, "resubmit_{}.sh".format(model_name))
    # Write bash combine script
    with open(file_path, "w") as f:
        f.write("""#!/bin/bash
# Resubmit failed jobs by running this script. It checks to see if the output nanoAOD file is present for each seed.
# Note that this should only be performed when all jobs have finished running.
: "${{SVJ_TOP_DIR:?Please source the setup script before running this as environment variables are required.}}; exit"
    for i in $(seq 0 1 {n_jobs_for_loop}); do
    if [ ! -r {work_space}/output/{model}_NANOAOD_$i.root ]; then
        echo "Found no output file for {model} with seed $i. Resubmitting..."
        condor_submit -batch-name {model} {work_space}/submission_scripts/{model}/condor_submission_$i.job
    fi
done
""".format(n_jobs_for_loop=n_jobs_for_loop, work_space=work_space, model=model_name)
        )

    call("chmod +x {}".format(file_path), shell=True)
    print Fore.MAGENTA + "Resubmission script written!", Style.RESET_ALL


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("work_space", type=str, help="Work space containing CMSSW releases, input and output files")
    parser.add_argument("model_name", type=str, help="Identifying name of model")
    parser.add_argument("n_jobs", type=int, help="Number of jobs to be submitted")
    args = parser.parse_args()

    write_resubmitter_script(*args)
