import math
# Stolen from https://github.com/kpedro88/SVJProduction/blob/master/python/svjHelper.py
# follows Ellis, Stirling, Webber calculations


class MassRunner(object):
    """
    Calculate running quark masses
    """
    def __init__(self, m_q, nfq, scale, n_f):
        self.Lambda = 0.218  # QCD scale in GeV
        self.m_run = self.run(m_q,  # quark mass
                              nfq,  # number of quark flavours to consider
                              scale,  # dark hadron mass
                              n_f)  # number of dark flavours

    # RG terms, assuming n_c = 3 (QCD)
    def c(self):
        return 1./math.pi

    def cp(self, n_f):
        return (303. - 10.*n_f) / (72. * math.pi)

    def b(self, n_f):
        return (33. - 2.*n_f) / (12. * math.pi)

    def bp(self, n_f):
        return (153. - 19.*n_f) / (2. * math.pi * (33. - 2.*n_f))

    def alphaS(self, Q, n_f):
        return 1. / (self.b(n_f) * math.log(Q**2 / self.Lambda**2))

    # derived terms
    def cb(self, n_f):
        return 12. / (33. - 2.*n_f)

    def one_c_cp_bp_b(self, n_f):
        return 1. + self.cb(n_f) * (self.cp(n_f) - self.bp(n_f))

    def mhat(self, m_q, nfq):
        """ constant of normalization """
        return m_q / math.pow(self.alphaS(m_q, nfq), self.cb(nfq)) / self.one_c_cp_bp_b(nfq)

    def m(self, m_q, nfq, Q, n_f):
        """ mass formula """
        # temporary hack: exclude quarks w/ mq < Lambda
        alphaq = self.alphaS(m_q, nfq)
        if alphaq < 0:
            return 0
        else:
            return self.mhat(m_q, nfq) * math.pow(self.alphaS(Q, n_f), self.cb(n_f)) * self.one_c_cp_bp_b(n_f)

    def run(self, m_q, nfq, scale, n_f):
        """ Operation. Run to specified scale and n_f """
        return self.m(m_q, nfq, scale, n_f)
