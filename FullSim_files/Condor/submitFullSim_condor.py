import argparse
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
import yaml
import calcDarkParams as cDP


# Reset text colours after colourful print statements
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("config", type=str, help="Path to YAML config to parse")
args = parser.parse_args()



def write_submission_script(work_space, gen_frag, lhe_file, model, n_events, seed, submission_dir):
    """
    Write the HTCondor submission script for sample generation.
    """

    disk_req = 50000 * n_events # kB
    runtime_req= 288 * n_events # seconds

    job_path = os.path.join(work_space, 'submission_scripts', model, 'condor_submission_{}.job'.format(seed))
    job_file = open(job_path, 'w')
    job_file.write("""# HTCondor submission script
Universe   = vanilla
cmd        = {submission_dir}/runFullSim_condor.sh
args       = {work_space} {gen_fragment} {lhe_file} {model} {n_events:.0f} {seed:.0f}
Log        = {work_space}/logs/{model}/condor_job_{seed}.log
Output     = {work_space}/logs/{model}/condor_job_{seed}.out
Error      = {work_space}/logs/{model}/condor_job_{seed}.error
getenv     = True
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT_OR_EVICT
{grid_proxy}
# Resource requests (disk storage in kB, memory in MB)
request_cpus = 1
# Disk request size determined by n_events
request_disk = {disk_req}
request_memory = 5000
# Max runtime (seconds) determined by n_events
+MaxRuntime = {runtime_req}
# Number of instances of job to run
queue 1
""".format(submission_dir=submission_dir, work_space=work_space, gen_fragment=gen_frag,
           lhe_file=lhe_file, model=model, n_events=n_events,
           seed=seed, disk_req=disk_req, runtime_req=runtime_req,
           grid_proxy="use_x509userproxy = true" if 'soolin' in os.environ['HOSTNAME'] or 'root://' in lhe_file else '')
                   )
    job_file.close()

    call('chmod +x {0}'.format(job_path), shell=True)
    return job_path



def main():
    """
    Handle the input and parsing from a YAML config file, then submit jobs for running FullSim sample production chain.
    """

    submission_dir = os.getcwd()

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = load_yaml_config(args.config)

    work_space = input_params['work_space']
    lhe_file_path = input_params['lhe_file_path']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    model_name = input_params['model_name']
    alpha_d = input_params['alpha_d']
    m_d = input_params['m_d']
    n_f = input_params['n_f']

    # Check arguments in config file
    thorough_checks(input_params)


    # Calculate Lambda_d (confinement scale)
    n_c = 2
    Lambda_d = cDP.calcLambdaD(n_c, n_f, alpha_d)
    print Fore.MAGENTA + "Confinement scale Lambda_d =", Lambda_d

    # Rescale Lambda_d if too low (should be >= m_d), then recalc alpha_d
    #if Lambda_d < m_d:
    #    Lambda_d = 1.1 * m_d
    #    alpha_d = cDP.calcAlphaD(n_c, n_f, Lambda_d)
    #    print Fore.MAGENTA + "Recalculated alpha_d =", alpha_d


    # Make a list of split LHE files to run over
    lhe_file_list = []
    for lheFile in os.listdir(lhe_file_path):
        if '{}_split'.format(model_name) in lheFile:
            lhe_file_list.append( os.path.join(lhe_file_path, lheFile) )

    if n_jobs > len(lhe_file_list):
        sys.exit('Number of jobs exceeds number of LHE files in directory. Check and try again.')

    if not os.path.exists(work_space):
        print "Work space doesn't exist. Creating it now..."
        os.makedirs(work_space)

    # Initialise proxy of grid certificate if required
    if 'root://' in lhe_file_path:
        grid_cert_path = '{0}/x509up_u{1}'.format(work_space, os.getuid())
        call('voms-proxy-init --voms cms --valid 168:00 --out {}'.format(grid_cert_path), shell=True)
        os.environ['X509_USER_PROXY'] = grid_cert_path


    # Dict for architectures corresponding to different CMSSW versions
    cmssw_archs = {
        'CMSSW_7_1_30': 'slc6_amd64_gcc481',
        'CMSSW_8_0_21': 'slc6_amd64_gcc530',
        'CMSSW_9_4_4' : 'slc6_amd64_gcc630',
    }

    # Set up CMSSW environments
    for cmssw_ver, arch in cmssw_archs.iteritems():
        if os.path.exists( os.path.join(work_space, cmssw_ver, 'src') ):
            print "{0} release already exists!".format(cmssw_ver)
        else:
            call('./sourceCMSSW.sh {0} {1} {2}'.format(cmssw_ver, arch, work_space), shell=True)

    if os.getcwd() != submission_dir:
        os.chdir(submission_dir)

    # Install new Pythia version if not already done so
    call('./sourceNewPythiaVer.sh {0} {1} {2}'.format(work_space, 'CMSSW_7_1_30', submission_dir), shell=True)

    # Create directories for gen fragments to occupy
    gen_fragment_dir = os.path.join(work_space, 'CMSSW_7_1_30', 'src', 'Configuration', 'GenProduction', 'python')
    if not os.path.exists(gen_fragment_dir):
        os.makedirs(gen_fragment_dir)

    # Create directories for logs, submission scripts and GS fragments
    extra_fullsim_dirs = [
        'logs/{}'.format(model_name),
        'output',
        'submission_scripts/{}'.format(model_name),
    ]

    for dir in extra_fullsim_dirs:
        if not os.path.exists( os.path.join(work_space, dir) ):
            os.makedirs( os.path.join(work_space, dir) )
    

    # Create the gen fragment
    gen_frag_file = os.path.basename( write_GS_fragment(args.config, Lambda_d, gen_fragment_dir) )

    # Create scripts to hadd output files and resubmit failed jobs
    call('python {0}/writers/write_combine_script.py -w {1} -m {2}'.format(submission_dir, work_space, model_name), shell=True)
    call('python {0}/writers/write_resubmitter_script.py -w {1} -m {2} -n {3}'.format(submission_dir, work_space, model_name, n_jobs), shell=True)


    # Write Condor submission file for each job and execute
    for seed in xrange(n_jobs):
        lhe_file_for_job = lhe_file_list[seed]

        sub_args = (work_space, gen_frag_file, lhe_file_for_job, model_name, n_events, seed, submission_dir)
        job_path = write_submission_script(*sub_args) # Consider **kwargs instead
        print Fore.CYAN + "Submitting job {0}/{1}...".format(seed+1, n_jobs)
        call('condor_submit {}'.format(job_path), shell=True)



if __name__ == '__main__':
    main()
