import argparse
import glob
import os
import pprint
import random
import re
import shutil
from splitLHE import splitLHE
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

    model_name = input_params['model_name']
    total_events = input_params['total_events']
    n_jobs = input_params['n_jobs']
    split_lhe_file_path = input_params['lhe_file_path']

    # Set up some path variables for use later
    svj_top_dir = os.environ['SVJ_TOP_DIR']
    genprod_dir = os.environ['MG_GENPROD_DIR']
    default_gridpack_dir = os.path.join(genprod_dir, model_name)
    lhe_gen_dir = os.path.join(default_gridpack_dir, model_name+'_gridpack', 'work', 'gridpack')

    # Get cross section from gridpack generation log file
    log_file = open(os.path.join(lhe_gen_dir, 'gridpack_generation.log'), 'r')
    log_str = log_file.read()
    x_sec = re.search("(?<=Cross-section :   )(\d*.\d+)", log_str).group(0)
    log_file.close()

    # Append cross section to config file if not included already
    config_read = open(args.config, 'r')
    config_orig_str = config_read.read()
    config_read.close()
    if str(x_sec) in config_orig_str:
        print "No need to append config file with new cross section!"
    else:
        print "Appending config file with cross section as calculated by MadGraph..."
        config_append = open(args.config, 'r+')
        original_str = config_append.readlines()
        config_append.seek(0)
        config_append.truncate()

        for i in xrange( len(original_str) ):
            if 'x_sec' in original_str[i]:
                continue
            else:
                config_append.write(original_str[i])

        config_append.write("x_sec: {0}\n".format(x_sec))
        config_append.close()


    # Copy gridpack tarball to gridpacks/
    for tarball in glob.glob( os.path.join(genprod_dir, model_name+'*.xz') ):
        print "Copying {0} to gridpacks/".format( os.path.basename(tarball) )
        shutil.copyfile( tarball, os.path.join(svj_top_dir, 'gridpacks', os.path.basename(tarball)) )
        os.remove(tarball)
        

    # Run the script produced with the gridpack to get the LHE file out and copy to gridpacks/ dir
    random_seed = random.randint(0, 1000000)
    call("cd {0}; ./runcmsgrid.sh {1} {2}".format(lhe_gen_dir, total_events, random_seed), shell = True)

    lhe_output_path = os.path.join(svj_top_dir, 'gridpacks', model_name+'_LHE.lhe')
    shutil.copyfile( os.path.join(lhe_gen_dir, 'cmsgrid_final.lhe'), lhe_output_path )

    # Delete untarred gridpack as it takes up unnecessary space
    shutil.rmtree(default_gridpack_dir)
    print "Removed untarred version of gridpack!"


    # Split the LHE file, the output files being stored in the current directory
    print "Splitting LHE file..."
    splitLHE(inputFile=lhe_output_path, outFileNameBase=model_name+'_split', numFiles=n_jobs)
    os.remove(lhe_output_path)

    # Copy the split LHE files to directory specified by user
    if not os.path.exists(split_lhe_file_path):
        os.mkdir(split_lhe_file_path)
    for splitFile in glob.glob( os.path.join(os.getcwd(), model_name+'_split*.lhe') ):
        shutil.copy(splitFile, split_lhe_file_path)
        os.remove(splitFile)
    print "Split LHE files copied to", split_lhe_file_path



if __name__ == '__main__':
    main()

