from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

# Not mandatory, just for simplicity in constructing directory/dataset names
modelName = 'DMsimp_SVJ_s_spin1_MadGraph'
datasetStr = 'mZp_1000_md_10_alphaD_0p1_NNPDF30_13TeV-LHE'

# CRAB project directory
config.General.workArea = modelName
# Directory below top level output directory
config.General.requestName = datasetStr
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
# Name of the CMSSW configutation file
config.JobType.psetName = 'DMsimp_SVJ_s_MadGraph_NNPDF_13TeV_LHE.py'
# Path to the gridpack (directory must have public read permissions)
config.JobType.inputFiles = ['/afs/cern.ch/work/e/ebhal/public/DMsimp_SVJ_s_spin1_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz']

# This string determines the primary dataset of the newly-produced output
config.Data.outputPrimaryDataset = datasetStr
#config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 50000 # Number of events per job (LHE must have 1 job due to RNG)
config.Data.totalUnits = 50000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True # If true, output files are published on DBS. Useful for future steps
# Directory below outputPrimaryDataset in output, also directory below workArea in project dir
config.Data.outputDatasetTag = modelName + '_' + datasetStr

config.Site.whitelist = ['T2_UK_SGrid_Bristol', 'T2_CH_CERN'] # CERN site needed so CRAB worker nodes with /afs mounted can be used
config.Site.storageSite = 'T2_UK_SGrid_Bristol' # Site the output files will be transmitted to

