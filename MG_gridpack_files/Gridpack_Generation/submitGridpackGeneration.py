import argparse
import glob
import os
import pprint
import shutil
from string import replace, Template
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

    print "The arguments you have set are the following:\n", pprint.pprint(input_params)

    # Tidy this in a loop?
    work_space = input_params['work_space']
    process_type = input_params['process_type']
    m_med = input_params['m_med']
    n_events = input_params['n_events']
    n_jobs = input_params['n_jobs']
    m_d = input_params['m_d']

    # Checking arguments in config file
    if not all (type(i) is int for i in [n_events, n_jobs]):
        raise TypeError('n_events and n_jobs are all required to be integers.')
    if m_d < 0 or m_med < 0:
        raise ValueError('m_d must be positive.')
    if m_med < 2*m_d:
        raise ValueError('m_med must be greater than 2*m_d for on-shell pair production of the dark quarks.')
    if 's-channel' in process_type:
        med_type = 'Zp'
        model_prefix = 'DMsimp_SVJ_s_spin1'
        default_model_dir = os.path.join( os.environ['SVJ_MODELS_DIR'], 'DMsimp_SVJ_s_spin1_editTemplate')
    elif 't-channel' in process_type:
        med_type = 'Phi'
        model_prefix = 'DMsimp_SVJ_t'
        default_model_dir = os.path.join( os.environ['SVJ_MODELS_DIR'], 'DMsimp_SVJ_t_editTemplate')
    else:
        raise ValueError('Unknown process_type specified. Please either specify \'s-channel\' or \'t-channel\'.')

    model_name = model_prefix + '_m' + med_type + '-' + str(m_med) + '_mDQ-' + str(m_d)
    total_events = n_events * n_jobs

    # Copy model files to new directory and change relevant parameters according to config
    new_model_dir = os.path.join(os.environ['SVJ_MODELS_DIR'], model_name)

    if os.path.exists(new_model_dir):
        print "Model of type {0} with parameters m_med = {1}, m_d = {2} already exists! No need to create it.".format(process_type, m_med, m_d)
    else:
        print "Copying template model..."
        shutil.copytree(default_model_dir, new_model_dir)
        # Read the parameters file (containing the dark particle masses) in the new model directory
        paramsFile = open( os.path.join(new_model_dir, 'parameters.py'), 'r+')
        oldParamsStr = Template( paramsFile.read() )
        # Replace all instances of $dark_quark_mass and $mediator_mass in parameters file with those chosen by user
        newStr = oldParamsStr.substitute(dark_quark_mass = str(m_d), mediator_mass = str(m_med))
        paramsFile.write(newStr)
        paramsFile.close()
        print "New parameters written in model files!"


    input_cards_dir = os.path.join( os.environ['SVJ_GRIDPACK_DIR'], model_name+"_input" )
    # Create directory to store input cards and model files for MadGraph
    if not os.path.exists(input_cards_dir):
        os.mkdir(input_cards_dir)
    else:
        print "Directory containing MadGraph input cards exists! No need to create it."
        # Remove previous input cards in case, e.g., n_events has changed
        for oldFile in glob.glob( os.path.join(input_cards_dir, '*.dat') ):
            os.remove(oldFile)


    # Copy template files from template card directory and replace placeholders with values chosen by user
    # Even if input_cards_dir existed before, copy the template files over in case number of events has changed
    for inFile in glob.glob( os.path.join(os.environ['SVJ_GRIDPACK_DIR'], model_prefix+'_input_template/*.dat') ):
        shutil.copy(inFile, input_cards_dir)
    
    for modelFile in glob.glob( os.path.join(input_cards_dir, '*.dat') ):
        card = open(modelFile, 'r+')
        oldStr = card.read()
        # Make sure there are no curly braces in the input cards except those containing the placeholders
        newStr = oldStr.format(modelName = model_name, totalEvents = str(total_events)) 
        card.write(newStr)
        card.close()
        print "Parameters written for input card", os.path.basename(modelFile)

    # Zip up model directory
    shutil.make_archive(os.path.join(input_cards_dir, model_name), 'tar', new_model_dir)

    # NOW, I CAN DO SUBPROCESS.CALL(BASH_SCRIPT) TO RUN THE ACTUAL GRIDPACK GENERATION
    

    # Run the gridpack generation
#    call( "./submitGridpackGeneration.sh {0}".format( ), shell = True)


if __name__ == '__main__':
    main()

