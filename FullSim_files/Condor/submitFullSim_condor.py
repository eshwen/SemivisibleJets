#!/usr/bin/env python2
from subprocess import call
import sys
import yaml

def main():
    """
    Handle the input and parsing from a YAML config file for submitFullSim_condor.sh
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = yaml.load( open("model_params.yaml", 'r') )

    work_space = input_params['work_space']
    gen_frag_path = input_params['gen_frag_path']
    lhe_file_path = input_params['lhe_file_path']
    model_name = input_params['model_name']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']

    call( "./submitFullSim_condor.sh {0} {1} {2} {3} {4} {5}".format( work_space, gen_frag_path, lhe_file_path, model_name, n_events, n_jobs ), shell = True )

if __name__ == '__main__':
    main()
    sys.exit("Completed")
