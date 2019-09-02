""" Calculates quantities required in semi-visible jet models """
import math


def calc_alpha_d(n_c, n_f, Lambda_d):
    b_param = calc_b_param(n_c, n_f)
    alpha_d = -2.0*math.pi / (b_param * math.log(Lambda_d/1000.0))
    return alpha_d


def calc_lambda_d(n_c, n_f, alpha_d):
    b_param = calc_b_param(n_c, n_f)
    Lambda_d = 1000.0 * math.exp(-2.0*math.pi / (alpha_d*b_param))
    return Lambda_d


def calc_b_param(n_c, n_f):
    b_param = (11.0/3.0)*float(n_c) - (2.0/3.0)*float(n_f)
    return b_param


def calc_lambda_d_from_str(n_c, n_f, alpha_d, m_dh):
    if not isinstance(alpha_d, str):
        raise TypeError("alpha_d must be a string")
    elif not any(alpha_d == x for x in ['peak', 'low', 'high']):
        raise ValueError("alpha_d must equal 'peak', 'low', or 'high'")
    else:
        Lambda_d_peak = 3.2 * math.pow(m_dh, 0.8)
        if alpha_d == "peak":
            Lambda_d = Lambda_d_peak
        else:
            alpha_d_peak = calc_alpha_d(n_c, n_f, Lambda_d_peak)
            if alpha_d == "low":
                a_d = 0.5 * alpha_d_peak
            elif alpha_d == "high":
                a_d = 1.5 * alpha_d_peak
            Lambda_d = calc_lambda_d(n_c, n_f, a_d)
        return Lambda_d
