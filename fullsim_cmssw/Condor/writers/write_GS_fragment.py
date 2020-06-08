from __future__ import print_function
import calc_dark_params as cdp
from colorama import Fore, init
import os
from load_yaml_config import load_yaml_config
from mass_runner import MassRunner
from xsec_from_dict import xsec_from_dict


class WriteGenSimFragment(object):
    """
    Write GEN-SIM fragment for job and return its path.
    """
    def __init__(self, config, GS_dir):
        """ Load YAML config into a dictionary and assign values to variables for cleanliness """
        _config = load_yaml_config(config, quiet=True)

        # Reset text colours after colourful print statements
        init(autoreset=True)

        self.model_name = _config['model_name']
        self.m_med = _config['m_med']
        self.m_d = _config['m_d']
        self.n_f = _config['n_f']
        self.r_inv = _config['r_inv']
        self.x_sec_mg = _config['x_sec_mg']
        self.alpha_d = _config['alpha_d']
        self.process_type = _config['process_type']
        self.year = _config['year']

        self.GS_dir = GS_dir

        # Run everything
        print(Fore.CYAN + "Writing gen fragment...")
        self.set_dark_params()
        self.get_lambda_d()
        self.get_xsec()
        self.get_pythia_info()
        self.write_fragment()

    def set_dark_params(self):
        self.n_c = 2
        self.m_dark_meson = 2 * self.m_d
        # Calculate mass of stable dark matter particles
        self.m_dark_stable = self.m_d - 0.1

    def get_lambda_d(self):
        """ Calculate Lambda_d (confinement scale) """
        if isinstance(self.alpha_d, str):
            _Lambda_d = cdp.calc_lambda_d_from_str(self.n_c, self.n_f, self.alpha_d, self.m_dark_meson)
        else:
            _Lambda_d = cdp.calc_lambda_d(self.n_c, self.n_f, self.alpha_d)
        self.Lambda_d = round(_Lambda_d, 4)
        print(Fore.MAGENTA + "Confinement scale Lambda_d =", self.Lambda_d)

        # Rescale Lambda_d if too low (should be >= m_d), then recalc alpha_d
        #if Lambda_d < m_d:
        #    Lambda_d = 1.1 * m_d
        #    alpha_d = cdp.calc_alpha_d(n_c, n_f, Lambda_d)
        #    print(Fore.MAGENTA + "Recalculated alpha_d =", alpha_d)

    def get_xsec(self):
        """ Get cross section from dictionary if possible, to replace value calculated by MadGraph """
        if self.process_type == 's-channel':
            self.x_sec = xsec_from_dict(os.path.join(os.environ['SVJ_TOP_DIR'], 'utils/xsecs_{}.yaml'.format(self.process_type)), self.m_med)
            print(Fore.CYAN + "Taking cross section from dictionary instead of MadGraph's calculation...")
        else:
            self.x_sec = self.x_sec_mg

    def get_quark_mass_dict(self):
        """ Return dictionary of quark rest masses """
        quark_masses = {  # PDGID: mass (GeV)
            1: 0.0048,    # down
            2: 0.0023,    # up
            3: 0.095,     # strange
            4: 1.275,     # charm
            5: 4.18,      # bottom
        }

        # Check if dark hadron mass > b quark. If so, all quarks are in the mix. Otherwise remove b from calculations
        if (self.m_dark_meson > quark_masses[5]):
            return quark_masses
        else:
            return {k: v for k, v in quark_masses.items() if k < 5}

    def remaining_br_democratic(self, n_quarks):
        """ Democratically allocate remaining BR (1 - r_inv)/n_quarks """
        # Can expand this in the future to take the running b- and c-quark masses into account
        return (1.0 - self.r_inv) / float(n_quarks)

    def remaining_br_mass_insertion(self, quark_id):
        """ Calculating running quark masses and use to calculate branching ratio """
        m_q_dict = self.get_quark_mass_dict()
        normaliser = sum([MassRunner(mass, len(m_q_dict), self.m_dark_meson, self.n_f).m_run ** 2 for mass in m_q_dict.values()])
        try:
            m_run = MassRunner(m_q_dict[quark_id], len(m_q_dict), self.m_dark_meson, self.n_f).m_run
            remain_br = (1.0 - self.r_inv) * (m_run ** 2) / normaliser
        except KeyError:  # i.e., if m_dark_meson < b quark
            remain_br = 0
        return remain_br

    def get_pythia_info(self):
        if self.year == 2016:
            self.tune_module = 'Pythia8CUEP8M1Settings_cfi'
            self.tune_block = 'pythia8CUEP8M1SettingsBlock'
            self.pythia_settings = 'pythia8CUEP8M1Settings'
        else:
            self.tune_module = 'MCTunes2017.PythiaCP5Settings_cfi'
            self.tune_block = 'pythia8CP5SettingsBlock'
            self.pythia_settings = 'pythia8CP5Settings'

    def write_fragment(self):
        """ Actually write the gen fragment """
        self.out_file = os.path.join(self.GS_dir, "{}_GS_fragment.py".format(self.model_name))
        f = open(self.out_file, "w")

        f.write("""import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.{tune_module} import *
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
        {tune_block},
        pythia8aMCatNLOSettingsBlock,
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off', # if 'on', merging parameters are set according to LHE file
            'JetMatching:scheme = 1', # 1 = scheme inspired by Madgraph matching code
            'JetMatching:merge = on', # master switch to activate parton-jet matching. when off, all external events accepted
            'JetMatching:jetAlgorithm = 2', # 2 = SlowJet clustering
            'JetMatching:etaJetMax = 5.', # max eta of any jet
            'JetMatching:coneRadius = 1.0', # gives the jet R parameter
            'JetMatching:slowJetPower = 1', # -1 = anti-kT algo, 1 = kT algo. Only kT w/ SlowJet is supported for MadGraph-style matching
            'JetMatching:qCut = 125.', # this is the actual merging scale. should be roughly equal to xqcut in MadGraph
            'JetMatching:nJetMax = 2', # number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', # off for MLM matching, turn on for shower-kT matching
            ),
""".format(cross_section=self.x_sec, tune_block=self.tune_block, tune_module=self.tune_module))

        f.write("""
        processParameters = cms.vstring(""")

        if self.process_type == 's-channel':
            f.write("""
            '4900023:m0 = {m_med:g}', # explicitly stating Z' mass in case it's not picked up properly by Pythia
            '4900023:mMin = {m_med_min:g}',
            '4900023:mMax = {m_med_max:g}',
            '4900023:mWidth = 0.01',
            '4900023:oneChannel = 1 0.982 102 4900101 -4900101', # explicitly stating Z' to dark quarks in case it's not picked up properly by Pythia
            '4900023:addChannel = 1 0.003 102 1 -1', # including small branching ratios to SM quarks for realism
            '4900023:addChannel = 1 0.003 102 2 -2',
            '4900023:addChannel = 1 0.003 102 3 -3',
            '4900023:addChannel = 1 0.003 102 4 -4',
            '4900023:addChannel = 1 0.003 102 5 -5',
            '4900023:addChannel = 1 0.003 102 6 -6',
            # decouple t-channel mediators
#            '4900001:m0 = 50000',
#            '4900002:m0 = 50000',
#            '4900003:m0 = 50000',
#            '4900004:m0 = 50000',
#            '4900005:m0 = 50000',
#            '4900006:m0 = 50000',
#            '4900011:m0 = 50000',
#            '4900012:m0 = 50000',
#            '4900013:m0 = 50000',
#            '4900014:m0 = 50000',
#            '4900015:m0 = 50000',
#            '4900016:m0 = 50000',""".format(m_med=self.m_med, m_med_min=self.m_med-1, m_med_max=self.m_med+1)
            )

        elif self.process_type == 't-channel':
            bifunds = [4900001, 4900002, 4900003, 4900004, 4900005, 4900006]
            f.write("""
            # parameters for bifundamental mediators
            # (keep default flavor-diagonal couplings)
            """)
            for bifund in bifunds:
                f.write("""
            '{bifund:d}:m0 = {m_med:g}'.format(bifund,self.mMediator),
            '{m_med_min:d}:mMin = {:g}'.format(bifund,self.mMin),
            '{m_med_max:d}:mMax = {:g}'.format(bifund,self.mMax),
            '{bifund:d}:mWidth = 0.01'.format(bifund),""".format(bifund=bifund, m_med=self.m_med, m_med_min=self.m_med-1, m_med_max=self.m_med+1)
                )
            f.write("""
            # Decouple s-channel particles
#            '4900011:m0 = 50000',
#            '4900012:m0 = 50000',
#            '4900013:m0 = 50000',
#            '4900014:m0 = 50000',
#            '4900015:m0 = 50000',
#            '4900016:m0 = 50000',
#            '4900023:m0 = 50000',
            # Pythia can only generate pair prod of bifundamental
            'HiddenValley:gg2DvDvbar = on',
            'HiddenValley:gg2UvUvbar = on',
            'HiddenValley:gg2SvSvbar = on',
            'HiddenValley:gg2CvCvbar = on',
            'HiddenValley:gg2BvBvbar = on',
            'HiddenValley:gg2TvTvbar = on',
            'HiddenValley:qqbar2DvDvbar = on',
            'HiddenValley:qqbar2UvUvbar = on',
            'HiddenValley:qqbar2SvSvbar = on',
            'HiddenValley:qqbar2CvCvbar = on',
            'HiddenValley:qqbar2BvBvbar = on',
            'HiddenValley:qqbar2TvTvbar = on',
""")

        remain_br = self.remaining_br_democratic(5)
        f.write("""
            '4900101:m0 = {m_dq}', # explicitly stating dark quark mass in case it's not picked up properly by Pythia
            '4900113:m0 = {m_dmeson}', # Dark meson mass. PDGID corresponds to rhovDiag HV spin-1 meson that can decay into SM particles
            '51:m0 = {m_dmatter}', # Stable dark particle mass. PDGID corresponds to spin-0 dark matter
            '51:isResonance = false',
            '4900113:oneChannel = 1 {r_inv} 51 -51', # Dark meson decay into stable dark particles with branching fraction r_inv
            '4900113:addChannel = 1 {remain_br} 91 1 -1', # Dark meson decay into SM quarks
            '4900113:addChannel = 1 {remain_br} 91 2 -2',
            '4900113:addChannel = 1 {remain_br} 91 3 -3',
            '4900113:addChannel = 1 {remain_br} 91 4 -4',
            '4900113:addChannel = 1 {remain_br} 91 5 -5',
""".format(m_dq=self.m_d, m_dmeson=self.m_dark_meson, m_dmatter=self.m_dark_stable, r_inv=self.r_inv, remain_br=remain_br))

        if self.n_f == 2:
            f.write(self.get_extra_decays())
        f.write("""
            'HiddenValley:probVector = {prob_vector}', # Ratio of number of vector mesons over scalar meson
            #'HiddenValley:ffbar2Zv = on', # Production of f fbar -> Zv (4900023). It works only in the case of narrow width approx
            'HiddenValley:fragment = on', # Enable hidden valley fragmentation
            'HiddenValley:Ngauge = 2', # As dark sector is SU(2)
            #'HiddenValley:spinFv = 0', # Spin of the HV partners of the SM fermions
            'HiddenValley:FSR = on', # Enable final-state shower of HV gammav
            #'HiddenValley:NBFlavRun = 0', # Number of bosonic flavor for running
            #'HiddenValley:NFFlavRun = 2', # Number of fermionic flavor for running
            'HiddenValley:alphaOrder = 1', # Order at which running coupling runs
            'HiddenValley:Lambda = {Lambda_dark}', # Dark confinement scale
            'HiddenValley:nFlav = {nFlav:.0f}', # This dictates what kind of hadrons come out of the shower. If nFlav = 2, for example, there will be many different flavor of hadrons
            'HiddenValley:pTminFSR = {pTminFSR:.2f}', # Cut-off for the showering, should be roughly confinement scale
            #'TimeShower:nPartonsInBorn = 2', # Number of coloured particles (before resonance decays) in born matrix element
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    '{pythia_settings}',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    'JetMatchingParameters',
                                    )
    )
)
""".format(prob_vector=0.0 if self.n_f == 1 else 0.75, Lambda_dark=self.Lambda_d, nFlav=self.n_f, pTminFSR=1.1*self.Lambda_d, pythia_settings=self.pythia_settings))

        f.write(self.insert_filters())
        f.close()

    def get_extra_decays(self):
        """ Compile string to include extra dark mesons and their decays, depending on value of n_f """
        if self.n_f == 2:
            ret = """
            '4900111:m0 = {m_dmeson}', # Dark meson mass. PDGID corresponds to pivDiag HV spin-0 meson that can decay into SM particles
            '4900211:m0 = {m_dmeson}', # Dark meson mass. PDGID corresponds to pivUp HV spin-0 meson that is stable and invisible by default
            '4900213:m0 = {m_dmeson}', # Dark meson mass. PDGID corresponds to rhovUp HV spin-1 meson that is stable and invisible by default
            '53:m0 = {m_dmatter}', # Stable dark particle mass. PDGID corresponds to spin-1 dark matter
            '53:isResonance = false',
            '4900111:oneChannel = 1 {r_inv} 0 51 -51',
            '4900111:addChannel = 1 {remain_BR_c:.5f} 91 4 -4', # Dark meson decay into c quarks with BR set by running mass
            '4900111:addChannel = 1 {remain_BR_b:.5f} 91 5 -5', # Dark meson decay into b quarks with BR set by running mass
            '4900211:oneChannel = 1 {r_inv} 0 51 -51',
            '4900211:addChannel = 1 {remain_BR_c:.5f} 91 4 -4',
            '4900211:addChannel = 1 {remain_BR_b:.5f} 91 5 -5',
            '4900213:oneChannel = 1 {r_inv} 0 53 -53', # Dark meson decay into stable dark particles with branching fraction r_inv
            '4900213:addChannel = 1 {remain_BR_democ} 91 1 -1',
            '4900213:addChannel = 1 {remain_BR_democ} 91 2 -2',
            '4900213:addChannel = 1 {remain_BR_democ} 91 3 -3',
            '4900213:addChannel = 1 {remain_BR_democ} 91 4 -4',
            '4900213:addChannel = 1 {remain_BR_democ} 91 5 -5',
""".format(m_dmeson=self.m_dark_meson, m_dmatter=self.m_dark_stable, r_inv=self.r_inv, remain_BR_democ=self.remaining_br_democratic(5),
           remain_BR_c=self.remaining_br_mass_insertion(quark_id=4), remain_BR_b=self.remaining_br_mass_insertion(quark_id=5))
        elif self.n_f == 1:
            ret = "\n"
        else:
            raise ValueError("The value of n_f = {} specified is not allowed. Please choose either n_f = 1 or n_f = 2".format(self.n_f))

        print(Fore.MAGENTA + "Extra decays added to gen fragment")
        return ret

    def insert_filters(self):
        """ Include Z2 symmmetry filter (enforce pair production of stable dark particles)
        and dark quark filter (reject events where Z' decays directly to SM particles) """
        ret = """
darkhadronZ2filter = cms.EDFilter("MCParticleModuloFilter",
    moduleLabel = cms.InputTag("generator"{smear}),
    absID = cms.bool(True),
    multipleOf = cms.uint32({two_n_dmatter:.0f}),  # 2x number of stable dark particles
    particleIDs = cms.vint32(51{extra_dmatter}),  # PDGIDs of stable dark particles
)

darkquarkFilter = cms.EDFilter("MCParticleModuloFilter",
    status = cms.int32(23),
    min = cms.uint32(2),
    moduleLabel = cms.InputTag("generator"{smear}),
    absID = cms.bool(True),
    multipleOf = cms.uint32(2),
    particleIDs = cms.vint32(4900101),  # PDGID of dark quark
)
""".format(two_n_dmatter=2*self.n_f, extra_dmatter=', 53' if self.n_f == 2 else '', smear='' if self.year == 2016 else ', "unsmeared"')

        print(Fore.MAGENTA + "Extra filters added to gen fragment")
        return ret
