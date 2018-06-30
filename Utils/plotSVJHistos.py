#!/usr/bin/python 
import CMS_lumi
import sys
try:
    from colorama import Fore, init
except ImportError:
    sys.exit('Please source the setup script first.')
from math import pi
import os
from progressbar import ProgressBar, Percentage, Bar, ETA
import re
from ROOT import TFile, TCanvas, gStyle, TLatex, TLegend, TH1F


# Define global variables

# Files to run over
baseDir = '/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor_v6/output/'
files = [ baseDir + 'DMsimp_SVJ_s_spin1_mZp-1000_mDQ-20_rinv-0p3_nanoAOD_final_withMatching_Esh_settings.root',
          baseDir + 'step4_MINIAOD_mZp-1000_mDQ-20_rinv-0p3_alpha-0.2_n-1000_nanoAOD_final.root',
          ]

# Models, from which to extract info
models = []
for file in files:
    models.append( os.path.basename(file.replace('.root', '') ) )

rootColours = [4, 2, 3, 1, 6, 5, 7, 8, 9] # length needs to be >= len(models)
legModelNames = []


# Write strings to be included in legend
for i, model in enumerate(models):
    m_d = re.search("(?<=mDQ-)[0-9]*", model).group(0)
    r_inv = re.search('(?<=rinv-)[0-9]*p[0-9]*',model).group(0).replace('p', '.')

    if 'mZp' in model:
        mZp = re.search("(?<=mZp-)[0-9]*", model).group(0)
        legModel = "#splitline{#it{s}-channel}"
        legModel += "{#it{m_{Z'}} = %s, " % mZp

    elif 'mPhi' in model:
        mPhi = re.search("(?<=mPhi-)[0-9]*", model).group(0)
        legModel = "#splitline{#it{t}-channel}"
        legModel += "{#it{m}_{#Phi} = %s, " % mPhi

    legModel += "#it{m_{d}} = %s, #it{r}_{inv.} = %s}" % (m_d, r_inv)
    legModelNames.append(legModel)


# Reset terminal colours after print statement in which they've changed
init(autoreset=True)


# Add CMS-style plot header
def addPlotTitle(canvas):
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.lumi_sqrtS = "13 TeV"
    CMS_lumi.CMS_lumi(canvas, 4, 0)


# Set plot aesthetics
def setTheGoodStuff(histo, model, index, xTitle, legend):
    legend.AddEntry(histo, legModelNames[index], 'l')
    histo.SetLineColor( rootColours[index] )
    histo.GetXaxis().SetTitle(xTitle)
    histo.GetXaxis().SetTitleOffset(1.15)
    histo.GetYaxis().SetTitle("entries / nEvents")
    legend.SetFillStyle(0)
    legend.Draw()    


# Plot histograms, then save
def drawIndivHistos(model, histo, canvas, legend, xTitle, fileSuffix, index=0):
    setTheGoodStuff(histo, model, index, xTitle, legend)
    histo.Draw("HIST")
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/"+model+"_"+fileSuffix+".pdf")
    legend.Clear()


# Run over all the histograms in an array and plot together, then save
def drawMultipleHistos(histoArray, canvas, legend, xTitle, fileSuffix, modelsArray=models):
    for i, hist in enumerate(histoArray):
        setTheGoodStuff(histoArray[i], modelsArray[i], i, xTitle, legend)
        if i == 0:
            histoArray[i].Draw("HIST")
        else:
            histoArray[i].Draw("HIST SAME")
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/all_"+fileSuffix+".pdf")
    legend.Clear()


def main():
    """
    Simply plot semi-visible jets histograms stored in nanoAOD files for a quick look at distributions
    """

    if not os.path.exists( os.path.join(os.getcwd(), 'Plots') ):
        os.mkdir('Plots')

    # Initialise the canvas and set aesthetics
    canv = TCanvas("canv", "canv", 800, 600)
    canv.SetLogy()
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)

    # Initialise legend and set colours
    leg_height = len(models) * 0.06 # make y-length of legend dependent on n_models
    myLeg = TLegend(0.6, 0.9 - leg_height, 0.9, 0.9)
    myLeg.SetTextSize(0.02)

    # Initialise histogram arrays
    nJetHist = [None] * len(models)
    jetPtHist = [None] * len(models)
    leadJetPtHist = [None] * len(models)
    metPtHist = [None] * len(models)
    dPhiJJHist = [None] * len(models)

    # x-axis labels for plots
    nJetLabel = "#it{n}_{jet}"
    jetPtLabel = "#it{p}_{T}^{jet}"
    leadJetPtLabel = "#it{p}_{T}^{j_{1}}"
    metPtLabel = "#it{E}_{T}^{miss}"
    dPhiJJLabel = "#Delta#it{#phi}_{j_{1} j_{2}}"

    # Initialise histograms here so I can use them later
    for i, model in enumerate(models):
        nJetHist[i] = TH1F("nJet"+model, "nJet dist "+model, 30, 0, 29)
        jetPtHist[i] = TH1F("jetPt"+model, "Jet pT dist "+model, 30, 0, 3000)
        leadJetPtHist[i] = TH1F("leadJetPt"+model, "Lead jet pT dist "+model, 30, 0, 3000)
        metPtHist[i] = TH1F("met"+model, "MET dist "+model, 30, 0, 3000)
        dPhiJJHist[i] = TH1F("dPhijj"+model, "DPhi dist "+model, 20, -1*(pi+0.1), pi+0.1)
    

    # Open root files, then draw individual histograms
    for i, model in enumerate(models):
        print Fore.MAGENTA + "Running over model {0}/{1}.".format(i+1, len(models))
        openFile = TFile(files[i])
        tree = openFile.Get("Events")
        nEntries = tree.GetEntries()

        # Initialise progress bar
        widgets = [Percentage(), Bar('>'), ETA()]
        pbar = ProgressBar(widgets = widgets, maxval = nEntries).start()    

        for entry in xrange(nEntries):
            treeEntry = tree.GetEntry(entry)
            nJetHist[i].Fill(tree.nJet)
        
            for jet in xrange( len(tree.Jet_pt) ):
                jetPtHist[i].Fill(tree.Jet_pt[jet])

            if len(tree.Jet_pt) > 0: leadJetPtHist[i].Fill(tree.Jet_pt[0])
            metPtHist[i].Fill(tree.MET_pt)

            if len(tree.Jet_phi) >= 2:
                deltaPhi = tree.Jet_phi[0] - tree.Jet_phi[1]
                dPhiJJHist[i].Fill(deltaPhi)        

            pbar.update(entry+1)
        
        pbar.finish()

        # Normalise histograms
        nJetHist[i].Scale(1./nEntries)
        jetPtHist[i].Scale(1./nEntries)
        leadJetPtHist[i].Scale(1./nEntries)
        metPtHist[i].Scale(1./nEntries)
        dPhiJJHist[i].Scale(1./nEntries)

        # Draw individual histograms and save
        drawIndivHistos(model, nJetHist[i], canv, myLeg, nJetLabel, "nJet", index=i)
        drawIndivHistos(model, jetPtHist[i], canv, myLeg, jetPtLabel, "jetPT", index=i)
        drawIndivHistos(model, leadJetPtHist[i], canv, myLeg, leadJetPtLabel, "leadJetPT", index=i)
        drawIndivHistos(model, metPtHist[i], canv, myLeg, metPtLabel, "MET", index=i)
        drawIndivHistos(model, dPhiJJHist[i], canv, myLeg, dPhiJJLabel, "dPhi", index=i)
    

    # Draw histograms for different models overlaid
    drawMultipleHistos(nJetHist, canv, myLeg, nJetLabel, "nJet")
    drawMultipleHistos(jetPtHist, canv, myLeg, jetPtLabel, "jetPT")
    drawMultipleHistos(leadJetPtHist, canv, myLeg, leadJetPtLabel, "leadJetPT")
    drawMultipleHistos(metPtHist, canv, myLeg, metPtLabel, "MET")
    drawMultipleHistos(dPhiJJHist, canv, myLeg, dPhiJJLabel, "dPhi")


if __name__ == '__main__':
    main()
