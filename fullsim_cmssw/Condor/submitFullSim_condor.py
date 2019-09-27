#!/usr/bin/env python2
""" Submit jobs for running FullSim sample production chain in CMSSW """
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys
try:
    from check_config import thorough_checks
except ImportError:
    sys.exit('Please source the setup script first.')
from colorama import Fore, init
from cmssw_info import CmsswInfo
from htcondor_job import HTCondorJob
from load_yaml_config import load_yaml_config
import os
import shutil
from subprocess import call
from writers.write_GS_fragment import WriteGenSimFragment
from writers.write_combine_script import write_combine_script
from writers.write_resubmitter_script import write_resubmitter_script

# Reset text colours after colourful print statements
init(autoreset=True)


def main(config):
    # Define variable for directory of script
    this_dir = os.path.dirname(os.path.realpath(__file__))

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = load_yaml_config(config)

    work_space = input_params['work_space']
    lhe_file_path = input_params['lhe_file_path']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    model_name = input_params['model_name']
    year = input_params['year']

    # Check arguments in config file
    thorough_checks(input_params)

    # Make a list of split LHE files for checks
    lhe_files = []
    for file in os.listdir(lhe_file_path):
        if '{}_split'.format(model_name) in file and file.endswith('.lhe'):
            lhe_files.append(os.path.join(lhe_file_path, file))

    if n_jobs > len(lhe_files):
        sys.exit('Number of jobs exceeds number of LHE files in directory. Check and try again.')

    if not os.path.exists(work_space):
        print(Fore.CYAN + "Work space doesn't exist. Creating it now...")
        os.makedirs(work_space)

    shutil.copy(os.path.join(os.environ['SVJ_TOP_DIR'], 'pileup_filelist_{}.txt'.format(year)), work_space)

    # Initialise proxy of grid certificate if required
    if 'root://' in lhe_file_path and 'X509_USER_PROXY' not in os.environ.keys():
        grid_cert_path = '{}/x509up_u{}'.format(work_space, os.getuid())
        call('voms-proxy-init --voms cms --valid 168:00 --out {}'.format(grid_cert_path), shell=True)
        os.environ['X509_USER_PROXY'] = grid_cert_path

    # Get CMSSW versions and architecture info
    cmssw_info = CmsswInfo(year)
    cmssw_info.initialise_envs(location=work_space)

    if os.getcwd() != this_dir:
        os.chdir(this_dir)

    # Create additional directories
    gen_frag_dir = os.path.join(work_space, cmssw_info.gensim['version'], 'src', 'Configuration', 'GenProduction', 'python')
    extra_fullsim_dirs = [
        gen_frag_dir,
        '{}/logs/{}'.format(work_space, model_name),
        '{}/output'.format(work_space),
        '{}/submission_scripts/{}'.format(work_space, model_name),
    ]
    for dir in extra_fullsim_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # Create the gen fragment
    gen_frag = os.path.basename(WriteGenSimFragment(config, gen_frag_dir).out_file)

    # Compile after everything is written to ensure gen fragment can be linked to
    cmssw_info.compile_env(location=work_space, version=cmssw_info.gensim['version'], arch=cmssw_info.gensim['arch'])

    # Create scripts to hadd output files and resubmit failed jobs
    write_combine_script(work_space, model_name, cmssw_info.nano['version'])
    write_resubmitter_script(work_space, model_name, n_jobs)

    lhe_base = os.path.join(lhe_file_path, '{}_split'.format(model_name))
    sub_args = (work_space, gen_frag, lhe_base, model_name, n_events, year)
    # Write a single job file to submit everything at once
    main_job = HTCondorJob(*sub_args, queue=n_jobs)
    call('condor_submit {}'.format(main_job.job_file), shell=True)
    print(Fore.MAGENTA + "Jobs submitted. Monitor them with 'condor_q $USER'")

    print(Fore.CYAN + "Writing individual job files to make resubmitting failed jobs easier...")
    for seed in xrange(n_jobs):
        HTCondorJob(*sub_args, seed=seed)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("config", type=str, help="Path to YAML config to parse")
    args = parser.parse_args()

    main(args.config)
    sys.exit("Done")
