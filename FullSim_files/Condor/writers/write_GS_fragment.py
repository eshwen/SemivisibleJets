import argparse
import math
import os
import pprint
from subprocess import call
import sys
import yaml
import calcDarkParams as cDP

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type = str, default = os.path.join(os.environ['SVJ_TOP_DIR'], "config", "model_params_s_spin1.yaml"), help = "Path to YAML config to parse")
parser.add_argument("-l", "--Lambda_d", type = float, help = "Confinement scale for dark hadrons")
args = parser.parse_args()

def main():
    """
    Write GEN-SIM fragment for job. Due to the nature of the "return" statement at the end,
    users editing this script are to refrain from including any print statements as it disrupts
    the returning of the file path.
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = yaml.load( open(args.config, 'r') )

    work_space = input_params['work_space']
    model_name = input_params['model_name']
    m_d = input_params['m_d']
    n_f = input_params['n_f']
    r_inv = input_params['r_inv']
    x_sec = input_params['x_sec']

    Lambda_d = format(args.Lambda_d, '.1f')

    # Calculate masses of dark mesons and stable dark matter particles
    m_dark_meson = 2 * m_d
    m_dark_stable = m_d - 0.1

    cmsswDir = "CMSSW_7_1_30/src/Configuration/GenProduction/python"

    filePath = os.path.join(work_space, cmsswDir, "{0}_GS_fragment.py".format(model_name))
    writeFile = open(filePath, "w")
    
    writeFile.write("""import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double({0}),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8aMCatNLOSettingsBlock,
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 100.', #this is the actual merging scale                           
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
            ),
        processParameters = cms.vstring(
            '4900111:m0 = {1}', # Dark meson mass
            '4900211:m0 = {2}', # Stable dark particle mass
            '4900111: oneChannel = 1 {3} 4900211 -4900211', # Dark meson decay into stable dark particles with branching fraction r_inv
            '4900111: addChannel = 1 {4} 91 1 -1', # Dark meson decay into down quarks with branching fraction 1 - r_inv
            #'TimeShower:nPartonsInBorn = 2', #number of coloured particles (before resonance decays) in born matrix element
            'HiddenValley:ffbar2Zv = on', #it works only in the case of narrow width approx
            'HiddenValley:fragment = on', # enable hidden valley fragmentation
            #'HiddenValley:NBFlavRun = 0', # number of bosonic flavor for running
            #'HiddenValley:NFFlavRun = 2', # number of fermionic flavor for running
            'HiddenValley:alphaOrder = 1', # order at which running coupling runs
            'HiddenValley:Lambda = {5}', # parameter used for running coupling
            'HiddenValley:nFlav = {6}', # this dictates what kind of hadrons come out of the shower, if nFlav = 2, for example, there will be many different flavor of hadrons
            'HiddenValley:probVector = 0.', # ratio of number of vector mesons over scalar meson, 3:1 is from naive degrees of freedom counting (so 0.75). But allows hadronisation into more species of dark particle no nFlav may not make physical sense
            'HiddenValley:pTminFSR = {7}', # cutoff for the showering, should be roughly confinement scale
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    'JetMatchingParameters'
                                    )
    )
)
""".format(x_sec, m_dark_meson, m_dark_stable, r_inv, 1-r_inv, Lambda_d, n_f, 1.1*Lambda_d)
    )                   
    writeFile.close()

    # Basically return statement for bash script. DO NOT CHANGE!
    print filePath


if __name__ == '__main__':
    main()

