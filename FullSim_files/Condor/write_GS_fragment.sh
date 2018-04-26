#!/bin/bash

# Write the GEN-SIM fragment based on the model parameters specified

model_name=$1
seed=$2
n_f=$3
Lambda_d=$4
r_inv=$5
x_sec=$6
m_d=$7
work_space=$8

# Calculate dark meson mass and stable dark particle masses here (as it's difficult to do it in bash)                                                                                                                                                                  
m_dark_meson=$(echo "$m_d * 2" | bc -l) # dark meson should be twice the dark quark mass
m_dark_stable=$(echo "$m_d - 0.1" | bc -l) # 0.1 GeV lighter than dark quark so it stays stable

echo "import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *

generator = cms.EDFilter(\"Pythia8HadronizerFilter\",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double(${x_sec}),
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
            '4900111:m0 = $m_dark_meson', # Dark meson mass
            '4900211:m0 = $m_dark_stable', # Stable dark particle mass
            '4900111: oneChannel = 1 $r_inv 4900211 -4900211', # Dark meson decay into stable dark particles with branching fraction r_inv
            '4900111: addChannel = 1 $(echo "1.0 - $r_inv" | bc -l) 91 1 -1', # Dark meson decay into down quarks with branching fraction 1 - r_inv
            #'TimeShower:nPartonsInBorn = 2', #number of coloured particles (before resonance decays) in born matrix element
            'HiddenValley:ffbar2Zv = on', #it works only in the case of narrow width approx
            'HiddenValley:fragment = on', # enable hidden valley fragmentation
            #'HiddenValley:NBFlavRun = 0', # number of bosonic flavor for running
            #'HiddenValley:NFFlavRun = 2', # number of fermionic flavor for running
            'HiddenValley:alphaOrder = 1', # order at which running coupling runs
            'HiddenValley:Lambda = $Lambda_d', # parameter used for running coupling
            'HiddenValley:nFlav = $n_f', # this dictates what kind of hadrons come out of the shower, if nFlav = 2, for example, there will be many different flavor of hadrons
            'HiddenValley:probVector = 0.75', # ratio of number of vector mesons over scalar meson, 3:1 is from naive degrees of freedom counting
            'HiddenValley:pTminFSR = 10', # cutoff for the showering, should be roughly confinement scale
            ),

        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    'JetMatchingParameters'
                                    )
    )
)
" > ${work_space}/GS_fragments/${model_name}_GS_fragment_${seed}.py

echo ${work_space}/GS_fragments/${model_name}_GS_fragment_${seed}.py