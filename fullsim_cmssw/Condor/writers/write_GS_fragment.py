import os
from load_yaml_config import load_yaml_config


def write_GS_fragment(config, Lambda_d, GS_dir):
    """
    Write GEN-SIM fragment for job and return its path.
    """
    # Load YAML config into a dictionary and assign values to variables for cleanliness
    input_params = load_yaml_config(config)

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

    in_file = os.path.join(GS_dir, "{0}_GS_fragment.py".format(model_name))
    f = open(in_file, "w")

    f.write("""import FWCore.ParameterSet.Config as cms
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
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off', # if 'on', merging parameters are set according to LHE file
            'JetMatching:scheme = 1', # 1 = scheme inspired by Madgraph matching code
            'JetMatching:merge = on', # master switch to activate parton-jet matching. when off, all external events accepted
            'JetMatching:jetAlgorithm = 2', # 2 = SlowJet clustering
            'JetMatching:etaJetMax = 5.', # max eta of any jet
            'JetMatching:coneRadius = 1.0', # gives the jet R parameter
            'JetMatching:slowJetPower = 1', # -1 = anti-kT algo, 1 = kT algo. Only kT w/ SlowJet is supported for MadGraph-style matching
            'JetMatching:qCut = 100.', # this is the actual merging scale. should be roughly equal to xqcut in MadGraph
            'JetMatching:nJetMax = 2', # number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', # off for MLM matching, turn on for shower-kT matching
            ),
        processParameters = cms.vstring(""".format(cross_section=x_sec))

    if process_type == 's-channel':
        f.write("""
            '4900023:m0 = {}', # explicitly stating Z' mass in case it's not picked up properly by Pythia""".format(m_med))
    elif process_type == 't-channel':
        f.write("""
            # ADD SHIT HERE""")

    f.write("""
            '4900101:m0 = {m_dark_quark:.0f}', # explicitly stating dark quark mass in case it's not picked up properly by Pythia
            '4900111:m0 = {m_dark_meson:.0f}', # Dark meson mass. PDGID corresponds to pivDiag HV spin-0 meson that can decay into SM particles
            '4900211:m0 = {m_dark_stable:.1f}', # Stable dark particle mass. PDGID corresponds to pivUp off-diagonal HV spin-0 meson that's stable and invisible
            '4900111: oneChannel = 1 {r_inv:.2f} 4900211 -4900211', # Dark meson decay into stable dark particles with branching fraction r_inv
            '4900111: addChannel = 1 {remain_BR:.2f} 91 1 -1', # Dark meson decay into down quarks with branching fraction 1 - r_inv
            #'TimeShower:nPartonsInBorn = 2', #number of coloured particles (before resonance decays) in born matrix element
            #'HiddenValley:ffbar2Zv = on', #it works only in the case of narrow width approx
            'HiddenValley:fragment = on', # enable hidden valley fragmentation
            #'HiddenValley:NBFlavRun = 0', # number of bosonic flavor for running
            #'HiddenValley:NFFlavRun = 2', # number of fermionic flavor for running
            'HiddenValley:alphaOrder = 1', # order at which running coupling runs
            'HiddenValley:Lambda = {Lambda_dark:.2f}', # parameter used for running coupling
            'HiddenValley:nFlav = {nFlav:.0f}', # this dictates what kind of hadrons come out of the shower, if nFlav = 2, for example, there will be many different flavor of hadrons
            'HiddenValley:probVector = 0.', # ratio of number of vector mesons over scalar meson, 3:1 is from naive degrees of freedom counting (so 0.75). But allows hadronisation into more species of dark particle no nFlav may not make physical sense
            'HiddenValley:pTminFSR = {pTminFSR:.2f}', # cutoff for the showering, should be roughly confinement scale
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    'JetMatchingParameters'
                                    )
    )
)
""".format(m_dark_quark=m_d, m_dark_meson=m_dark_meson, m_dark_stable=m_dark_stable, r_inv=r_inv,
           remain_BR=1-r_inv, Lambda_dark=Lambda_d, nFlav=n_f, pTminFSR=1.1*Lambda_d)
    )
    f.close()

    return in_file
