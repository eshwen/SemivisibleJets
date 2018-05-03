#!/usr/bin/python 
from ROOT import TFile, TCanvas, gStyle, TLatex
import os
import CMS_lumi

# Simply plot semi-visible jets histograms stored in nanoAOD files for a quick look at distributions

def addPlotTitle(canvas):
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.lumi_sqrtS = "13 TeV"
    CMS_lumi.CMS_lumi(canvas, 4, 0)


baseDir = "/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor_NewWorkflow/output"
models = ["DMsimp_SVJ_s_spin1_mZp-1000_mDQ-10", "DMsimp_SVJ_t_mPhi-1000_mDQ-10"]

# Histograms to draw
histos = ["nJet", "Jet_pt", "Jet_pt[0]", "MET_pt"]

# Initialise the canvas and set aesthetics
canv = TCanvas("canv", "canv", 600, 600)
canv.SetLogy()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

rootColours = [4, 2, 3]
# Open root files, then draw and save histograms
for model in models:
    rootFile = os.path.join(baseDir, model+"_nanoAOD_final.root")
    openFile = TFile(rootFile)
    tree = openFile.Get("Events")
    canv.cd()

    for i in xrange( len(histos) ):
        tree.Draw(histos[i])
        addPlotTitle(canv)
        canv.SaveAs("./Plots/"+model+"_"+histos[i]+".pdf")
 
