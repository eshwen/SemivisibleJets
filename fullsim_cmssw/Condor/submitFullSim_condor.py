#!/usr/bin/env python2
""" Handle the input and parsing from a YAML config file, then submit jobs for running FullSim sample production chain """
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys
try:
    from check_config import thorough_checks
except ImportError:
    sys.exit('Please source the setup script first.')
from colorama import Fore, init
from load_yaml_config import load_yaml_config
import os
from subprocess import call
from writers.write_GS_fragment import write_GS_fragment
from writers.write_combine_script import write_combine_script
from writers.write_resubmitter_script import write_resubmitter_script

# Reset text colours after colourful print statements
init(autoreset=True)

# Define some global variables
this_dir = os.path.dirname(os.path.realpath(__file__))
this_sys = os.environ['SCRAM_ARCH']

parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("config", type=str, help="Path to YAML config to parse")
args = parser.parse_args()


def write_submission_script(work_space, gen_frag, lhe_base, model, n_events, queue=1, seed=None):
    """
    Write the HTCondor submission script for sample generation.
    """
    disk = 50000 * n_events  # kB
    runtime = 288 * n_events  # seconds
    if 'soolin' in os.environ['HOSTNAME'] or lhe_base.startswith('root://'):
        grid_proxy = "use_x509userproxy = true"
    else:
        grid_proxy = ""

    body = """# HTCondor submission script
Universe   = vanilla
cmd        = {this_dir}/runFullSim_condor.sh
args       = {work_space} {gen_frag} {lhe_base}_$(Process).lhe {model} {n_events:.0f} $(Process)
Log        = {work_space}/logs/{model}/condor_job_$(Process).log
Output     = {work_space}/logs/{model}/condor_job_$(Process).out
Error      = {work_space}/logs/{model}/condor_job_$(Process).error
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT_OR_EVICT
{grid_proxy}
# Resource requests (disk storage in kB, memory in MB)
request_cpus = 1
# Disk request size determined by n_events
request_disk = {disk}
request_memory = 5000
# Max runtime (seconds) determined by n_events
+MaxRuntime = {runtime}
# Require non-SLC7/CentOS7 machines
Requirements = (OpSysAndVer == "SLCern6")
# Number of instances of job to run
queue {queue}
""".format(this_dir=this_dir, work_space=work_space, gen_frag=gen_frag,
           lhe_base=lhe_base, model=model, n_events=n_events, disk=disk,
           runtime=runtime, grid_proxy=grid_proxy, queue=queue)

    job_file = os.path.join(work_space, 'submission_scripts', model, 'condor_submission_all.job')
    # Edit submission script file name and body if writing individual files
    if seed is not None:
        job_file = job_file.replace('all.job', '{}.job'.format(seed))
        body = body.replace('$(Process)', str(seed))

    with open(job_file, 'w') as f:
        f.write(body)

    call('chmod +x {}'.format(job_file), shell=True)
    return job_file


def main():
    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = load_yaml_config(args.config)

    work_space = input_params['work_space']
    lhe_file_path = input_params['lhe_file_path']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    model_name = input_params['model_name']

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
        print "Work space doesn't exist. Creating it now..."
        os.makedirs(work_space)

    # Initialise proxy of grid certificate if required
    if 'root://' in lhe_file_path:
        grid_cert_path = '{}/x509up_u{}'.format(work_space, os.getuid())
        call('voms-proxy-init --voms cms --valid 168:00 --out {}'.format(grid_cert_path), shell=True)
        os.environ['X509_USER_PROXY'] = grid_cert_path

    # Dict for architectures corresponding to different CMSSW versions
    init_cmssw = 'CMSSW_7_1_30'
    init_arch = 'slc6_amd64_gcc481'
    cmssw_archs = {
        init_cmssw: init_arch,
        'CMSSW_8_0_21': 'slc6_amd64_gcc530',
        'CMSSW_9_4_4': 'slc6_amd64_gcc630',
    }

    # Set up CMSSW environments
    for version, arch in cmssw_archs.iteritems():
        if os.path.exists(os.path.join(work_space, version, 'src')):
            print "{} release already exists!".format(version)
        else:
            _run = '{}/sourceCMSSW.sh {} {} {}'.format(this_dir, version, arch, work_space)
            if this_sys.startswith('slc6'):
                call(_run, shell=True)
            else:
                # Use singularity to initialise CMSSW in a SLC6 env
                call('{}/run_singularity.sh "{}"'.format(this_dir, _run), shell=True)

    if os.getcwd() != this_dir:
        os.chdir(this_dir)

    # Install new Pythia version if not already done so. Use singularity if required
    if all(x.startswith('slc6') for x in [this_sys, init_arch]):
        call('{0}/sourceNewPythiaVer.sh {1} {2} {0}'.format(this_dir, work_space, init_cmssw), shell=True)
    else:
        call('{0}/run_singularity.sh "{0}/sourceNewPythiaVer.sh {1} {2} {0}"'.format(this_dir, work_space, init_cmssw), shell=True)

    # Create directories for gen fragments to occupy
    gen_frag_dir = os.path.join(work_space, init_cmssw, 'src', 'Configuration', 'GenProduction', 'python')
    if not os.path.exists(gen_frag_dir):
        os.makedirs(gen_frag_dir)

    # Create directories for logs, submission scripts and GS fragments
    extra_fullsim_dirs = [
        'logs/{}'.format(model_name),
        'output',
        'submission_scripts/{}'.format(model_name),
    ]

    for dir in extra_fullsim_dirs:
        if not os.path.exists(os.path.join(work_space, dir)):
            os.makedirs(os.path.join(work_space, dir))

    # Create the gen fragment
    gen_frag = os.path.basename(write_GS_fragment(args.config, gen_frag_dir))

    # Create scripts to hadd output files and resubmit failed jobs
    write_combine_script(work_space, model_name)
    write_resubmitter_script(work_space, model_name, n_jobs)

    lhe_base = os.path.join(lhe_file_path, '{}_split'.format(model_name))
    sub_args = (work_space, gen_frag, lhe_base, model_name, n_events)
    # Write a single job file to submit everything at once
    job_main = write_submission_script(*sub_args, queue=n_jobs)
    call('condor_submit -batch-name {} {}'.format(model_name, job_main), shell=True)
    print Fore.MAGENTA + "Jobs submitted. Monitor them with 'condor_q $USER'"

    print Fore.CYAN + "Writing individual job files to make resubmitting failed jobs easier..."
    for seed in xrange(n_jobs):
        job_path = write_submission_script(*sub_args, seed=seed)  # Consider **kwargs instead


if __name__ == '__main__':
    main()
    sys.exit("Done")
