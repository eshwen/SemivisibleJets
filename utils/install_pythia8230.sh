#!/bin/bash -e

# this script follows:
# https://github.com/cms-sw/cmsdist/blob/IB/CMSSW_7_1_X/stable/pythia8.spec
# https://github.com/cms-sw/cmsdist/blob/IB/CMSSW_7_1_X/stable/pythia8-toolfile.spec

# environment check
if [ -z "$CMSSW_BASE" ]; then
    echo "you need to run \cmsenv\""
    exit 1
fi  

cd ${CMSSW_BASE}

# some really bad ways to get info out of scram
HEPMC_BASE=$(scram tool info hepmc | grep "HEPMC_BASE" | sed 's/HEPMC_BASE=//')
BOOST_BASE=$(scram tool info boost | grep "BOOST_BASE" | sed 's/BOOST_BASE=//')
LHAPDF_BASE=$(scram tool info lhapdf | grep "LHAPDF_BASE" | sed 's/LHAPDF_BASE=//')

# get pythia8 source and compile
git clone git@github.com:cms-externals/pythia8 -b "cms/230"
cd pythia8
# configure for c++11
./configure --enable-shared --with-boost=${BOOST_BASE} --with-hepmc2=${HEPMC_BASE} --with-lhapdf6=${LHAPDF_BASE} --with-lhapdf6-plugin=LHAPDF6.h --cxx-common="-std=c++11 -fPIC"
make -j 8
make install

# create xml for tool
cd $CMSSW_BASE
cat << 'EOF_TOOLFILE' > pythia8.xml
<tool name="pythia8" version="230">
  <lib name="pythia8"/>
  <client>
    <environment name="PYTHIA8_BASE" default="$CMSSW_BASE/pythia8"/>
    <environment name="LIBDIR" default="$PYTHIA8_BASE/lib"/>
    <environment name="INCLUDE" default="$PYTHIA8_BASE/include"/>
  </client>
  <runtime name="PYTHIA8DATA" value="$PYTHIA8_BASE/share/Pythia8/xmldoc"/>
  <use name="hepmc"/>
  <use name="lhapdf"/>
</tool>
EOF_TOOLFILE

# install tool in scram
cp ${CMSSW_BASE}/pythia8.xml ${CMSSW_BASE}/config/toolbox/${SCRAM_ARCH}/tools/selected
scram setup pythia8

# test success of installation
TEST=`scram tool list | grep pythia8 | wc -l`

if [ "$TEST" -eq "0" ]; then
    echo "pythia8 was not successfully installed :-("
    exit 1
fi

echo "You can now link to the pythia8 libraries through scram!"

# better to use 'scram b checkdeps' but this is not available in 71X
scram b echo_pythia8_USED_BY | tr ' ' '\n' | grep "self" | cut -d'/' -f2-3 | sort -u > pkgs.txt
# update CMSSW dependencies
cd $CMSSW_BASE/src
eval `scramv1 runtime -sh`
git cms-addpkg -f ../pkgs.txt
scram b -j 8
