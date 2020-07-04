from __future__ import print_function
import matplotlib
matplotlib.use("Agg")  # Agg backend to work around any problems with Tkinter
import matplotlib.pyplot as plt
import numpy as np

from calc_dark_params import calc_lambda_d_from_str as cld


plt.rcParams["figure.figsize"] = [8, 6]
ax = plt.gca()

alpha_dark = ["v_low", "low", "peak", "high", "v_high"]
m_dark = np.array([1., 2., 3., 4., 5., 6., 8., 10., 15., 20., 30., 40., 50., 60., 70., 80., 90., 100])  # dark hadron mass (GeV)

n_c = 2
n_f = 2

max_lam_dark = []

# Plot Lambda_dark vs m_dark for each value of alpha_dark given
for a_dark in alpha_dark:
    lambda_dark = cld(n_c, n_f, a_dark, m_dark)
    ax.plot(m_dark, lambda_dark, label=r"$\alpha_{\mathrm{dark}}$ = " + a_dark)
    max_lam_dark.append(lambda_dark.max())

# Get max Lambda_dark in plot for tuning y-axis range
max_lam_dark = np.array(max_lam_dark).max()

# Set plotting aesthetics
ax_label_fontsize = 16
ax.set_xlabel(r"$m_{\mathrm{dark}}$ [GeV]", fontsize=ax_label_fontsize)
ax.set_ylabel(r"$\Lambda_{\mathrm{dark}}$ [GeV]", fontsize=ax_label_fontsize)
ax.set_xlim(0, m_dark.max())
ax.set_ylim(0, max_lam_dark)
ax.legend(loc="upper left", prop={'size': ax_label_fontsize - 4})
ax.grid(True)
ax.set_axisbelow(True)

# Reduce padding around plot, then save
top_right_margin = 0.97
bottom_left_margin = 0.10
plt.subplots_adjust(top=top_right_margin, right=top_right_margin, left=bottom_left_margin, bottom=bottom_left_margin)
out_file = "lambda_dark_vs_mDark.pdf"
plt.savefig(out_file, dpi=200)
print("Saving figure as", out_file)

