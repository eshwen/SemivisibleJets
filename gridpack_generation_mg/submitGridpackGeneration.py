#!/usr/bin/env python2
""" Handle the input and parsing from a YAML config file for submitGridpackGeneration.sh.
Copy the MadGraph model files to a new directory and change parameters according to the config. """
from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys
try:
    from check_config import basic_checks
except ImportError:
    sys.exit('Please source the setup script first.')
from colorama import Fore, init
import glob
from lhaIDs import lhaIDs as lhaID_dict
from load_yaml_config import load_yaml_config
import os
import re
import shutil
from string import Template
from subprocess import call

# Reset text colours after colourful print statements
init(autoreset=True)


def main(config, resub=False, mode='batch'):
    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = load_yaml_config(config)

    # Set variables from config file
    process_type = input_params['process_type']
    m_med = input_params['m_med']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    m_d = input_params['m_d']
    r_inv = input_params['r_inv']
    alpha_d = input_params['alpha_d']
    year = input_params['year']

    # Check arguments in config file
    basic_checks(input_params)

    # Set process-specific variables
    if 's-channel' in process_type:
        med_type = 'Zp'
        model_prefix = 'SVJ_s'
        template_prefix = 'DMsimp_SVJ_s_spin1'
    elif 't-channel' in process_type:
        med_type = 'Phi'
        model_prefix = 'SVJ_t'
        template_prefix = 'DMsimp_SVJ_t'

    default_model_dir = os.path.join(os.environ['SVJ_MODELS_DIR'], template_prefix+'_editTemplate')
    model_name = '{prefix}_{year}_m{med}-{m_med}_mDQ-{m_d}_rinv-{rinv}_aD-{alphad}'.format(
        rinv=str(r_inv).replace('.', 'p'), alphad=str(alpha_d).replace('.', 'p'),  # MadGraph doesn't like '.' in the model name
        prefix=model_prefix, med=med_type, **input_params)
    total_events = n_events * n_jobs

    # Remove failed gridpack for model if resubmitted
    if resub:
        print(Fore.CYAN + "Removing failed gridpack and resubmitting...")
        for file in glob.glob(os.path.join(os.environ['MG_GENPROD_DIR'], model_name+'*')):
            try:
                if os.path.isfile(file):
                    os.remove(file)
                elif os.path.isdir(file):
                    shutil.rmtree(file)
            except OSError as e:
                print("Error: {0} - {1}.".format(e.filename, e.strerror))

    # If required, append config file with new parameters for simplicity in future steps
    with open(config, 'r+') as f:
        print(Fore.CYAN + "Updating config file with new parameters...")
        original_str = f.readlines()
        # Delete contents of file and update
        f.seek(0)
        f.truncate()
        # Strip model name and total events if they've changed since last use of config, and also blank lines
        for line in original_str:
            if any(line.startswith(x) for x in ['model_name:', 'total_events:', '\n']):
                continue
            else:
                f.write(line)
        # Write new parameters at the end of the file
        f.write("\nmodel_name: {}\ntotal_events: {}\n".format(model_name, total_events))

    new_model_dir = os.path.join(os.environ['SVJ_MODELS_DIR'], model_name)
    if os.path.exists(new_model_dir):
        print("Model of type {} with parameters m_med = {}, m_d = {} already exists!".format(process_type, m_med, m_d))
    else:
        # Copy model files to new directory and change relevant parameters according to config
        print(Fore.CYAN + "Copying template model...")
        shutil.copytree(default_model_dir, new_model_dir)
        # Read the parameters file (containing the dark particle masses) in the new model directory
        with open(os.path.join(new_model_dir, 'parameters.py'), 'r+') as f:
            old_params = Template(f.read())
            # Fill placeholders with values chosen by user
            new_params = old_params.substitute(dark_quark_mass=str(m_d), mediator_mass=str(m_med))
            f.seek(0)
            f.truncate()
            f.write(new_params)
        print(Fore.MAGENTA + "New parameters written in model files!")

    # Write param_card text file
    call('python {}'.format(os.path.join(new_model_dir, 'write_param_card.py')), shell=True)

    input_cards_dir = os.path.join(os.environ['SVJ_MG_INPUT_DIR'], model_name+"_input")
    # Create directory to store input cards and model files for MadGraph
    if not os.path.exists(input_cards_dir):
        os.mkdir(input_cards_dir)
    else:
        print("Directory containing MadGraph input cards exists! No need to create it.")
        # Remove previous input cards in case, e.g., n_events has changed
        for old_file in glob.glob(os.path.join(input_cards_dir, '*.dat')):
            os.remove(old_file)

    # Copy MadGraph input files from template card directory
    # Even if input_cards_dir existed before, copy the template files over in case parameters have changed
    for in_file in glob.glob(os.path.join(os.environ['SVJ_MG_INPUT_DIR'], template_prefix+'_input_template/*.dat')):
        # Get the suffix of the template card for specifying the basename in the dest. path
        card_type = re.search("(?<={0})(\w+).dat".format(template_prefix), in_file).group(0)
        shutil.copy(in_file, os.path.join(input_cards_dir, model_name+card_type))

    # In input files, fill replacement fields with values chosen by user
    for modelFile in glob.glob(os.path.join(input_cards_dir, '*.dat')):
        with open(modelFile, 'r+') as mg_card:
            old_params = mg_card.read()
            # Make sure there are no curly braces in the input cards except those containing the replacement fields
            new_params = old_params.format(modelName=model_name, totalEvents=total_events, lhaid=lhaID_dict[year])
            mg_card.seek(0)
            mg_card.truncate()
            mg_card.write(new_params)
        print(Fore.MAGENTA + "Parameters written for input card", os.path.basename(modelFile))

    # Zip up model directory, specifying basedir to zip enclosing folder, not just files
    shutil.make_archive(os.path.join(input_cards_dir, model_name), 'tar', os.environ['SVJ_MODELS_DIR'], model_name)
    print(Fore.MAGENTA + "Copied model files to input directory!")

    # Require relative path between MG input files and genproductions' gridpack generation script
    rel_cards_dir = os.path.relpath(input_cards_dir, os.environ['MG_GENPROD_DIR'])

    # Run the gridpack generation
    call("{}/runGridpackGeneration.sh {} {} {}".format(os.path.dirname(os.path.realpath(__file__)), model_name, rel_cards_dir, mode), shell=True)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("config", type=str, help="Path to YAML config to parse")
    parser.add_argument('-r', '--resub', action="store_true", help="Retry if previous attempt failed")
    parser.add_argument('-m', '--mode', type=str, choices=['local', 'batch'], default="batch", help="Mode to submit jobs for gridpack generation")
    args = parser.parse_args()

    main(args.config, resub=args.resub, mode=args.mode)
    sys.exit("Done")
