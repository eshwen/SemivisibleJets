import argparse
import math
import os
import pprint
from subprocess import call
import sys
import yaml
import calcDarkParams as cDP

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type = str, default = "model_params_s_spin1.yaml", help = "YAML config to parse")
args = parser.parse_args()

def main():
    """
    Handle the input and parsing from a YAML config file for submitFullSim_condor.sh
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    print "Using config file", args.config
    input_params = yaml.load( open(args.config, 'r') )

    print "The arguments you have set are the following:\n", pprint.pprint(input_params)

    # Tidy this in a loop?
    work_space = input_params['work_space']
    lhe_file_path = input_params['lhe_file_path']
    model_name = input_params['model_name']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    alpha_d = input_params['alpha_d']
    m_d = input_params['m_d']
    n_f = input_params['n_f']
    r_inv = input_params['r_inv']
    x_sec = input_params['x_sec']

    # Checking arguments in config file
    if not os.path.exists(lhe_file_path):
        raise ValueError('The LHE file path you have specified does not exist.')

    if not all (type(i) is int for i in [n_events, n_jobs, n_f]):
        raise TypeError('n_events, n_jobs and n_f are all required to be integers.')

    if m_d < 0 or x_sec < 0.0 or  r_inv < 0.0 or r_inv > 1.0:
        raise ValueError('m_d and x_sec must be positive, and 0 < r_inv < 1.')

    # Calculate Lambda_d (confinement scale)
    n_c = 2
    Lambda_d = cDP.calcLambdaD(n_c, n_f, alpha_d)
    print "Confinement scale Lambda_d =", Lambda_d

    # Rescale Lambda_d if too low (should be >= m_d), then recalc alpha_d
    if Lambda_d < m_d:
        Lambda_d = 1.1 * m_d
        alpha_d = cDP.calcAlphaD(n_c, n_f, Lambda_d)
        print "Recalculated alpha_d =", alpha_d

    # Run the rest of the chain
    call( "./submitFullSim_condor.sh {0} {1} {2} {3} {4} {5} {6}".format( work_space, lhe_file_path, model_name, n_events, n_jobs, Lambda_d, os.path.abspath(args.config) ), shell = True)
    

if __name__ == '__main__':
    main()

