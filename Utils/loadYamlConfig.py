from colorama import Fore, Style
import pprint
import yaml

def loadYamlConfig(configFile):
    """
    Parse YAML config file and load into a dictionary.
    """

    print "Using config file", configFile
    configDict = yaml.load( open(configFile, 'r') )

    print Fore.CYAN + "The arguments you have set are the following:\n", pprint.pprint(configDict)
    print Style.RESET_ALL

    return configDict
