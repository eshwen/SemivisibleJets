#!/usr/bin/env python2
""" Handle the input and parsing from a YAML config file.
Run gridpack to retrieve LHE file, then split it and move output to directory specified by user. """
from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys
try:
    from check_config import basic_checks
except ImportError:
    sys.exit('Please source the setup script first.')
from colorama import Fore, init
import glob
from load_yaml_config import load_yaml_config
import os
import random
import re
import shutil
from splitLHE import splitLHE
from subprocess import call

# Reset text colours after colourful print statements
init(autoreset=True)


def main(config):
    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = load_yaml_config(config)

    model_name = input_params['model_name']
    total_events = input_params['total_events']
    n_jobs = input_params['n_jobs']
    out_split_lhe = input_params['lhe_file_path']
    process_type = input_params['process_type']

    # Check arguments in config file
    basic_checks(input_params)

    # Set up some path variables for use later
    genprod_dir = os.environ['MG_GENPROD_DIR']
    default_gridpack_dir = os.path.join(genprod_dir, model_name)
    lhe_gen_dir = os.path.join(default_gridpack_dir, model_name+'_gridpack', 'work', 'gridpack')
    gridpack_outdir = os.path.join(os.environ['SVJ_MG_FILES_DIR'], 'gridpacks')

    # Get cross section from gridpack generation log file
    with open(os.path.join(lhe_gen_dir, 'gridpack_generation.log'), 'r') as f:
        log_str = f.read()
        x_sec_mg = re.search("(?<=Cross-section :   )(\d*.\d+)", log_str).group(0)

    # Append cross section to config file if not included already
    with open(config, 'r+') as f:
        config_str = f.read()
        if str(x_sec_mg) not in config_str:
            print(Fore.CYAN + "Appending config file with cross section as calculated by MadGraph...")
            f.seek(0)
            config_lines = f.readlines()
            f.seek(0)
            f.truncate()
            for i in config_lines:
                if i.startswith('x_sec_mg'):
                    continue
                else:
                    f.write(i)
            f.write("x_sec_mg: {}\n".format(x_sec_mg))

    # Copy gridpack tarball to new directory
    for tarball in glob.glob(os.path.join(genprod_dir, model_name+'*.xz')):
        print(Fore.CYAN + "Copying {} to {}/".format(os.path.basename(tarball), gridpack_outdir))
        shutil.copyfile(tarball, os.path.join(gridpack_outdir, os.path.basename(tarball)))
        os.remove(tarball)

    # Run the script produced with the gridpack to get the LHE file out and copy to gridpacks dir
    seed = random.randint(0, 1000000)
    call("cd {}; ./runcmsgrid.sh {} {}".format(lhe_gen_dir, total_events, seed), shell=True)
    in_lhe = os.path.join(gridpack_outdir, model_name+'_LHE.lhe')
    shutil.copyfile(os.path.join(lhe_gen_dir, 'cmsgrid_final.lhe'), in_lhe)

    # Delete untarred gridpack as it takes up unnecessary space
    shutil.rmtree(default_gridpack_dir)
    print(Fore.MAGENTA + "Removed untarred version of gridpack!")

    # Change PDGIDs for dark particles in preparation for hadronisation
    call('{}/utils/pid_change.sh {}'.format(os.environ['SVJ_TOP_DIR'], in_lhe), shell=True)

    # Split the LHE file, the output files being stored in the current directory
    print(Fore.CYAN + "Splitting LHE file...")
    splitLHE(inputFile=in_lhe, outFileNameBase=model_name+'_split', numFiles=n_jobs)
    os.remove(in_lhe)

    # Copy the split LHE files to directory specified by user
    if not os.path.exists(out_split_lhe):
        os.mkdir(out_split_lhe)
    for split_file in glob.glob(os.path.join(os.getcwd(), model_name+'_split*.lhe')):
        shutil.copy(split_file, out_split_lhe)
        os.remove(split_file)
    print(Fore.MAGENTA + "Split LHE files moved to {}".format(out_split_lhe))


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("config", type=str, help="Path to YAML config to parse")
    args = parser.parse_args()

    main(args.config)
    sys.exit("Done")
