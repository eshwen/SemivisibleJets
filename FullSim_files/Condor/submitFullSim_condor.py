#!/usr/bin/env python2
import argparse
import math
import os
import pprint
from subprocess import call
import sys
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", default = os.path.join(os.getcwd(), "model_params.yaml"), help = "YAML config to parse")
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

    # Calculate b (related to n_colours and n_f) and Lambda_d (confinement scale) from alpha_d
    n_c = 2
    b_param = (11/3)*n_c - (2/3)*n_f
    Lambda_d = 1000 * math.exp( -2*math.pi / (alpha_d*b_param) )

    # Rescale Lambda_d if too low. Should be >= m_d
    if Lambda_d < m_d:
        Lambda_d = 1.1 * m_d

    # SORT OUT ARGUMENTS
    call( "./submitFullSim_condor.sh {0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format( work_space, lhe_file_path, model_name, n_events, n_jobs, Lambda_d, m_d, n_f, r_inv, x_sec ), shell = True )

if __name__ == '__main__':
    main()
#    sys.exit("Completed")
