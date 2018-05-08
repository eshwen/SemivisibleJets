import argparse
import os
import pprint
import re
import shutil
from subprocess import call
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], "config", "model_params_s_spin1.yaml"), help = "Path to YAML config to parse")
args = parser.parse_args()

def main():
    """
    Handle the input and parsing from a YAML config file, and .

    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    print "Using config file", args.config
    input_params = yaml.load( open(args.config, 'r') )

    print "The arguments you have set are the following:\n", pprint.pprint(input_params)

    work_space = input_params['work_space']
    model_name = input_params['model_name']
    total_events = input_params['total_events']


    default_gridpack_dir = os.path.join(os.environ['MG_GENPROD_DIR'], model_name)

    # Get cross section from gridpack generation log file
    log_file = open(os.path.join(default_gridpack_dir, model_name+'_gridpack', 'work', 'gridpack', 'gridpack_generation.log'), 'r')
    log_str = log_file.read()
    x_sec = re.search("(?<=Cross-section :   )(\d*.\d+)", log_str).group(0)
    log_file.close()
    
    # Append cross section to config file if not included already
    config_read = open(args.config, 'r')
    if 'x_sec:' in config_read.read():
        config_read.close()
    else:
        print "Appending config file with cross section as calculated by MadGraph..."
        config_append = open(args.config, 'a')
        config_append.write("x_sec: {0}\n".format(x_sec))
        config_append.close()

    # COPY GRIDPACK TARBALL TO gridpacks/, RUN runcmsgrid.sh WITH N_EVENTS AND RANDOM SEED ARGUMENTS (FIND FUNCTION TO CREATE RANDOM INTEGER) ON UNTARRED VERSION TO GET LHE FILE, MOVE LHE FILE SOMEWHERE AND DELETE UNTARRED GRIDPACK,  THEN SPLIT LHE FILE AND STORE IN DIRECTORY SPECIFIED BY USER


if __name__ == '__main__':
    main()

