from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

# Top level output directory
config.General.workArea = 'DMsimp_SVJ_t'
# Directory below top level output directory
config.General.requestName = 'CRAB_SVJ_LHE_test1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
# Name of the CMSSW configutation file
config.JobType.psetName = 'DMsimp_SVJ_t_MadGraph_NNPDF_13TeV_LHE.py'

# This string determines the primary dataset of the newly-produced output
config.Data.outputPrimaryDataset = 'DMsimp_SVJ_t_MadGraph_NNPDF'
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 50000 # Number of events per job (LHE must have 1 job due to RNG)
config.Data.totalUnits = 50000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC_generation_test1'

# Site the output files will be transmitted to
config.Site.whitelist = ['T2_UK_SGrid_Bristol', 'T2_CH_CERN']
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
