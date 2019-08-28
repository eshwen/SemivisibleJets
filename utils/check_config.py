#!/usr/bin/env python2
""" Perform some checks for the YAML config files """
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from colorama import Fore, Style
from load_yaml_config import load_yaml_config
import os
import sys
import yaml


def basic_checks(config_dict):
    """
    Performs basic checks of config file parameters that are required for all steps in sample production.
    """
    process_type = config_dict['process_type']
    m_med = config_dict['m_med']
    n_events = config_dict['n_events']
    n_jobs = config_dict['n_jobs']
    m_d = config_dict['m_d']
    r_inv = config_dict['r_inv']
    year = config_dict['year']

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
    if not any(year == y for y in [2016, 2017, 2018]):
        raise ValueError(Fore.GREEN + 'year must be 2016, 2017, or 2018.')
    else:
        print Fore.MAGENTA + "Basic config file check finished. All looks good!", Style.RESET_ALL


def thorough_checks(config_dict):
    """
    Performs thorough checks of config file that are required for running FullSim Condor chain.
    """

    basic_checks(config_dict)

    lhe_file_path = config_dict['lhe_file_path']
    alpha_d = config_dict['alpha_d']
    n_f = config_dict['n_f']
    x_sec_mg = config_dict['x_sec_mg']

    if 'root://' not in lhe_file_path and not os.path.exists(lhe_file_path):
        raise ValueError(Fore.GREEN + 'The LHE file path you have specified does not exist.')
    if not type(n_f) is int:
        raise TypeError(Fore.GREEN + 'n_f is required to be an integer.')
    if x_sec_mg < 0.0 or (isinstance(alpha_d, float) and alpha_d < 0.0):
        raise ValueError(Fore.GREEN + 'x_sec and alpha_d must be positive.')
    if isinstance(alpha_d, str) and not any(alpha_d == x for x in ['peak', 'low', 'high']):
        raise ValueError("If specifying alpha_d as a string, it must equal 'peak', 'low', or 'high'.")
    else:
        print Fore.MAGENTA + "Thorough config file check finished. All looks good!", Style.RESET_ALL

        
if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("config", type=file, help="Path to YAML config to parse")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--basic', action="store_true", help="Perform basic config checks")
    group.add_argument('-t', '--thorough', action="store_true", help="Perform thorough config checks")

    args = parser.parse_args()

    print Fore.MAGENTA + "Checking config file...", Style.RESET_ALL
    config_dict = load_yaml_config(args.config)

    if args.basic:
        basic_checks(config_dict)
    elif args.thorough:
        thorough_checks(config_dict)
    sys.exit("Completed")
