""" Calculates quantities required in semi-visible jet models """
import numpy as np


def calc_alpha_d(n_c, n_f, Lambda_d):
    b_param = calc_b_param(n_c, n_f)
    alpha_d = -2.0*np.pi / (b_param * np.log(Lambda_d/1000.0))
    return alpha_d


def calc_lambda_d(n_c, n_f, alpha_d):
    b_param = calc_b_param(n_c, n_f)
    Lambda_d = 1000.0 * np.exp(-2.0*np.pi / (alpha_d*b_param))
    return Lambda_d


def calc_b_param(n_c, n_f):
    b_param = (11.0/3.0)*float(n_c) - (2.0/3.0)*float(n_f)
    return b_param


def calc_lambda_d_from_str(n_c, n_f, alpha_d, m_dh):
    if not isinstance(alpha_d, str):
        raise TypeError("alpha_d must be a string")
    sfs = {
        "low": 0.5,
        "peak": 1.,
        "high": 1.5,
        "v_high": 2.,
    }
    if not any(alpha_d == x for x in sfs.keys()):
        raise ValueError("alpha_d must equal one of the following: {}".format(sfs.keys()))

    Lambda_d_peak = 3.2 * np.power(m_dh, 0.8)
    if alpha_d == "peak":
        Lambda_d = Lambda_d_peak
    else:
        alpha_d_peak = calc_alpha_d(n_c, n_f, Lambda_d_peak)
        a_d = sfs[alpha_d] * alpha_d_peak
        Lambda_d = calc_lambda_d(n_c, n_f, a_d)
    return Lambda_d
