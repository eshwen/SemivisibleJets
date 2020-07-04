# SemivisibleJets

- [SemivisibleJets](#semivisiblejets)
  * [Introduction](#introduction)
    + [s-channel model](#s-channel-model)
    + [t-channel model](#t-channel-model)
  * [Running the complete sample production with HTCondor (recommended)](#running-the-complete-sample-production-with-htcondor)
  * [Interactive running (deprecated)](#interactive-running)
  * [Running the CMSSW FullSim chain with gridpacks (deprecated)](#running-the-cmssw-fullsim-chain-with-gridpacks)
  * [Miscellaneous](#miscellaneous)
  * [Troubleshooting](#troubleshooting)
  * [Contact](#contact)
  * [To do](#to-do)

## Introduction

[![arXiv](https://img.shields.io/badge/arXiv-1707.05326%20-green.svg)](https://arxiv.org/abs/1707.05326)

This repository contains model files necessary for generation of semi-visible jet Monte Carlo signal events in `MadGraph`. It also includes instructions of how to generate gridpacks for production with these models, and how to run them through the FullSim CMSSW chain to create nanoAOD files for analysis. Emulation of 2016, 2017 and 2018 data taking with CMS is supported. Please see [1707.05326](https://arxiv.org/abs/1707.05326) and [1503.00009](https://arxiv.org/abs/1503.00009) for further details about the models. Please note that a recent version of `PYTHIA` (>= 8.230) including the Hidden Valley module and running of the dark coupling is required when implementing the subsequent dark hadronization.

UFO files associated with two UV completions are provided (under [madgraph/models/](madgraph/models/)):

### s-channel model

An s-channel production (e.g., [DMsimp_SVJ_s_spin1_mZp-1000_mDQ-10_rinv-0p3](madgraph/models/DMsimp_SVJ_s_spin1_mZp-1000_mDQ-10_rinv-0p3)) mediated through a new heavy Z'. The model provided is a modified version of the spin-1 `DMsimp` model (http://feynrules.irmp.ucl.ac.be/wiki/DMsimp) implemented through `FeynRules`.

### t-channel model

A t-channel production (e.g., [DMsimp_SVJ_t_mPhi-1000_mDQ-10_rinv-0p3](madgraph/models/DMsimp_SVJ_t_mPhi-1000_mDQ-10_rinv-0p3)) where the dark and visible sectors interact through a new scalar bi-fundamental.

The bi-fundamentals are denoted with `su11, su12, su21, su22...`, where `u` etc explicitly specifies the QCD flavour index and the numbers are the explicit dark non-Abelian group indices. Similarly, the dark quarks are labeled as `qv11, qv12, qv21, qv22`.

Please note that a modified version of `MadGraph` using the patch included [here](https://bugs.launchpad.net/mg5amcnlo/+bug/1702712) is required to ensure a stable cross section for event generation using this model.

A `FeynRules` model file ([DMsimp_tchannel.fr](madgraph/models/DMsimp_SVJ_t_mPhi-1000_mDQ-10_rinv-0p3/DMsimp_tchannel.fr)) as well as the `Mathematica` notebook ([DMsimp_tchannel.nb](madgraph/models/DMsimp_SVJ_t_mPhi-1000_mDQ-10_rinv-0p3/DMsimp_tchannel.nb)) used to generated the UFO output are also provided.

## Running the complete sample production with HTCondor

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
python gridpack_generation_mg/submitGridpackGeneration.py <path to YAML config>
```

If the parameters are okay (and there are no bugs in the code), the MadGraph model files and input cards should be copied from the template directories into model-specific directories, and the specified parameters will be added. Then, the gridpack will be created in [external/genproductions/bin/MadGraph5_aMCatNLO/](external/genproductions/bin/MadGraph5_aMCatNLO/).

If you plan to run the rest of the sample production via CRAB or by some means that requires a gridpack, you're done! However, if you want to continue here and follow the rest of my steps, great! Now that you have the gridpack, the next stage is to get the LHE file out, apply the PDGID renumbering for the dark particles, and split the LHE file for running the FullSim jobs easily. This is taken care of with

```bash
python gridpack_to_lhe/runLHERetrieval.py <path to YAML config>
```

The location of the split LHE files will be printed in the terminal (it is specified by the config parameter `lhe_file_path`). **Note that the systematic weights computation is turned off in my fork of the `genproductions` repo**, as this step otherwise takes ages. To turn it back on, uncomment this block in [runcmsgrid_LO.sh](https://github.com/eshwen/genproductions/blob/1d1df93a7078d4aa24c022ba7ea4aa0c977c5de6/bin/MadGraph5_aMCatNLO/runcmsgrid_LO.sh#L165-L177).

Now, the final step is to run the full CMSSW chain on these split LHE files and get nanoAODs out. The relevant `cmsDriver` commands are in the `runFullSim_condor_YYYY.sh` files ([2016](runFullSim_condor_2016.sh)/[2017](runFullSim_condor_2017.sh)/[2018](runFullSim_condor_2018.sh)). If required, you change certain parameters of the model (in your config), hadronisation treatment (in [write_GS_fragment.py](fullsim_cmssw/Condor/writers/write_GS_fragment.py)), or the CMSSW versions (in [cmssw_info.py](fullsim_cmssw/Condor/cmssw_info.py)).

The batch system used for running the jobs is HTCondor, configured to run at lxplus (it _may_ run out of the box on other T2/T3 systems, but may need to be modified if specific requirements need to be met). Now, just run

```bash
python fullsim_cmssw/Condor/submitFullSim_condor.py <YAML config>
```

which should take care of everything. Hadronisation is performed in `PYTHIA 8.230` -- integrated in an unconventional manner if the default version that ships with CMSSW is too old -- because some LHE files tended to hang with 8.226 (presumably the new module contains patches and bug fixes). The output nanoAOD files will be located in `$work_space/output/`. If some jobs fail, they can be resubmitted by running

```bash
$work_space/resubmit_${model_name}.sh
```

(note that all jobs must _finish running_ first). When happy, the output files from each job can be combined using [haddnano.py](utils/haddnano.py). A script which performs that step will is

```bash
$work_space/combine_components_${model_name}.sh
```

If you then want to clean up the work space (remove log files, submission scripts, and leftover output from the finished model), run

```bash
$work_space/cleanup_residue_${model_name}.sh
```

## Interactive running

This isn't maintained any more. An old version of this README ([here](https://github.com/eshwen/SemivisibleJets/blob/d8fc373dd4081a14752859f18a6c0b2eefc10b1e/README.md)) has instructions (that may be outdated) on how to create gridpacks locally, and FullSim production with either CRAB or CMSSW locally.

## Running the CMSSW FullSim chain with gridpacks

This isn't maintained any more. An old version of this README ([here](https://github.com/eshwen/SemivisibleJets/blob/d8fc373dd4081a14752859f18a6c0b2eefc10b1e/README.md)) has instructions (that may be outdated) on how to create gridpacks locally, and use Pythia + Delphes for hadronisation and detector simulation (i.e., outside of CMSSW).

## Miscellaneous

- To upgrade the installed pip packages, run
```bash
pip install --user --upgrade -r requirements.txt
```
- Some rudimentary plotting, for a quick look at distributions, can be done by running [plotSVJHistos.py](utils/plotSVJHistos.py). You just need to specify the root files in the list `files`.
- For the s-channel mode, the couplings between the Z' and SM quarks is 1.0. This can be verified in the variables `g{V,A}{u,d}##` in [parameters.py](madgraph/models/DMsimp_SVJ_s_spin1_editTemplate/parameters.py)
- The PDF sets used for 2016, 2017, and 2018 generation are detailed in [lhaIDs.py](utils/lhaIDs.py)
- For now, the output nanoAOD files are use the NanoAODv1 configuration for 2016, and NanoAODv5 for the other years. I am looking into updating the 2016 workflow to use NanoAODv5 for consistency
- This repository utlises many software packages. To cite any of them, I have listed their BibTeX entries in [software_references.bib](utils/software_references.bib)

## Troubleshooting

Below are some of the common issues experienced when using this repo and some potential fixes.

- Gridpack generation stage:
  - _MadGraph fails to compile_. MadGraph is quite a large program with lots of plug-ins. Occasionally, it will fail to compile properly. Retry the command. If it persistently fails though, it could be a problem with your environment. Doing `eval \`scram unsetenv -sh\`` should more-or-less give you a clean shell, and should help with things. Otherwise, contact someone in [Contact](#contact), or the `genproductions` maintainers if you think it's a MadGraph problem.
  - _The t-channel process takes ages/often fails_. The t-channel process is much more complex than the s-channel, and there's not a lot that can be done about optimising it, unfortunately. Many diagrams and subprocesses have to be simulated. Running the gridpack generation step with `-m batch` will use HTCondor to run the subprocesses, but if even one job gets held, it causes the entire thing to crash. That seems to be a fault with MadGraph/genproductions, so I don't know how to get around that. Running locally (with `-m local`) in a terminal multiplexing (e.g., `screen`) session might be an alternative. But at least on lxplus, I've found that disconnecting and reconnecting doesn't transfer permissions properly and the process dies anyway. Running this on a different remote server may avoid the problem, but I've only tested this code on lxplus.
- FullSim stage:
  - _Problems with the AOD step 1 (pre-mixing) step_. It's a pain in the butt to get the pileup input right for this step. Checking McM for reference, I see most setup commands for centrally-produced datasets just give the `cmsDriver.py` option `--pileup_input "dbs:<dataset>"`. The problem is these datasets are large (tens of TB), and the file query that's run on the dataset can hang, then fail. The best alternative I've found for private production is just to query the dataset myself (as I can continuously retry), selecting some of the files, and then putting the paths in a `pileup_filelist_201X.txt` file for `cmsDriver.py` to parse. But again, these are large datasets, and the storage sites supplying them can fail, etc., so it's not a foolproof method. If you see a repeated problem in the log files saying it was unable to access some of these files, it might be best to swap out the files you're using. The paths are given as `/store/mc/...`, followed by the rest of the subdirectories. You can find the files on EOS by prepending the directory with `/eos/cms/`, and explicitly check there to see if any files exist for the dataset. The xrootd redirector that attempts to find the files in your pileup file list checks there first. If files exist, consider replacing your pileup file list with the files that exist in the directory. Otherwise, try replacing them with files from another dataset corresponding to the same data-taking year.
- Using the environment-sourced `ROOT` to look at the nanoAODs:
  - If, like me, you want to inspect some of the output files, the version of `ROOT` sourced when this repo's environment is sourced may not work with the files and crash. To fix this, go to your `work_space` directory, find the latest CMSSW version in there, and do `cmsenv` in that version's `src/` subdirectory

## Contact

For questions or issues please contact:

-  Tim Lou; [hlou@berkeley.edu](mailto:hlou@berkeley.edu)
-  Siddharth Mishra-Sharma; [smsharma@princeton.edu](mailto:smsharma@princeton.edu)
-  Eshwen Bhal (for implementation, not theory); [eshwen.bhal@cern.ch](mailto:eshwen.bhal@cern.ch)

## To do

- Consider changing dark quarks to spin-1/2 in MadGraph model files (would have to change `spin` attribute in particles.py to '2'). Find out if that will affect decays or anything. Would also need to consider the spin of the dark hadron (see HV documentation in Pythia for PDGIDs).
- See if I still need to do the confinement scale rescaling
- Add n_c to config file? How would changing value affect things physically/kinematically?
- Figure out correct xsec values for t-channel as has been done for s-channel. Update scripts accordingly
- Rewrite plotting script to do in 2 stages. Run fast-carpenter with a config file of important variables, etc., to make a summary dataframe for each model. Then run fast-plotter with a plotting config to make matplotlib plots. Move everything to a new directory: `$SVJ_TOP_DIR/plotting/`
- Replace my `m_d` with `m_dq` so as not to confuse with FNAL's m_d = m_dark_hadron
- Consider updating code to Python 3 (need to be careful of `print`, relative imports). Will need to update Python version sourced in setup script (or accommodate in conda/virtualenv if I implement)
- Add support for running at other T2/T3 sites
- Consider switching to conda/virtualenv so managing environments and packages/installs are simpler
- Whenever I change/update things, remember to update the README as well
