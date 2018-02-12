#!/usr/bin/env python

import sys, getopt
import os

def main(argv):
        if len(sys.argv)<2:
                print 'run_mg_grid <initial string>'
                sys.exit(2)
        inputfile = sys.argv[1]
        idString = inputfile
        if not os.path.isfile(inputfile):
                print inputfile+" does not exist"
                sys.exit()


        idString = idString.replace('configs/', '')
        idString = idString.replace('.input', '')
        os.system('mkdir -p results/'+idString)
        os.system('cp '+inputfile+' results/'+idString+'/')


	names=[]
	fC = open(inputfile)
        for line in fC:
		line = line.replace("\n", " ")
		if ("output") in line and not ("loop_optimized_output") in line:
			names.append(line.split(' ', 1)[1].strip())
	fC.close()

        f1 = open('templates/template.sh', 'r')  
        f2 = open('results/'+idString+'/'+idString+'.sh', 'w') 
        for line in f1:
                line=line.replace('SAMPLE', idString)
                f2.write(line)
        f1.close()
        f2.close()


        f1 = open('templates/template.submit', 'r')  
        f2 = open('results/'+idString+'/'+idString+'.submit', 'w') 
        for line in f1:
                line=line.replace('SAMPLE', idString)
		if ("transfer_output_files") in line:
			f2.write("transfer_output_files = "+', '.join(names)+'\n')
		else: 
			f2.write(line)
        f1.close()
        f2.close()

        print('cd results/'+idString+'/; condor_submit '+idString+'.submit; cd -')
        os.system('cd results/'+idString+'/; condor_submit '+idString+'.submit; cd -')


if __name__ == "__main__":
        main(sys.argv[1:])
