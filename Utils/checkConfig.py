#!/usr/bin/env python2 
import argparse
from colorama import Fore, Style
from loadYamlConfig import loadYamlConfig
import os
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
        raise TypeError(Fore.GREEN + 'n_events, n_jobs, m_med and m_d are all required to be integers.')
    if m_d < 0 or m_med < 0:
        raise ValueError(Fore.GREEN + 'm_d and m_med must be positive.')
    if m_med < 2*m_d:
        raise ValueError(Fore.GREEN + 'm_med must be greater than 2*m_d for on-shell pair production of the dark quarks.')
    if not 's-channel' in process_type and not 't-channel' in process_type:
        raise ValueError(Fore.GREEN + 'Unknown process_type specified. Please either specify \'s-channel\' or \'t-channel\'.')
    if r_inv < 0 or r_inv > 1.0:
        raise ValueError(Fore.GREEN + 'r_inv is required to be in the range 0 < r_inv < 1.0.')
    else:
        print Fore.MAGENTA + "Basic config file check finished. All looks good!", Style.RESET_ALL


def performThoroughChecks(configDict):
    """
    Performs thorough checks of config file that are required for running FullSim Condor chain.
    """

    performBasicChecks(configDict)

    lhe_file_path = configDict['lhe_file_path']
    alpha_d = configDict['alpha_d']
    n_f = configDict['n_f']
    x_sec = configDict['x_sec']

    if 'root://' not in lhe_file_path and not os.path.exists(lhe_file_path):
        raise ValueError(Fore.GREEN + 'The LHE file path you have specified does not exist.')
    if not type(n_f) is int:
        raise TypeError(Fore.GREEN + 'n_f is required to be an integer.')
    if x_sec < 0.0 or alpha_d < 0.0:
        raise ValueError(Fore.GREEN + 'x_sec and alpha_d must be positive.')
    else:
        print Fore.MAGENTA + "Thorough config file check finished. All looks good!", Style.RESET_ALL

        
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], 'config', 'model_params_s_spin1.yaml'), help = "Path to YAML config to parse")
    parser.add_argument('-t', '--checkType', type = str, default = 'basic', help = "Type of check to perform, either 'basic' or 'thorough'")
    args = parser.parse_args()

    print Fore.MAGENTA + "Checking config file...", Style.RESET_ALL

    configDict = loadYamlConfig(args.config)

    if args.checkType == "basic":
        performBasicChecks(configDict)

    elif args.checkType == 'thorough':
        performThoroughChecks(configDict)

    else:
        sys.exit("The --checkType option must be either 'basic' or 'thorough'.")

    sys.exit("Completed")
