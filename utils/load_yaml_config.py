from __future__ import print_function
from colorama import deinit, Fore, init, Style
import pprint
import yaml


def load_yaml_config(config_file, quiet=False):
    """
    Parse YAML config file and load into a dictionary.
    """
    # Resets colour env. so config dict can be coloured
    deinit()

    config_dict = yaml.full_load(open(config_file, 'r'))

    if not quiet:
        print("Using config file", config_file)
        print(Style.RESET_ALL, Fore.CYAN + "The arguments you have set are the following:\n", pprint.pprint(config_dict))

    # Reset colourful after print statement
    init(autoreset=True)
    print(Style.RESET_ALL)

    return config_dict
