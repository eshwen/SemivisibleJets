#!/usr/bin/env python2
import argparse
import os
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--work_space", type = str, help = "Work space containing CMSSW releases, input and output files")
parser.add_argument("-m", "--model_name", type = str, help = "Identifying name of model")
parser.add_argument("-n", "--n_jobs", type = int, help = "Number of jobs to be submitted")
args = parser.parse_args()

def main():
    """
    Write bash script to resubmit failed jobs
    """

    work_space = args.work_space
    model_name = args.model_name
    n_jobs_for_loop = args.n_jobs - 1

    filePath = os.path.join(work_space, "resubmit_{0}.sh".format(model_name))
    writeFile = open(filePath, "w")

    # Write bash combine script
    writeFile.write("""#!/bin/bash
# Resubmit failed jobs by running this script. It checks to see if the output nanoAOD file is present for each seed.
# Note that this should only be performed when all jobs have finished running. 
: "${{SVJ_TOP_DIR:?Please source the setup script before running this as environment variables are required.}}; exit"
for i in $(seq 0 1 {0}); do
    if [ ! -r {1}/output/{2}_NANOAOD_$i.root ]; then
        echo "Found no output file for $model_name with seed $i. Resubmitting..."
        condor_submit {1}/submission_scripts/{2}/condor_submission_$i.job
    fi
done
    """.format(n_jobs_for_loop, work_space, model_name)
    )
    writeFile.close()

    call("chmod +x {0}".format(filePath), shell = True)
    print "Resubmission script written!"


if __name__ == '__main__':
    main()

