# Source CMSSW
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
cd ../CMSSW_8_0_26/src
cmsenv
cd ../..

# Compile Delphes
cd Delphes-3.4.1
export PYTHIA8=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/pythia8/212-ikhhed3/
export LD_LIBRARY_PATH=$PYTHIA8/lib:$LD_LIBRARY_PATH
make HAS_PYTHIA8=true DelphesPythia8
cd ..

# Set Delphes environment variables
export DELPHES=$(pwd)/Delphes-3.4.1
export LD_LIBRARY_PATH=${DELPHES}/tmp/modules:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=${DELPHES}/tmp/classes:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=${DELPHES}/tmp/external/ExRootAnalysis:$LD_LIBRARY_PATH
export PATH=${DELPHES}:$PATH
