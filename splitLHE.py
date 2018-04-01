#!/usr/bin/env python2                                                                                                                                                              
import argparse
import re
import sys
from progressbar import ProgressBar, Percentage, Bar, ETA # requires progressbar package from pip

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFile", default = "unweighted_events.lhe", type = str, help = "Input LHE file")
parser.add_argument("-o", "--outFileNameBase", default = "outputFile", type = str, help = "Base name for output files")
parser.add_argument("-n", "--numFiles", default = 100, type = int, help = "Number of files to split input file in to") 

args = parser.parse_args()

def main():
    """
    Splits the LHE file inputFile into numFiles individual files of the form <outFileNameBase>_XXX.lhe
    For numFiles > 1000, the number of open IO files in python will cause the program to exit with an error.
    """

    inputFile = args.inputFile
    outFileNameBase = args.outFileNameBase
    numFiles = args.numFiles

    fin = ""
    try:
        fin = open(inputFile)
    except:
        print( "Error: Input file: {0} could not be opened, exiting.".format(inputFile) )
        sys.exit(1)

    print "Opened input file", inputFile

    eventNum = 0
    init = False
    inFooter = False
    footLines = []

    for line in fin:
        if re.match(r"[^#]*</LesHouchesEvents>",line):
            inFooter = True
            footLines.append(line)
        elif inFooter:
            footLines.append(line)
        elif init:  
            if re.match(r"[^#]*</event>",line):
                eventNum += 1
        elif re.match(r"[^#]*</init>",line):
            init = True

    eventsTotal = eventNum
    print "Total number of events: {0}".format(eventsTotal)

    # Initialise progress bar                                                                                                                                                       
    widgets = [Percentage(), Bar('>'), ETA()]
    pbar = ProgressBar(widgets = widgets, maxval = numFiles).start()

    files = []
    maxEventsFile = []

    for i in range(numFiles):
        splitFileName = outFileNameBase
#        if(i < 100):
#            splitFileName += "0"
#        if(i < 10):
#            splitFileName += "0"

        tmp = open(splitFileName + "_" + str(i) + ".lhe", 'w')
        files.append(tmp)
        maxEventsFile.append(eventsTotal / numFiles)
        pbar.update(i + 1)

    pbar.finish()
    maxEventsFile[len(maxEventsFile) - 1] += eventsTotal % numFiles

    eventNum = 0
    eventNumThisFile = 0
    init = False
    headLines = []
    iFile = 0
    fin.seek(0)

    for line in fin:
        if init:  
            files[iFile].write(line)
            if re.match(r"[^#]*</event>", line):
                eventNum += 1
                eventNumThisFile += 1
                if eventNumThisFile >= maxEventsFile[iFile]:
                    files[iFile].writelines(footLines)
                    iFile += 1
                    eventNumThisFile = 0
                    if iFile == numFiles:
                        break
                    files[iFile].writelines(headLines)
        elif re.match(r"[^#]*</init>",line):
            init = True
            headLines.append(line)
            files[iFile].writelines(headLines)
        else:
            headLines.append(line)

    for f in files:
        f.close()
 

if __name__ == '__main__':
    main()
    sys.exit("Completed")
