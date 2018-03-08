# Semi-visible Jets

[![arXiv](https://img.shields.io/badge/arXiv-1707.05326%20-green.svg)](https://arxiv.org/abs/1707.05326)

This repository contains model files necessary for generation of semi-visible jet Monte Carlo signal events in `MadGraph`. It also includes instructions of how to generate gridpacks for production with these models, and how to run them through the FullSim CMSSW chain to create nanoAOD files for analysis. Please see [1707.05326](https://arxiv.org/abs/1707.05326) and [1503.00009](https://arxiv.org/abs/1503.00009) for
for further details. Please note that a recent version of `PYTHIA` (> 8.226) including the Hidden Valley module 
and running of the dark coupling is required when implementing the subsequent dark hadronization.

UFO files associated with two UV completions are provided (under [MG_models/](MG_models/)):

## s-channel production

An s-channel production ([DMsimp_SVJ_s_spin1](MG_models/DMsimp_SVJ_s_spin1)) mediated through a new heavy Z'. The model provided is a modified version of the spin-1 `DMsimp` model (http://feynrules.irmp.ucl.ac.be/wiki/DMsimp) 
implemented through `FeynRules`.

## t-channel production

A t-channel production ([DMsimp_SVJ_t](MG_models/DMsimp_SVJ_t)) where the dark and visible sectors interact through a new scalar bi-fundamental.

The bi-fundamentals are denoted with `su11, su12, su21, su22...`, where `u` etc explicitly specifies the QCD flavour index 
and the numbers are the explicit dark non-Abelian group indices. Similarly, the dark quarks are labeled as `qv11, qv12, qv21, qv22`.

Please note that a modified version of `MadGraph` using the patch included [here](https://bugs.launchpad.net/mg5amcnlo/+bug/1702712) 
is required to ensure a stable cross section for event generation using this model.

A `FeynRules` model file ([DMsimp_tchannel.fr](MG_models/DMsimp_SVJ_t/DMsimp_tchannel.fr)) as well as the `Mathematica` notebook ([DMsimp_tchannel.nb](MG_models/DMsimp_SVJ_t/DMsimp_tchannel.nb)) used to generated the UFO output 
are also provided.

## LHE production with `MadGraph` (interactive)

Make a directory to store the programs and output. Then, clone the semi-visible jets files required with

```bash
git clone git@github.com:eshwen/SemivisibleJets.git
```

Download a recent release of `MadGraph` with

```bash
wget https://launchpad.net/mg5amcnlo/2.0/2.6.x/+download/MG5_aMC_v2.6.1.tar.gz
```

Unzip the tar ball with

```bash
tar -xvzf MG5_aMC_v2.6.1.tar.gz
```

In the folder created, the run command is `./bin/mg5_aMC`. Copy the model files from [here](MG_models/SemivisibleJets) into `models/` with

```bash
cp -r ../SemivisibleJets/MG_models/DMsimp_* ./models/
```

The input cards for the s- and t-channel processes are specified in [MG_input/](MG_input/). In these files, the number of events, output directory, as well as other parameters, can be changed.

Run one of the configs with

```bash
./bin/mg5_aMC ../SemivisibleJets/MG_input/<file>
```

This will create lots of output files in the directory specified by the config. The LHE file will be zipped in `<Output dir>/Events/run_01/`, which you can unzip with

```bash
gunzip <file>
```

Other information like the cross section and Feynman diagrams can also be viewed.

_N.B._: MadGraph can be a bit erratic and sometimes fail at the "Working on SubProcesses" stage. Just delete the output directory and try again.

## Generating `MadGraph` gridpacks

For central production, gridpacks will be needed as external LHE generators don't cooperate with CMSSW. These gridpacks are made on the grid, with monitoring output such that it looks like you're running locally.

First, clone this repo with

```bash
git clone git@github.com:eshwen/SemivisibleJets.git
```

All the necessary files for spin1-s- and t-channel production are in [MG_gridpack_files/](MG_gridpack_files/), and a tutorial can be found at https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO. More models can be added if needed, but it is cumbersome. The file names need to be specific, with the same prefix of `<model name>` and have the suffixes as shown in the existing models (e.g., `<model name>_proc_card.dat`). If adding models, use the existing files as templates. The model files also need to be zipped with

```bash
tar -cf <output file name>.tar <input file(s)>
```

and be copied to the generator web repository on `/afs/cern.ch/cms/generators/www/`. Note that you will need to contact Cms.Computing@cern.ch and cms.generators@cern.ch to request write access to the directory. Though, you will have read access by default.

Once the models are in place and the input cards have been written, clone the `genproductions` repo somewhere with a lot of storage. The gridpacks end up in directories within the repository, and so its size can grow considerably. Clone my fork of the repo (which includes some minor fixes for bugs I was receiving) with

```bash
git clone git@github.com:eshwen/genproductions.git genproductions -b mg26x
```

The branch specified above is necessary to run MadGraph version 2.6.x, with some slight bug fixes present in the fork.

Validate the input cards you have with

```bash
cd genproductions/bin/MadGraph5_aMCatNLO/Utilities/parsing_code
python parsing.py <path to process card directory/name of process card without _proc_card.dat>
```

Once validated, run the gridpack generation with

```bash
cd genproductions/bin/MadGraph5_aMCatNLO/
./gridpack_generation.sh <name of process card without _proc_card.dat> <relative path to cards directory> <queue selection>
```

where `<queue selection>` options can be found by typing `bqueues`. If instead, you would like to run on Condor (either at lxplus or at a T2/T3 site), run

```bash
cd genproductions/bin/MadGraph5_aMCatNLO/
./submit_condor_gridpack_generation.sh <name of process card without _proc_card.dat> <relative path to cards directory> 
```

Note that the architecture, and CMSSW and MadGraph versions are all hardcoded into `gridpack_generation.sh`. They be changed either from within, or with command-line arguments (which only work for arch and CMSSW versions). As with interactive running, MadGraph can be unruly on the "Working on Subprocesses" bit. Just kill and resubmit if that's the case.

Your grid certificate may also be required to run. To initialise a proxy that lasts a week, type

```bash
voms-proxy-init --voms cms --valid 168:00
```

Once completed, the gridpack (in a .tar.xz file) will be located in the current directory. An untarred version is also available for viewing and validation. Just repeat the procedure for other parameters and models.

## Hadronisation with `PYTHIA` and detector simulation with `Delphes` (interactive)

As noted above, a recent version of `PYTHIA` (> 8.226) including the Hidden Valley (HV) module and running of the dark coupling is required when implementing the subsequent dark hadronisation.

In order to be able to use the HV module, the PDG IDs of the dark particles must be changed in the LHE files for `PYTHIA` to be able to recognize and shower these properly (see http://home.thep.lu.se/Pythia/pythia82html/HiddenValleyProcesses.html). This can be done as follows:

- For the s-channel model
```bash
sed -i 's/5000521/4900101/g' <LHE filename>
```
- For the t-channel model
```bash
sed -i 's/49001010/4900101/g' <LHE filename>	
sed -i 's/49001011/4900101/g' <LHE filename>	
sed -i 's/49001012/4900101/g' <LHE filename>	
sed -i 's/49001013/4900101/g' <LHE filename>	
sed -i 's/49001014/4900101/g' <LHE filename>	
```
or
```bash
./tChannelPIDChange.sh <LHE filename>
```

Once the PIDs have been changed, it is possible to run `PYTHIA` and `Delphes` concurrently on the LHE file. See the README in https://github.com/eshwen/mc-production/tree/master/run_delphes for the installation commands and how to run everything. On subsequent sessions, you can just `source delphes_pythia8_setup.sh` in that directory to set up the environment.

## Running the FullSim CMSSW chain for hadronisation with `PYTHIA` and detector simulation with `GEANT4`

The PID change, as noted above, is only necessary when running on interactively-generated LHE files from MadGraph. When generating the gridpacks, I have already included a fix so that once the LHEs are created from the gridpack in CMSSW, the PIDs are changed before hadronisation with Pythia.

Now, to run the full chain, one has to first specify a "GEN fragment", telling CMSSW about the external generator we have used and how to hadronise the particles. The GEN fragment I used can be found in [SVJ_MadGraph_LHAPDF_13TeV_s_channel_spin1_GEN_frag.py](FullSim_files/SVJ_MadGraph_LHAPDF_13TeV_s_channel_spin1_GEN_frag.py). As `MadGraph` was used as the external generator, the `externalLHEProducer` information needs to be included, telling CMSSW where the gridpack is located as well as how many events are in there and the output LHE file (which _should not_ be changed). All the code in the fragment and commands below are specific to emulating 2016 data taking, and `cmsDriver` commands can be changed depending on the context in which you would like to generate samples. Note that you may also have to regenerate the gridpacks with different Parton Distribution Functions to simulate different years. It should be detailed in the quick start guide linked above.

### Gridpack to LHE-GEN-SIM

This requires CMSSW\_7\_1\_30 as it contains `PYTHIA` 8.226, which contains the Hidden Valley module. It can be initialised with

```bash
ource /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
cmsrel CMSSW_7_1_30
cd CMSSW_7_1_30/src
cmsenv
mkdir -p Configuration/GenProduction/python
cp <GEN fragment> Configuration/GenProduction/python/
scram b
cmsenv
```

and then the `cmsDriver` command is

```bash
cmsDriver.py Configuration/GenProduction/python/SVJ_MadGraph_LHAPDF_13TeV_s_channel_spin1_GEN_frag.py --fileout file:SVJ_s_LHE_GEN_SIM.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename SVJ_s_LHE_GEN_SIM.py --no_exec -n 250
```

Once a config has been created, it can be run with `cmsRun`:

```bash
cmsRun SVJ_s_LHE_GEN_SIM.py -n <no. threads>
```

This should give an output root file, which is needed for the next step.

### GEN-SIM to AOD (step 1)

This requires a different CMSSW version as the GEN-SIM files are being emulated for the 2016 year of data taking.

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_8_0_21
cd CMSSW_8_0_21/src
cmsenv
cp <path>/SVJ_s_LHE_GEN_SIM.root .
scram b
cmsenv
voms-proxy-init --voms cms --valid 168:00 # for querying PU dataset
```

From this point, the only input needed by `cmsDriver` is the output root file from the previous step. For the first AOD step, pileup mixing is performed and is required for accurate replication of the conditions for the year of data taking being emulated. However, querying the entire dataset below is unfeasible (as it's 500 TB and 125k files large), so I only used one file. In practice, this, or a smaller dataset are usually fine. One thing to note is, past this point, if your files contain very few events (< 10), specifying a specific number of threads in `cmsRun` can cause failures so it's usually best to leave that option blank. The config for this stage can be made with

```bash
cmsDriver.py step1 --filein file:SVJ_s_LHE_GEN_SIM.root --fileout file:SVJ_s_AOD_step1.root --pileup_input /store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/100000/001EB167-3781-E611-BE3C-0CC47A4D75F4.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --datamix PreMix --era Run2_2016 --python_filename SVJ_s_AOD_step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 250
```

and run with

```bash
cmsRun SVJ_s_AOD_step1.py -n 8
```

### AOD (step 1) to AOD (step 2)

This is done with the same CMSSW and in the same environment as the previous step. The config is created with

```bash
cmsDriver.py step2 --filein file:SVJ_s_AOD_step1.root --fileout file:SVJ_s_AOD_step2.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --era Run2_2016 --python_filename SVJ_s_AOD_step2.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 250
```

and run with

```bash
cmsRun SVJ_s_AOD_step2.py -n 8
```

### AOD (step 2) to miniAOD

This is done with the same CMSSW and in the same environment as the previous step. The config is created with

```bash
cmsDriver.py --filein file:SVJ_s_AOD_step2.root --fileout file:SVJ_s_MINIAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --era Run2_2016 --python_filename SVJ_s_MINIAOD.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 250
```

and run with

```bash
cmsRun SVJ_s_MINIAOD.py
```

### miniAOD to nanoAOD

This is a relatively new step in the CMSSW chain. NanoAODs are supposed to resemble Heppy flat trees, which makes them easy to read, and only require an extra command from `cmsDriver.py` and `cmsRun`. But as backward and forward compatibility between CMSSW releases can be an issue, a newer version that supports nanoAOD creation is needed:

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_9_4_4
cd CMSSW_9_4_4/src
cmsenv
cp <path>/SVJ_s_MINIAOD.root .
scram b
cmsenv
```

Then, the `cmsDriver` command is

```bash
cmsDriver.py --filein file:SVJ_s_MINIAOD.root --fileout file:SVJ_s_NANOAOD.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:run2_mc -s NANO --era Run2_2016,run2_miniAOD_80XLegacy --python_filename SVJ_s_NANOAOD.py --no_exec -n 250
```

which is run with

```bash
cmsRun SVJ_s_NANOAOD.py -n 8
```

A nanoAOD file should be produced, and inspection should reveal several trees. The only interesting one is called "Events", which should contain easy-to-read branches. This, in turn, makes it an easier object to analyse.

## Contact

For questions or issues please contact:

-  Tim Lou; hlou@berkeley.edu
-  Siddharth Mishra-Sharma; smsharma@princeton.edu
-  Eshwen Bhal (for implementation, not theory); eshwen.bhal@cern.ch

## To do

- Add grid support for running CMSSW chain
- Make a pileup filelist like in SVJ_production, specifying a few files from the Neutrino Gun dataset.