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


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], "config", "model_params_s_spin1.yaml"), help = "Path to YAML config to parse")
args = parser.parse_args()



def main():
    """
    Handle the input and parsing from a YAML config file for submitGridpackGeneration.sh.
    Copy the MadGraph model files to a new directory and change parameters according to the config.
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    print "Using config file", args.config
    input_params = yaml.load( open(args.config, 'r') )

    print Fore.CYAN + "The arguments you have set are the following:\n", pprint.pprint(input_params)
    print Style.RESET_ALL

    # Set variables from config file
    process_type = input_params['process_type']
    m_med = input_params['m_med']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    m_d = input_params['m_d']
    r_inv = input_params['r_inv']


    # Checking arguments in config file
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


    # Set process-specific variables
    elif 's-channel' in process_type:
        med_type = 'Zp'
        model_prefix = 'DMsimp_SVJ_s_spin1'
        default_model_dir = os.path.join( os.environ['SVJ_MODELS_DIR'], 'DMsimp_SVJ_s_spin1_editTemplate')
    elif 't-channel' in process_type:
        med_type = 'Phi'
        model_prefix = 'DMsimp_SVJ_t'
        default_model_dir = os.path.join( os.environ['SVJ_MODELS_DIR'], 'DMsimp_SVJ_t_editTemplate')

    model_name = model_prefix + '_m' + med_type + '-' + str(m_med) + '_mDQ-' + str(m_d) + '_rinv-' + str(r_inv).replace('.', 'p')
    total_events = n_events * n_jobs


    # If required, append config file with new parameters for simplicity in future steps
    config_read = open(args.config, 'r')
    config_orig_str = config_read.read()
    config_read.close()
    if model_name in config_orig_str and str(total_events) in config_orig_str:
        print "No need to append config file with new parameters!"
    else:
        print "Appending config file with new parameters..."
        config_append = open(args.config, 'r+')
        original_str = config_append.readlines()
        # Delete contents of file and update
        config_append.seek(0)
        config_append.truncate()        

        # Strip model name and total events if they've changed since last use of config
        for i in xrange( len(original_str) ):
            if 'model_name' in original_str[i] or 'total_events' in original_str[i]:
                continue
            else:
                config_append.write(original_str[i])
        # Write new model name and total number of events
        config_append.write("""
model_name: {0}
total_events: {1}
""".format(model_name, total_events)
        )
        config_append.close()


    new_model_dir = os.path.join(os.environ['SVJ_MODELS_DIR'], model_name)
    if os.path.exists(new_model_dir):
        print "Model of type {0} with parameters m_med = {1}, m_d = {2} already exists! No need to create it.".format(process_type, m_med, m_d)
    else:
        # Copy model files to new directory and change relevant parameters according to config
        print "Copying template model..."
        shutil.copytree(default_model_dir, new_model_dir)
        # Read the parameters file (containing the dark particle masses) in the new model directory
        paramsFile = open( os.path.join(new_model_dir, 'parameters.py'), 'r+')
        oldStr = Template( paramsFile.read() )
        # Replace placeholders with those chosen by use
        newStr = oldStr.substitute(dark_quark_mass = str(m_d), mediator_mass = str(m_med))
        paramsFile.seek(0)
        paramsFile.truncate()
        paramsFile.write(newStr)
        paramsFile.close()
        print Fore.MAGENTA + "New parameters written in model files!", Style.RESET_ALL


    input_cards_dir = os.path.join( os.environ['SVJ_MG_INPUT_DIR'], model_name+"_input" )
    # Create directory to store input cards and model files for MadGraph
    if not os.path.exists(input_cards_dir):
        os.mkdir(input_cards_dir)
    else:
        print "Directory containing MadGraph input cards exists! No need to create it."
        # Remove previous input cards in case, e.g., n_events has changed
        for oldFile in glob.glob( os.path.join(input_cards_dir, '*.dat') ):
            os.remove(oldFile)


    # Copy MadGraph input files from template card directory
    # Even if input_cards_dir existed before, copy the template files over in case oarameters have changed
    for inFile in glob.glob( os.path.join(os.environ['SVJ_MG_INPUT_DIR'], model_prefix+'_input_template/*.dat') ):
        # Get the suffix of the template card for specifying the basename in the dest. path
        card_type = re.search("(?<={0})(\w+).dat".format(model_prefix), inFile).group(0)
        shutil.copy(inFile, os.path.join(input_cards_dir, model_name+card_type) )

    # In input files, replace placeholders with values chosen by user
    for modelFile in glob.glob( os.path.join(input_cards_dir, '*.dat') ):
        card = open(modelFile, 'r+')
        oldStr = card.read()
        # Make sure there are no curly braces in the input cards except those containing the placeholders
        newStr = oldStr.format(modelName = model_name, totalEvents = str(total_events)) 
        card.seek(0)
        card.truncate()
        card.write(newStr)
        card.close()
        print Fore.MAGENTA + "Parameters written for input card", os.path.basename(modelFile), Style.RESET_ALL


    # Zip up model directory, specifying basedir to zip enclosing folder, not just files
    shutil.make_archive(os.path.join(input_cards_dir, model_name), 'tar', os.environ['SVJ_MODELS_DIR'], model_name)
    print Fore.MAGENTA + "Copied model files to input directory!", Style.RESET_ALL

    # Require relative path between MG input files and genproductions' gridpack generation script
    rel_cards_dir = os.path.relpath(input_cards_dir, os.environ['MG_GENPROD_DIR'])
    
    # Run the gridpack generation
    call( "./runGridpackGeneration.sh {0} {1}".format(model_name, rel_cards_dir), shell = True)



if __name__ == '__main__':
    main()

