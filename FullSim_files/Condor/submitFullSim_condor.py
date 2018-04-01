#!/usr/bin/env python2                                                                                                                                                              
import argparse
from subprocess import call
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--workSpace", default = os.getcwd(), type = str, help = "Working directory to store scripts and output files")
parser.add_argument("-g", "--genFragPath", default = "./GS.py", type = str, help = "Path to gen fragment")
parser.add_argument("-l", "--lheFilePath", default = "./unweighted_events", type = str, help = "The path to the lhe files with a common basename, e.g., for ./unweighted_events_XXX.lhe, give the argument as ./unweighted_events")
parser.add_argument("-m", "--modelName", default = "myModel", type = str, help = "Identifier for model being run")
parser.add_argument("-n", "--nEvents", default = 100, type = int, help = "Number of events per job")
parser.add_argument("-j", "--nJobs", default = 100, type = int, help = "Number of jobs to run. Note, you must have one LHE file available per job")

args = parser.parse_args()

def main():
    """
    Handle the input and parsing for submitFullSim_condor.sh
    """

    call( "./submitFullSim_condor.sh {0} {1} {2} {3} {4} {5}".format(args.workSpace, args.genFragPath, args.lheFilePath, args.modelName, args.nEvents, args.nJobs), shell = True )

if __name__ == '__main__':
    main()
    sys.exit("Completed")
