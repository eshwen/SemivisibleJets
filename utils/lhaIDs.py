"""
IDs for LHAPDF PDF sets (https://lhapdf.hepforge.org/pdfsets).
For 2016/17/18 UL, PDF set with ID 325300 is recommended (https://monte-carlo-production-tools.gitbook.io/project/mccontact/info-for-mc-production-for-ultra-legacy-campaigns-2016-2017-2018).
In this case, MadGraph5 v2.6.1 is recommended (version specified in external/genproductions/bin/MadGraph5_aMCatNLO/gridpack_generation.sh).
For "normal" 2016 (2017/18), PDF set with ID 292000 (320900) should be used. Though, there are reports that 320900 can generate large negative weights and this needs to be investigated further for this model.
"""
lhaIDs = {
    2016: 247000,  # corresponds to NNPDF2.3 LO (NNPDF23_lo_as_0130_qed, for CUETP8M1)
    2017: 315200,  # corresponds to NNPDF3.1 LO (NNPDF31_lo_as_0130)
    2018: 315200,  # in CMS, generation is the same for 2017 and 2018
}
