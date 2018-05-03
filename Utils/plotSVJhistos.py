#!/usr/bin/python 
from ROOT import TFile, TCanvas, TLegend, gStyle, TLatex
import os
import CMS_lumi

def addPlotTitle(canvas):
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.lumi_sqrtS = "13 TeV"
    CMS_lumi.CMS_lumi(canvas, 4, 0)

#    textCMS = TLatex(0.25,0.96,"  Preliminary ")
#    textCMS.SetNDC()
#    textCMS.SetTextAlign(13)
#    textCMS.SetTextFont(52)
#    textCMS.SetTextSize(0.033)
#    textCMS.Draw()
#    canvas.textCMS = textCMS

baseDir = "/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor_NewWorkflow/output"
models = ["DMsimp_SVJ_s_spin1_mZp-1000_mDQ-10", "DMsimp_SVJ_t_mPhi-1000_mDQ-10"]

# Histograms to draw
histos = ["nJet", "Jet_pt", "Jet_pt[0]", "MET_pt"]

# Initialise the canvas and legend, and set aesthetics
canv = TCanvas("canv", "canv", 600, 600)
canv.SetLogy()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
#myLeg = TLegend(0.65, 0.7, 0.9, 0.9)

# Open root files, then draw and save histograms
for model in models:
    rootFile = os.path.join(baseDir, model+"_nanoAOD_final.root")
    openFile = TFile(rootFile)
    tree = openFile.Get("Events")

    for i in xrange( len(histos) ):
        tree.Draw(histos[i])
        addPlotTitle(canv)
        #myLeg.Draw()
        canv.SaveAs("./Plots/"+model+"_"+histos[i]+".pdf")
    


