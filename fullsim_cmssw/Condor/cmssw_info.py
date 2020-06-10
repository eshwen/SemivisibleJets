from __future__ import print_function
import os
from subprocess import call
import sys

this_dir = os.path.dirname(os.path.realpath(__file__))
this_sys = os.environ['SCRAM_ARCH']


class CmsswInfo(object):
    """ Store CMSSW information (i.e., version and architecture) for different years """
    def __init__(self, year):
        self.year = year

        if self.year == 2016:
            self.gensim = {'version': 'CMSSW_7_1_38_patch1', 'arch': 'slc6_amd64_gcc481'}  # earlier versions don't have CMSSW plug-ins for dark quark/Z2 filters
            self.aod = {'version': 'CMSSW_8_0_31', 'arch': 'slc6_amd64_gcc530'}
            self.nano = {'version': 'CMSSW_9_4_4', 'arch': 'slc6_amd64_gcc630'}
            self.new_pythia = True  # CMSSW_7_1_38_patch1 ships with old Pythia version

        elif self.year == 2017:
            self.gensim = {'version': 'CMSSW_9_3_15', 'arch': 'slc7_amd64_gcc630'}  # earlier versions (at least <=9_3_12) don't have CMSSW plug-ins for dark quark/Z2 filters
            self.aod = {'version': 'CMSSW_9_4_10', 'arch': 'slc7_amd64_gcc630'}
            self.nano = {'version': 'CMSSW_10_2_15', 'arch': 'slc7_amd64_gcc700'}
            self.new_pythia = False  # CMSSW_9_3_15 already ships with Pythia 8.230

        elif self.year == 2018:
            self.gensim = {'version': 'CMSSW_10_2_15', 'arch': 'slc7_amd64_gcc700'}  # earlier versions (at least <=10_2_3) don't have CMSSW plug-ins for dark quark/Z2 filters
            self.aod = {'version': 'CMSSW_10_2_15', 'arch': 'slc7_amd64_gcc700'}
            self.nano = {'version': 'CMSSW_10_2_15', 'arch': 'slc7_amd64_gcc700'}
            self.new_pythia = False  # CMSSW_10_2_15 already ships with Pythia 8.230

        else:
            sys.exit("Only years 2016, 2017, and 2018 are supported")

        self.stages = [self.gensim, self.aod, self.nano]

    def initialise_envs(self, location):
        """ Initialise CMSSW environments """
        for stage in self.stages:
            if os.path.exists(os.path.join(location, stage['version'], 'src')):
                print("{} release already exists!".format(stage['version']))
            else:
                _command = '{}/sourceCMSSW.sh {} {} {}'.format(this_dir, stage['version'], stage['arch'], location)
                run_in_slc6_env(_command, target_arch=stage['arch'])

        # Install new Pythia version if not already done so
        if self.new_pythia:
            _command = '{}/sourceNewPythiaVer.sh {} {} {}'.format(this_dir, location, self.gensim['version'], self.gensim['arch'])
            run_in_slc6_env(_command, target_arch=self.gensim['arch'])

    def compile_env(self, location, version, arch):
        """ Compile CMSSW env """
        _command = '{}/utils/compile_cmssw.sh {} {} {}'.format(os.environ['SVJ_TOP_DIR'], location, version, arch)
        run_in_slc6_env(_command, target_arch=arch)


def run_in_slc6_env(command, target_arch="slc6_amd64_gcc481", current_sys=this_sys, singularity_dir=this_dir):
    """ Call Singularity to set up SLC6 env if required """
    if target_arch.startswith('slc6') and not current_sys.startswith('slc6'):
        call('{}/run_singularity.sh "{}"'.format(singularity_dir, command), shell=True)
    else:
        call(command, shell=True)
