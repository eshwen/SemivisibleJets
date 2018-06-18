import argparse
import sys
try:
    from checkConfig import performThoroughChecks
except ImportError:
    sys.exit('Please source the setup script first.')
from colorama import Fore, init
from loadYamlConfig import loadYamlConfig
import os
from subprocess import call
from writers.write_GS_fragment import write_GS_fragment
import yaml
import calcDarkParams as cDP


# Reset text colours after colourful print statements
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], "config", "model_params_s_spin1.yaml"), required = True, help = "Path to YAML config to parse")
args = parser.parse_args()



def main():
    """
    Handle the input and parsing from a YAML config file, then submit jobs for running FullSim sample production chain.
    """

    submission_dir = os.getcwd()

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = loadYamlConfig(args.config)

    work_space = input_params['work_space']
    lhe_file_path = input_params['lhe_file_path']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    model_name = input_params['model_name']
    alpha_d = input_params['alpha_d']
    m_d = input_params['m_d']
    n_f = input_params['n_f']

    # Check arguments in config file
    performThoroughChecks(input_params)


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
        if '{0}_split'.format(model_name) in lheFile:
            lhe_file_list.append( os.path.join(lhe_file_path, lheFile) )

    if n_jobs > len(lhe_file_list):
        sys.exit('Number of jobs exceeds number of LHE files in directory. Check and try again.')

    if not os.path.exists(work_space):
        print "Work space doesn't exist. Creating it now.."
        os.makedirs(work_space)


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
        'logs/{0}'.format(model_name),
        'output',
        'submission_scripts/{0}'.format(model_name),
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

        job_path = write_submission_script(work_space, gen_frag_file, lhe_file_for_job, model_name, n_events, seed, submission_dir)
        call('condor_submit {0}'.format(job_path), shell=True)

    # Run the rest of the chain
    #call( "./submitFullSim_condor.sh {0} {1} {2} {3} {4} {5} {6}".format( work_space, lhe_file_path, model_name, n_events, n_jobs, Lambda_d, os.path.abspath(args.config) ), shell = True)



def write_submission_script(work_space, gen_frag_file, lhe_file, model_name, n_events, seed, submission_dir):
    """
    Write the HTCondor submission script for sample generation.
    """

    disk_req = 50000 * n_events # kB
    runtime_req= 288 * n_events # seconds

    job_path = os.path.join(work_space, 'submission_scripts', model_name, 'condor_submission_{0}.job'.format(seed))
    job_file = open(job_path, 'w')
    job_file.write("""# HTCondor submission script
Universe   = vanilla
cmd        = {0}/runFullSim_condor.sh
args       = {1} {2} {3} {4} {5} {6}
Log        = {1}/logs/{4}/condor_job_{6}.log
Output     = {1}/logs/{4}/condor_job_{6}.out
Error      = {1}/logs/{4}/condor_job_{6}.error
getenv     = True
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT_OR_EVICT
# Resource requests (disk storage in kB, memory in MB)
request_cpus = 1
# Disk request size determined by n_events
request_disk = {7}
request_memory = 5000
# Max runtime (seconds) determined by n_events
+MaxRuntime = {8}
# Number of instances of job to run
queue 1
""".format(submission_dir, work_space, gen_frag_file, lhe_file, model_name, n_events, seed, disk_req, runtime_req) )

    if 'soolin' in os.environ['HOSTNAME']:
        job_file.write("use_x509userproxy = true\n")

    job_file.close()

    call('chmod +x {0}'.format(job_path), shell=True)
    return job_path



if __name__ == '__main__':
    main()

