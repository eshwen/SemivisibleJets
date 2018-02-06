# Semi-visible Jets

[![arXiv](https://img.shields.io/badge/arXiv-1707.05326%20-green.svg)](https://arxiv.org/abs/1707.05326)

This repository contains model files necessary for generation of semi-visible jet Monte Carlo signal events in `MadGraph`. 
Please see [1707.05326](https://arxiv.org/abs/1707.05326) and [1503.00009](https://arxiv.org/abs/1503.00009) for
for further details. Please note that a recent version of `PYTHIA` (> 8.226) including the Hidden Valley module 
and running of the dark coupling is required when implementing the subsequent dark hadronization.

UFO files associated with two UV completions are provided:

## s-channel production

An s-channel production (`DMsimp_s_spin1`) mediated through a new heavy Z'. The model provided is a modified version of the spin-1 `DMsimp` model (http://feynrules.irmp.ucl.ac.be/wiki/DMsimp) 
implemented through `FeynRules`.

## t-channel production

A t-channel production (`DMsimp_tchannel`) where the dark and visible sectors interact through a new scalar bi-fundamental.

The bi-fundamentals are denoted with `su11, su12, su21, su22...`, where `u` etc explicitly specifies the QCD flavour index 
and the numbers are the explicit dark non-Abelian group indices. Similarly, the dark quarks are labeled as `qv11, qv12, qv21, qv22`.

Please note that a modified version of `MadGraph` using the patch included [here](https://bugs.launchpad.net/mg5amcnlo/+bug/1702712) 
is required to ensure a stable cross section for event generation using this model.

A `FeynRules` model file (`DMsimp_tchannel.fr`) as well as the `Mathematica` notebook (`DMsimp_tchannel.nb`) used to generated the UFO output 
are also provided.

## Example `MadGraph` production

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

In the folder created, the run command is `./bin/mg5_aMC`. Copy the model files from `SemivisibleJets/` into `models/` with

```bash
cp -r ../SemivisibleJets/MG_models/DMsimp_* ./models/
```

The input/config files for the s- and t-channel processes are specified in `SemivisibleJets/MG_input/`. In these files, the number of events, output directory, as well as other parameters, can be changed.

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

## Hadronization with `PYTHIA` and detector simulation with `Delphes`

As noted above, a recent version of `PYTHIA` (> 8.226) including the Hidden Valley (HV) module and running of the dark coupling is required when implementing the subsequent dark hadronization.

In order to be able to use the HV module, the PDG IDs of the dark particles must be changed in the LHE files for `PYTHIA` to be able to recognize and shower these properly. This can be done as follows:

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

from this directory. Once the PIDs have been changed, it is possible to run `PYTHIA` and `Delphes` concurrently on the LHE file. See the README in https://github.com/eshwen/mc-production/tree/master/run_delphes for the installation commands and how to run everything. On subsequent sessions, you can just `source delphes_pythia8_setup.sh` in that directory to set up the environment.

## Contact

For questions or issues please contact:

-  Tim Lou; hlou@berkeley.edu
-  Siddharth Mishra-Sharma; smsharma@princeton.edu
-  Eshwen Bhal (for implementation, not theory); eshwen.bhal@cern.ch

## To do

- Tidy up `sed` commands for t-channel (make into a single line)
- Make sure commands and code are robust and validate output