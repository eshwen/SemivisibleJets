import sys

class CmsswInfo(object):
    def __init__(self, year):
        self.year = year

        if self.year == 2016:
            self.init = {'version': 'CMSSW_7_1_38_patch1', 'arch': 'slc6_amd64_gcc481'}  # earlier versions don't have CMSSW plug-ins for dark quark/Z2 filters
            self.aod = {'version': 'CMSSW_8_0_21', 'arch': 'slc6_amd64_gcc530'}
            self.nano = {'version': 'CMSSW_9_4_4', 'arch': 'slc6_amd64_gcc630'}

        elif self.year == 2017:
            self.init = {'version': 'CMSSW_9_3_15', 'arch': 'slc7_amd64_gcc630'}  # earlier versions don't have CMSSW plug-ins for dark quark/Z2 filters
            self.aod = {'version': 'CMSSW_9_4_7', 'arch': 'slc7_amd64_gcc630'}
            self.nano = {'version': 'CMSSW_10_2_15', 'arch': 'slc7_amd64_gcc700'}

        elif self.year == 2018:
            self.init = {'version': 'CMSSW_10_2_3', 'arch': 'slc7_amd64_gcc700'}
            self.aod = {'version': 'CMSSW_10_2_3', 'arch': 'slc7_amd64_gcc700'}
            self.nano = {'version': 'CMSSW_10_2_15', 'arch': 'slc7_amd64_gcc700'}
        else:
            sys.exit("Only years 2016, 2017, and 2018 are supported")
