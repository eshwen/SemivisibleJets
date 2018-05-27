import argparse
from colorama import Fore, Style
import glob
import os
import pprint
import re
import shutil
from string import Template
from subprocess import call
import sys
import yaml


def performBasicChecks(configDict):
    """
    Performs basic checks of config file parameters that are required for all steps in sample production.
    """

    process_type = configDict['process_type']
    m_med = configDict['m_med']
    n_events = configDict['n_events']
    n_jobs = configDict['n_jobs']
    m_d = configDict['m_d']
    r_inv = configDict['r_inv']

    if not all (type(i) is int for i in [n_events, n_jobs, m_med, m_d]):
        raise TypeError('{0} is required to be an integer.'.format(i))
    if m_d < 0 or m_med < 0:
        raise ValueError('m_d and m_med must be positive.')
    if m_med < 2*m_d:
        raise ValueError('m_med must be greater than 2*m_d for on-shell pair production of the dark quarks.')
    if not 's-channel' in process_type and not 't-channel' in process_type:
        raise ValueError('Unknown process_type specified. Please either specify \'s-channel\' or \'t-channel\'.')
    if r_inv < 0 or r_inv > 1.0:
        raise ValueError('r_inv is required to be in the range 0 < r_inv < 1.0.')
    else:
        print Fore.MAGENTA + "Basic config file check finished. All looks good!", Style.RESET_ALL


def loadConfig(configFile):
    """
    Load the config file into a dictionary.
    """

    configDict = yaml.load( open(configFile, 'r') )
    return configDict


def performThoroughChecks(configDict):
    """
    Performs thorough checks of config file that are required for running FullSim Condor chain.
    """

    performBasicChecks(configDict)

    lhe_file_path = configDict['lhe_file_path']
    alpha_d = configDict['alpha_d']
    n_f = configDict['n_f']
    x_sec = configDict['x_sec']

    if not os.path.exists(lhe_file_path):
        raise ValueError('The LHE file path you have specified does not exist.')
    if not type(n_f) is int:
        raise TypeError('n_f is required to be an integer.')
    if x_sec < 0.0 or alpha_d < 0.0:
        raise ValueError('x_sec and alpha_d must be positive.')
    else:
        print Fore.MAGENTA + "Thorough config file check finished. All looks good!", Style.RESET_ALL

        

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], "config", "model_params_s_spin1.yaml"), help = "Path to YAML config to parse")
    parser.add_argument("-t", "--checkType", type = str, default = "basic", help = "Type of check to perform, either 'basic' or 'thorough'")
    args = parser.parse_args()

    print Fore.MAGENTA + "Checking config file...", Style.RESET_ALL

    configDict = loadConfig(args.config)

    if args.checkType == "basic":
        basicChecks(configDict)

    elif args.checkType == 'thorough':
        performThoroughChecks(configDict)

    sys.exit("Completed")
