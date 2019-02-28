import argparse
import sys
try:
    from checkConfig import performBasicChecks
except ImportError:
    sys.exit('Please source the setup script first.')
from colorama import Fore, init
import glob
from loadYamlConfig import loadYamlConfig
import os
import re
import shutil
from string import Template
from subprocess import call
import yaml


# Reset text colours after colourful print statements
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("config", type=str, default=os.path.join(os.environ['SVJ_TOP_DIR'], 'config', 'model_params_s_spin1.yaml'), help="Path to YAML config to parse")
parser.add_argument('-r', '--resub', action="store_true", help="Retry if previous attempt failed")
args = parser.parse_args()



def main():
    """
    Handle the input and parsing from a YAML config file for submitGridpackGeneration.sh.
    Copy the MadGraph model files to a new directory and change parameters according to the config.
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = loadYamlConfig(args.config)

    # Set variables from config file
    process_type = input_params['process_type']
    m_med = input_params['m_med']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    m_d = input_params['m_d']
    r_inv = input_params['r_inv']

    # Check arguments in config file
    performBasicChecks(input_params)

    # Set process-specific variables
    if 's-channel' in process_type:
        med_type = 'Zp'
        model_prefix = 'DMsimp_SVJ_s_spin1'
        default_model_dir = os.path.join( os.environ['SVJ_MODELS_DIR'], 'DMsimp_SVJ_s_spin1_editTemplate')
    elif 't-channel' in process_type:
        med_type = 'Phi'
        model_prefix = 'DMsimp_SVJ_t'
        default_model_dir = os.path.join( os.environ['SVJ_MODELS_DIR'], 'DMsimp_SVJ_t_editTemplate')

    model_name = model_prefix + '_m' + med_type + '-' + str(m_med) + '_mDQ-' + str(m_d) + '_rinv-' + str(r_inv).replace('.', 'p')
    total_events = n_events * n_jobs


    # Remove failed gridpack for model if resubmitted
    if args.resub:
        print Fore.CYAN + "Removing failed gridpack and resubmitting..."
        for file in glob.glob( os.path.join(os.environ['MG_GENPROD_DIR'], model_name+'*') ):
            try:
                if os.path.isfile(file):
                    os.remove(file)
                elif os.path.isdir(file):
                    shutil.rmtree(file)
            except OSError as e:
                print "Error: {0} - {1}.".format(e.filename, e.strerror)


    # If required, append config file with new parameters for simplicity in future steps
    read_config_file = open(args.config, 'r')
    config_orig_str = read_config_file.read()
    read_config_file.close()    

    if model_name+'\n' in config_orig_str and str(total_events)+'\n' in config_orig_str:
        print "No need to append config file with new parameters!"
    else:
        print Fore.CYAN + "Appending config file with new parameters..."
        appended_config_file = open(args.config, 'r+')
        original_str = appended_config_file.readlines()
        # Delete contents of file and update
        appended_config_file.seek(0)
        appended_config_file.truncate()        

        # Strip model name and total events if they've changed since last use of config, and also blank lines
        for i in xrange( len(original_str) ):
            if any(x in original_str[i] for x in ['model_name:', 'total_events:', '\n']):
                continue
            else:
                appended_config_file.write(original_str[i])
        # Write new model name and total number of events
        appended_config_file.write( "\nmodel_name: {0}\ntotal_events: {1}\n".format(model_name, total_events) )
        appended_config_file.close()


    new_model_dir = os.path.join(os.environ['SVJ_MODELS_DIR'], model_name)
    if os.path.exists(new_model_dir):
        print "Model of type {0} with parameters m_med = {1}, m_d = {2} already exists! No need to create it.".format(process_type, m_med, m_d)
    else:
        # Copy model files to new directory and change relevant parameters according to config
        print Fore.CYAN + "Copying template model..."
        shutil.copytree(default_model_dir, new_model_dir)
        # Read the parameters file (containing the dark particle masses) in the new model directory
        params_file = open( os.path.join(new_model_dir, 'parameters.py'), 'r+')
        oldStr = Template( params_file.read() )
        # Replace placeholders with those chosen by use
        newStr = oldStr.substitute( dark_quark_mass = str(m_d), mediator_mass = str(m_med) )
        params_file.seek(0)
        params_file.truncate()
        params_file.write(newStr)
        params_file.close()
        print Fore.MAGENTA + "New parameters written in model files!"


    # Write param_card text file
    call('python {}'.format( os.path.join(new_model_dir, 'write_param_card.py') ), shell=True)
    shutil.move( 'param_card.dat', os.path.join(new_model_dir, 'param_card.dat') )


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
    # Even if input_cards_dir existed before, copy the template files over in case parameters have changed
    for inFile in glob.glob( os.path.join(os.environ['SVJ_MG_INPUT_DIR'], model_prefix+'_input_template/*.dat') ):
        # Get the suffix of the template card for specifying the basename in the dest. path
        card_type = re.search("(?<={0})(\w+).dat".format(model_prefix), inFile).group(0)
        shutil.copy(inFile, os.path.join(input_cards_dir, model_name+card_type) )

    # In input files, replace placeholders with values chosen by user
    for modelFile in glob.glob( os.path.join(input_cards_dir, '*.dat') ):
        mg_card = open(modelFile, 'r+')
        oldStr = mg_card.read()
        # Make sure there are no curly braces in the input cards except those containing the placeholders
        newStr = oldStr.format( modelName = model_name, totalEvents = str(total_events) )
        mg_card.seek(0)
        mg_card.truncate()
        mg_card.write(newStr)
        mg_card.close()
        print Fore.MAGENTA + "Parameters written for input card", os.path.basename(modelFile)


    # Zip up model directory, specifying basedir to zip enclosing folder, not just files
    shutil.make_archive(os.path.join(input_cards_dir, model_name), 'tar', os.environ['SVJ_MODELS_DIR'], model_name)
    print Fore.MAGENTA + "Copied model files to input directory!"

    # Require relative path between MG input files and genproductions' gridpack generation script
    rel_cards_dir = os.path.relpath(input_cards_dir, os.environ['MG_GENPROD_DIR'])

    # Run the gridpack generation
    call( "./runGridpackGeneration.sh {0} {1}".format(model_name, rel_cards_dir), shell = True)



if __name__ == '__main__':
    main()

