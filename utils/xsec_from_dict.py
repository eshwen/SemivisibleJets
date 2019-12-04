from load_yaml_config import load_yaml_config
import sys


def xsec_from_dict(in_file, m_med):
    """
    Get cross section from yaml dictionary
    """
    xsec_dict = load_yaml_config(in_file, quiet=True)
    try:
        x_sec = xsec_dict[m_med]
    except KeyError:
        if m_med < min(xsec_dict.keys()) or m_med > max(xsec_dict.keys()):
            raise ValueError("m_med = {} is outside the range of the dictionary in '{}'".format(m_med, in_file))
        else:
            # Cross sections given in increments of 100 GeV. Round m_med if required
            x_sec = xsec_dict[int(round(m_med, -2))]
    return x_sec
