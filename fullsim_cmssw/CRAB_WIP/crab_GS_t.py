from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

# Not mandatory, just for simplicity in constructing directory/dataset names
modelName = 'DMsimp_SVJ_t_MadGraph'
datasetStr = 'mZp_1000_md_10_alphaD_0p1_NNPDF30_13TeV-GEN-SIM'

# CRAB project directory
config.General.workArea = modelName
# Directory below top level output directory
config.General.requestName = datasetStr
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'DMsimp_SVJ_t_MadGraph_NNPDF_13TeV_GS.py'

config.Data.inputDataset = '/mZp_1000_md_10_alphaD_0p1_NNPDF30_13TeV-LHE/ebhal-DMsimp_SVJ_t_MadGraph_mZp_1000_md_10_alphaD_0p1_NNPDF30_13TeV-LHE-d5245ab584434bea4faa5aea256d691f/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True # If true, output files are published on DBS. Useful for future steps
# Directory below outputPrimaryDataset in output, also directory below workArea in project dir
config.Data.outputDatasetTag = modelName + '_' + datasetStr

config.Site.whitelist = ['T2_UK_SGrid_Bristol', 'T2_CH_CERN'] # CERN site needed so CRAB worker nodes with /afs mounted can be used
config.Site.storageSite = 'T2_UK_SGrid_Bristol' # Site the output files will be transmitted to

