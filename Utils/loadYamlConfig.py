from colorama import deinit, Fore, init, Style
import pprint
import yaml


def loadYamlConfig(configFile):
    """
    Parse YAML config file and load into a dictionary.
    """
    # Resets colour env. so config dict can be coloured
    deinit()

    print "Using config file", configFile
    configDict = yaml.load( open(configFile, 'r') )

    print Style.RESET_ALL, Fore.CYAN + "The arguments you have set are the following:\n", pprint.pprint(configDict)

    # Reset colourful after print statement
    init(autoreset=True)
    print Style.RESET_ALL

    return configDict
