# Table of contents

1. [Introduction](#introduction)
    - [s-channel model](#schannelmodel)
    - [t-channel model](#tchannelmodel)
2. [Running the complete sample production with HTCondor (recommended)](#completesampleproduction)
3. [Running the CMSSW FullSim chain with gridpacks](#fullsimchaingridpacks)
    - [Generating `MadGraph` gridpacks](#generatinggridpacks)
    - [Running the FullSim CMSSW chain for hadronisation with `PYTHIA` and detector simulation with `GEANT4` (local)](#fullsimchainlocal)
    - [FullSim chain using CRAB (Work-In-Progress)](#fullsimchaincrab)
4. [Interactive running](#interactiverunning)
    - [LHE production with `MadGraph` (interactive)](#lhemadgraphinteractive)
    - [Hadronisation with `PYTHIA` and detector simulation with `Delphes` (interactive)](#pythiadelphesinteractive)
5. [Miscellaneous](#misc)
6. [Contact](#contact)
7. [To do](#todo)



# Introduction <a name="introduction"></a>

[![arXiv](https://img.shields.io/badge/arXiv-1707.05326%20-green.svg)](https://arxiv.org/abs/1707.05326)

This repository contains model files necessary for generation of semi-visible jet Monte Carlo signal events in `MadGraph`. It also includes instructions of how to generate gridpacks for production with these models, and how to run them through the FullSim CMSSW chain to create nanoAOD files for analysis. Emulation of 2016, 2017 and 2018 data taking with CMS is supported. Please see [1707.05326](https://arxiv.org/abs/1707.05326) and [1503.00009](https://arxiv.org/abs/1503.00009) for further details about the models. Please note that a recent version of `PYTHIA` (>= 8.230) including the Hidden Valley module and running of the dark coupling is required when implementing the subsequent dark hadronization.

UFO files associated with two UV completions are provided (under [madgraph/models/](madgraph/models/)):


### s-channel model <a name="schannelmodel"></a>

An s-channel production ([DMsimp_SVJ_s_spin1](madgraph/models/DMsimp_SVJ_s_spin1)) mediated through a new heavy Z'. The model provided is a modified version of the spin-1 `DMsimp` model (http://feynrules.irmp.ucl.ac.be/wiki/DMsimp) implemented through `FeynRules`.


### t-channel model <a name="tchannelmodel"></a>

A t-channel production ([DMsimp_SVJ_t](madgraph/models/DMsimp_SVJ_t)) where the dark and visible sectors interact through a new scalar bi-fundamental.

The bi-fundamentals are denoted with `su11, su12, su21, su22...`, where `u` etc explicitly specifies the QCD flavour index and the numbers are the explicit dark non-Abelian group indices. Similarly, the dark quarks are labeled as `qv11, qv12, qv21, qv22`.

Please note that a modified version of `MadGraph` using the patch included [here](https://bugs.launchpad.net/mg5amcnlo/+bug/1702712) is required to ensure a stable cross section for event generation using this model.

A `FeynRules` model file ([DMsimp_tchannel.fr](madgraph/models/DMsimp_SVJ_t/DMsimp_tchannel.fr)) as well as the `Mathematica` notebook ([DMsimp_tchannel.nb](madgraph/models/DMsimp_SVJ_t/DMsimp_tchannel.nb)) used to generated the UFO output are also provided.



## Running the complete sample production with HTCondor (recommended) <a name="completesampleproduction"></a>

There are scripts included to run the entire sample production using a single config file. You specify the input arguments in a YAML file (see [model_params_demo.yaml](config/model_params_demo.yaml) for descriptions or the other files in that directory for complete examples).

Fork this repository, then clone it somewhere with the genproductions repo as a submodule:

```bash
git clone --recursive git@github.com:<user>/SemivisibleJets.git
cd SemivisibleJets
source setup.sh
pip install --user -r requirements.txt
```

In each new session, you must set up the environment with

```bash
source setup.sh
```

Now you can run the gridpack generation according to the parameters in your config file with

```bash
cd gridpack_generation_mg
python submitGridpackGeneration.py <path to YAML config>
```

If the parameters are okay (and there are no bugs in the code), the MadGraph model files and input cards from the template directories I have should be copied into model-specific directories, and the specified parameters will be added. Then, the gridpack will be created in [external/genproductions/bin/MadGraph5_aMCatNLO/](external/genproductions/bin/MadGraph5_aMCatNLO/).

If you plan to run the rest of the sample production via CRAB or by some means that requires a gridpack, you're done! However, if you want to continue here and follow the rest of my steps, great! Now that you have the gridpack, the next stage is to get the LHE file out, apply the PDGID renumbering for the dark particles, and split the LHE file for running the FullSim jobs easily. This is taken care of with

```bash
cd $SVJ_TOP_DIR/gridpack_to_lhe
python runLHERetrieval.py <path to YAML config>
```

The location of the split LHE files will be printed in the terminal, which will be the path specified by the config parameter `lhe_file_path`. **Note that the systematic weights computation is turned off in my fork of the `genproductions` repo**, as this step otherwise takes ages. To turn it back on, uncomment this block in [runcmsgrid_LO.sh](https://github.com/eshwen/genproductions/blob/1d1df93a7078d4aa24c022ba7ea4aa0c977c5de6/bin/MadGraph5_aMCatNLO/runcmsgrid_LO.sh#L165-L177).

Now, the final step is to run the full CMSSW chain on these split LHE files and get nanoAODs out. The cmsDriver commands are in the relevant `.sh` files ([2016](runFullSim_condor_2016.sh)/[2017](runFullSim_condor_2017.sh)/[2018](runFullSim_condor_2018.sh)). And if you would like to change some more specific aspects of the model or hadronisation, either edit your config (as some parameters are detailed there) or [fullsim_cmssw/Condor/writers/write_GS_fragment.py](write_GS_fragment.py). The batch system used for running the jobs is HTCondor, configured to run at lxplus (it _may_ run out of the box on other T2/T3 systems, but may need to be modified if specific requirements need to be met). Now, just run

```bash
cd $SVJ_TOP_DIR/fullsim_cmssw/Condor
python submitFullSim_condor.py <YAML config>
```

which should take care of everything. Hadronisation is performed in `PYTHIA 8.230` -- integrated in an unconventional manner if the default version that ships with CMSSW is too old -- because some LHE files tended to hang with 8.226 (presumably the new module contains patches and bug fixes). The output nanoAOD files will be located in `$work_space/output/`. If some jobs fail, they can be resubmitted by running

```bash
$work_space/resubmit_${model_name}.sh
```

(note that all jobs must _finish running_ first). When happy, the component output files can be combined using [haddnano.py](utils/haddnano.py). A script which does that step will be in `$work_space/combine_components_${model_name}.sh`, which can be run without any arguments.



## Interactive running <a name="interactiverunning"></a>

### LHE production with `MadGraph` (interactive) <a name="lhemadgraphinteractive"></a>

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

In the folder created, the run command is `./bin/mg5_aMC`. Copy the model files from [here](SemivisibleJets/madgraph/models/) into `models/` with

```bash
cp -r ../SemivisibleJets/madgraph/models/DMsimp_* ./models/
```

The input cards for the s- and t-channel processes are specified in [madgraph/input_files/](madgraph/input_files/). In these files, the number of events, output directory, as well as other parameters, can be changed.

Run one of the configs with

```bash
./bin/mg5_aMC ../SemivisibleJets/madgraph/input_files/<file>
```

This will create lots of output files in the directory specified by the config. The LHE file will be zipped in `<Output dir>/Events/run_01/`, which you can unzip with

```bash
gunzip <file>
```

Other information like the cross section and Feynman diagrams can also be viewed.

_N.B._: MadGraph can be a bit erratic and sometimes fail at the "Working on SubProcesses" stage. Just delete the output directory and try again.


### Hadronisation with `PYTHIA` and detector simulation with `Delphes` (interactive) <a name="pythiadelphesinteractive"></a>

As noted above, a recent version of `PYTHIA` (> 8.230) including the Hidden Valley (HV) module and running of the dark coupling is required when implementing the subsequent dark hadronisation.

In order to be able to use the HV module, the PDG IDs of the dark particles must be changed in the LHE files for `PYTHIA` to be able to recognize and shower these properly (see http://home.thep.lu.se/Pythia/pythia82html/HiddenValleyProcesses.html). For both s- and t-channel, there are scripts in [utils/](utils/) to do this:
```bash
./pid_change_{s,t}_channel.sh <LHE filename>
```

Once the PIDs have been changed, it is possible to run `PYTHIA` and `Delphes` concurrently on the LHE file. See the README in https://github.com/eshwen/mc-production/tree/master/run_delphes for the installation commands and how to run everything. On subsequent sessions, you can just `source delphes_pythia8_setup.sh` in that directory to set up the environment.



## Running the CMSSW FullSim chain with gridpacks <a name="fullsimchaingridpacks"></a>

### Generating `MadGraph` gridpacks <a name="generatinggridpacks"></a>

For central production, gridpacks will be needed as external LHE generators don't cooperate with CMSSW. These gridpacks are set up with the master job locally, and each channel run as an HTCondor job. First, clone the relevant repositories as done [here](#completesampleproduction).

All the necessary files for s- and t-channel production are in [madgraph/input_files/](madgraph/input_files/), and a tutorial can be found at https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO. More models can be added if needed, but it is cumbersome. The file names need to be specific, with the same prefix of `<model name>` and have the suffixes as shown in the existing models (e.g., `<model name>_proc_card.dat`). If adding models, use the existing files as templates. Usually, the model files also need to be zipped with

```bash
tar -cf <output file name>.tar <input file(s)>
```

and be copied to the generator web repository on `/afs/cern.ch/cms/generators/www/`. Note that you will need to contact Cms.Computing@cern.ch and cms.generators@cern.ch to request write access to the directory. Though, you will have read access by default. In my branch, I hacked the [gridpack_generation.sh](external/genproductions/bin/MadGraph5_aMCatNLO/gridpack_generation.sh) script and changed L193 (below the "Loading extra model" line) to the same path as the input card directory and specify the model files there.

Validate the input cards you have with

```bash
cd external/genproductions/bin/MadGraph5_aMCatNLO/Utilities/parsing_code
python parsing.py <path to process card directory/name of process card without _proc_card.dat>
```

Once validated, run the gridpack generation with

```bash
cd external/genproductions/bin/MadGraph5_aMCatNLO/
./gridpack_generation.sh <name of process card without _proc_card.dat> <relative path to cards directory> <queue selection>
```

where `<queue selection>` options can be found by typing `bqueues` ("1nd" is usually fine). If instead, you would like to run on Condor (either at lxplus or at a T2/T3 site), run

```bash
cd external/genproductions/bin/MadGraph5_aMCatNLO/
./submit_condor_gridpack_generation.sh <name of process card without _proc_card.dat> <relative path to cards directory> 
```

Note that the architecture, and CMSSW and MadGraph versions are all hardcoded into `gridpack_generation.sh`. They be changed either from within, or with command-line arguments (which only work for arch and CMSSW versions). As with interactive running, MadGraph can be unruly on the "Working on Subprocesses" bit. Just kill and resubmit if that's the case.

Your grid certificate may also be required to run. To initialise a proxy that lasts a week, type

```bash
voms-proxy-init --voms cms --valid 168:00
```

Once completed, the gridpack (in a .tar.xz file) will be located in the current directory. An untarred version is also available for viewing and validation. Just repeat the procedure for other parameters and models.


### Running the FullSim CMSSW chain for hadronisation with `PYTHIA` and detector simulation with `GEANT4` (local) <a name="fullsimchainlocal"></a>

The PID change, as noted [here](#pythiadelphesinteractive), is only necessary when running on interactively-generated LHE files from MadGraph. When generating the gridpacks, I have already included a fix so that once the LHEs are created from the gridpack in CMSSW, the PIDs are changed before hadronisation with Pythia.

Now, to run the full chain, one has to first specify a "GEN fragment", telling CMSSW about the external generator we have used and how to hadronise the particles. The GEN fragment I used can be found in [SVJ_MadGraph_NNPDF30_13TeV_s_spin1_LHE_GS_frag.py](fullsim_cmssw/fragments_deprecated/SVJ_MadGraph_NNPDF30_13TeV_s_spin1_LHE_GS_frag.py). As `MadGraph` was used as the external generator, the `externalLHEProducer` information needs to be included, telling CMSSW where the gridpack is located as well as how many events are in there and the output LHE file (which _should not_ be changed). All the code in the fragment and commands below are specific to emulating 2016 data taking, and `cmsDriver` commands can be changed depending on the context in which you would like to generate samples. Note that you may also have to regenerate the gridpacks with different Parton Distribution Functions to simulate different years. It should be detailed in the quick start guide linked above.

<details>
<summary>Gridpack to LHE-GEN-SIM</summary>
This requires CMSSW\_7\_1\_30 as it contains `PYTHIA` 8.226 with the Hidden Valley module. It can be initialised with

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
cmsrel CMSSW_7_1_30
cd CMSSW_7_1_30/src
cmsenv
mkdir -p Configuration/GenProduction/python
cp $SVJ_TOP_DIR/fullsim_cmssw/SVJ_MadGraph_NNPDF30_13TeV_s_spin1_LHE_GS_frag.py Configuration/GenProduction/python/
scram b
cmsenv
```

** Update this to use Pythia 8.230 **

and then the `cmsDriver` command is

```bash
cmsDriver.py Configuration/GenProduction/python/SVJ_MadGraph_NNPDF30_13TeV_s_spin1_LHE_GS_frag.py --fileout file:SVJ_s_LHE_GEN_SIM.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename SVJ_s_LHE_GEN_SIM.py --no_exec -n 250
```

Once a config has been created, it can be run with `cmsRun`:

```bash
cmsRun SVJ_s_LHE_GEN_SIM.py -n <no. threads>
```

This should give an output root file, which is needed for the next step.
</details>

<details>
<summary>GEN-SIM to AOD (step 1)</summary>
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

From this point, the only input needed by `cmsDriver` is the output root file from the previous step. For the first AOD step, pileup mixing is performed and is required for accurate replication of the conditions for the year of data taking being emulated. However, querying the entire dataset below is unfeasible (as it's 500 TB and 125k files large), so I only specified a text file containing some of the root files. In practice, this, or a smaller dataset are usually fine. One thing to note is, past this point, if your files contain very few events (< 10), specifying a specific number of threads in `cmsRun` can cause failures so it's usually best to leave that option blank. The config for this stage can be made with

```bash
cmsDriver.py step1 --filein file:SVJ_s_LHE_GEN_SIM.root --fileout file:SVJ_s_AOD_step1.root --pileup_input filelist:/afs/cern.ch/user/e/ebhal/Semi-visible_jets/SemivisibleJets/pileup_filelist_2016.txt --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --datamix PreMix --era Run2_2016 --python_filename SVJ_s_AOD_step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 250
```

and run with

```bash
cmsRun SVJ_s_AOD_step1.py -n 8
```
</details>

<details>
<summary>AOD (step 1) to AOD (step 2)</summary>
This is done with the same CMSSW and in the same environment as the previous step. The config is created with

```bash
cmsDriver.py step2 --filein file:SVJ_s_AOD_step1.root --fileout file:SVJ_s_AOD_step2.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --era Run2_2016 --python_filename SVJ_s_AOD_step2.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 250
```

and run with

```bash
cmsRun SVJ_s_AOD_step2.py -n 8
```
</details>

<details>
<summary>AOD (step 2) to miniAOD</summary>
This is done with the same CMSSW and in the same environment as the previous step. The config is created with

```bash
cmsDriver.py --filein file:SVJ_s_AOD_step2.root --fileout file:SVJ_s_MINIAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --era Run2_2016 --python_filename SVJ_s_MINIAOD.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 250
```

and run with

```bash
cmsRun SVJ_s_MINIAOD.py
```
</details>

<details>
<summary>miniAOD to nanoAOD</summary>
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
</details>


### FullSim chain using CRAB (Work-In-Progress) <a name="fullsimchaincrab"></a>

If running over a significant number of events, the GEN-SIM step in the FullSim chain takes awhile. So using CRAB (CMS Remote Analysis Builder) becomes appealing, and is required for central production. The steps are similar to running the chain locally, but now the CMSSW config generated by `cmsDriver.py` is given to a CRAB config file, which is uploaded to the CERN grid and executed.

An example config for the gridpack to LHE step is located in [crab_LHE_s.py](fullsim_cmssw/CRAB_WIP/crab_LHE_s.py), with an accompanying gen fragment. The comments should be detailed enough, with the CMSSW config being specified by `config.JobType.psetName` and being created as it would be when running locally.

The main thing to notice about the gen fragment is the path to the gridpack. For private production, you can't put a gridpack on `/cvmfs`, which is normally the standard procedure. The workaround is to specify the gridpack path as `../<basename of gridpack>` in the gen fragment. Then, in the CRAB config, specify the absolute path to the gridpack in `config.JobType.inputFiles`, making sure the gridpack is in a publicly-accessible directory. On lxplus, directory permissions can be changed for `/afs` with

```bash
fs sa <path to folder> system:anyuser rl
```

which gives any user read permissions. This is important as the CRAB server (or node) needs access to upload the gridpack to the sandbox tied to the job. When ready to submit the CRAB job(s), you will first have to source the CMSSW release used to make the CMSSW config, and then set up the CRAB environment with

```bash
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

and submit with

```bash
crab submit -c <CRAB config>
```

It is possible to monitor the status of the jobs with `crab status`. Failed jobs can also be resubmitted with `crab resubmit <CRAB project directory>`, where `<CRAB project directory>` is created (usually) in the directory you submitted from. When submitting jobs, you will be prompted for your grid certificate authentication.

For the other steps in the FullSim chain, the procedure is the same as described above. Create a CMSSW config that is passed to the CRAB config (see examples in fullsim_cmssw/CRAB_WIP/ for templates), and submit the job(s) to the CRAB server. The main differences are that, instead of when running locally, the LHE-GEN-SIM step should be split into gridpack to LHE, and LHE to GEN-SIM steps. When running the LHE step, it must be submitted as a single job per gridpack. But when running LHE to GEN-SIM, you can split it into several jobs by specifying in `config.Data.unitsPerJob` and `config.Data.totalUnits` in the CRAB config.

_FINISH_



## Miscellaneous <a name="misc"></a>

- To upgrade the installed pip packages, run
```bash
pip install --user --upgrade -r requirements.txt
```
- Some rudimentary plotting, for a quick look at distributions, can be done by running [plotSVJHistos.py](utils/plotSVJHistos.py). You just need to specify the root files in the list `files`.
- This repository utlises many software packages. To cite any of them, I have listed their BibTeX entries in [software_references.bib](utils/software_references.bib)


## Contact <a name="contact"></a>

For questions or issues please contact:

-  Tim Lou; hlou@berkeley.edu
-  Siddharth Mishra-Sharma; smsharma@princeton.edu
-  Eshwen Bhal (for implementation, not theory); eshwen.bhal@cern.ch



## To do <a name="todo"></a>

- Consider changing dark quarks to spin-1/2 in MadGraph model files (would have to change `spin` attribute in particles.py to '2'). Find out if that will affect decays or anything. Would also need to consider the spin of the dark hadron (see HV documentation in Pythia for PDGIDs).
- See if I still need to do the confinement scale rescaling
- Add n_c to config file? How would changing value affect things physically/kinematically?
- Figure out correct xsec values for t-channel as has been done for s-channel. Update scripts accordingly
- Rewrite plotting script to do in 2 stages. Run fast-carpenter with a config file of important variables, etc., to make a summary dataframe for each model. Then run fast-plotter with a plotting config to make matplotlib plots. Move everything to a new directory: `$SVJ_TOP_DIR/plotting/`
- Replace my `m_d` with `m_dq` so as not to confuse with FNAL's m_d = m_dark_hadron
- Add support for running at other T2/T3 sites
- Consider switching to conda/virtualenv so managing environments and packages/installs are simpler

- Whenever I change/update things, remember to update the README as well
