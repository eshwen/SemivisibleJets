import math
import os
import yaml
import calcDarkParams as cDP

def write_GS_fragment(config, Lambda_d, GS_dir):
    """
    Write GEN-SIM fragment for job and return its path.
    """

    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = yaml.load( open(config, 'r') )

    model_name = input_params['model_name']
    m_med = input_params['m_med']
    m_d = input_params['m_d']
    n_f = input_params['n_f']
    r_inv = input_params['r_inv']
    x_sec = input_params['x_sec']
    process_type = input_params['process_type']

    Lambda_d = round(Lambda_d, 2)

    # Calculate masses of dark mesons and stable dark matter particles
    m_dark_meson = 2 * m_d
    m_dark_stable = m_d - 0.1

    filePath = os.path.join(GS_dir, "{0}_GS_fragment.py".format(model_name))
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
    crossSection = cms.untracked.double({cross_section:f}),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8aMCatNLOSettingsBlock,
       # JetMatchingParameters = cms.vstring(
       #     'JetMatching:setMad = off', # if 'on', merging parameters are set according to LHE file
       #     'JetMatching:scheme = 1', # 1 = scheme inspired by Madgraph matching code
       #     'JetMatching:merge = on', # master switch to activate parton-jet matching. when off, all external events accepted 
       #     'JetMatching:jetAlgorithm = 2', # 2 = SlowJet clustering
       #     'JetMatching:etaJetMax = 5.', # max eta of any jet
       #     'JetMatching:coneRadius = 1.1', # gives the jet R parameter
       #     'JetMatching:slowJetPower = 1', # -1 = anti-kT algo, 1 = kT algo. Only kT w/ SlowJet is supported for MadGraph-style matching
       #     'JetMatching:qCut = 100.', # this is the actual merging scale. should be roughly equal to xqcut in MadGraph
       #     'JetMatching:nJetMax = 2', # number of partons in born matrix element for highest multiplicity
       #     'JetMatching:doShowerKt = off', # off for MLM matching, turn on for shower-kT matching
       #     ),
        processParameters = cms.vstring(""".format(cross_section=x_sec))

    if process_type == 's-channel':
        writeFile.write("""
            '4900023:m0 = {0}', # explicitly stating Z' mass in case it's not picked up properly by Pythia""".format(m_med))
    elif process_type == 't-channel':
        writeFile.write("""
            # ADD SHIT HERE""")

    writeFile.write("""
            '4900101:m0 = {m_dark_quark:.0f}', # explicitly stating dark quark mass in case it's not picked up properly by Pythia
            '4900111:m0 = {m_dark_meson:.0f}', # Dark meson mass. PDGID corresponds to pivDiag HV spin-0 meson that can decay into SM particles
            '4900211:m0 = {m_dark_stable:.1f}', # Stable dark particle mass. PDGID corresponds to pivUp off-diagonal HV spin-0 meson that's stable and invisible
            '4900111: oneChannel = 1 {r_inv:.2f} 4900211 -4900211', # Dark meson decay into stable dark particles with branching fraction r_inv
            '4900111: addChannel = 1 {remain_BR:.2f} 91 1 -1', # Dark meson decay into down quarks with branching fraction 1 - r_inv
            'HiddenValley:Ngauge = 1',
            'HiddenValley:spinFv = 1',
            'HiddenValley:spinqv = 0',
            'HiddenValley:FSR = on',
            'HiddenValley:fragment = on',
            'HiddenValley:alphaOrder = 1',
            'HiddenValley:Lambda = {Lambda_dark:.2f}',
            'HiddenValley:nFlav = {nFlav:.0f}',
            'HiddenValley:probVector = 0.0',
            'HiddenValley:pTminFSR = {pTminFSR:.2f}',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    #'JetMatchingParameters'
                                    )
    )
)
""".format(m_dark_quark=m_d, m_dark_meson=m_dark_meson, m_dark_stable=m_dark_stable, r_inv=r_inv,
           remain_BR=1-r_inv, Lambda_dark=Lambda_d, nFlav=n_f, pTminFSR=1.1*Lambda_d)
                    )                   
    writeFile.close()

    return filePath
