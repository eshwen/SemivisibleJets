import argparse
from checkConfig import performThoroughChecks
from colorama import Fore, init
from loadYamlConfig import loadYamlConfig
import os
from subprocess import call
import sys
import yaml
import calcDarkParams as cDP


# Reset text colours after colourful print statements
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], "config", "model_params_s_spin1.yaml"), required = True, help = "Path to YAML config to parse")
args = parser.parse_args()



def main():
    """
    Handle the input and parsing from a YAML config file for submitFullSim_condor.sh
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = loadYamlConfig(args.config)

    work_space = input_params['work_space']
    lhe_file_path = input_params['lhe_file_path']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    model_name = input_params['model_name']
    alpha_d = input_params['alpha_d']
    m_med = input_params['m_med']
    m_d = input_params['m_d']
    n_f = input_params['n_f']
    r_inv = input_params['r_inv']
    x_sec = input_params['x_sec']
    process_type = input_params['process_type']

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

    # Run the rest of the chain
    call( "./submitFullSim_condor.sh {0} {1} {2} {3} {4} {5} {6}".format( work_space, lhe_file_path, model_name, n_events, n_jobs, Lambda_d, os.path.abspath(args.config) ), shell = True)
    


if __name__ == '__main__':
    main()

