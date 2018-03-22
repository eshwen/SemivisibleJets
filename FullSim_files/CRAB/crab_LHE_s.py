from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

# Top level output directory
config.General.workArea = 'DMsimp_SVJ_s'
# Directory below top level output directory
config.General.requestName = 'CRAB_SVJ_LHE_test1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
# Name of the CMSSW configutation file
config.JobType.psetName = 'DMsimp_SVJ_s_MadGraph_NNPDF_13TeV_LHE.py'
# Path to the gridpack (directory must have public read permissions)
#config.JobType.inputFiles = ['/afs/cern.ch/work/e/ebhal/Semi_visible_jets_CRAB_TEST/CMSSW_7_1_30/src/DMsimp_SVJ_s_spin1_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz']

config.JobType.inputFiles = ['/afs/cern.ch/work/e/ebhal/public/DMsimp_SVJ_s_spin1_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz']

# This string determines the primary dataset of the newly-produced output
config.Data.outputPrimaryDataset = 'DMsimp_SVJ_s_spin1_MadGraph_NNPDF'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 20000 # Number of events per job (LHE must have 1 job due to RNG)
config.Data.totalUnits = 20000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_MC_generation_test1'

# Site the output files will be transmitted to
config.Site.whitelist = ['T2_UK_SGrid_Bristol', 'T2_CH_CERN']
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
