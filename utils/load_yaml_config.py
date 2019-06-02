from colorama import deinit, Fore, init, Style
import pprint
import yaml


def load_yaml_config(config_file):
    """
    Parse YAML config file and load into a dictionary.
    """
    # Resets colour env. so config dict can be coloured
    deinit()

    print "Using config file", config_file
    configDict = yaml.full_load(open(config_file, 'r'))

    print Style.RESET_ALL, Fore.CYAN + "The arguments you have set are the following:\n", pprint.pprint(configDict)

    # Reset colourful after print statement
    init(autoreset=True)
    print Style.RESET_ALL

    return configDict
