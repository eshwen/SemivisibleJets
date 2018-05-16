#!/usr/bin/python 
from ROOT import TFile, TCanvas, gStyle, TLatex, TLegend, TH1F, gDirectory
import os
import CMS_lumi
from progressbar import ProgressBar, Percentage, Bar, ETA

# Simply plot semi-visible jets histograms stored in nanoAOD files for a quick look at distributions


# Add CMS-style plot header
def addPlotTitle(canvas):
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.lumi_sqrtS = "13 TeV"
    CMS_lumi.CMS_lumi(canvas, 4, 0)


# Plot histograms, add labels and legend, then save
def drawIndivHistos(model, histo, canvas, legend, xTitle, fileSuffix, index=0, same=False):
    histo.SetLineColor( rootColours[index] )
    histo.GetXaxis().SetTitle(xTitle)
    if same == False:
        histo.Draw()
    else:
        histo.Draw("SAME")
    legend.Draw()
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/"+model+"_"+fileSuffix+".pdf")


baseDir = "/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor/v3"
models = ["DMsimp_SVJ_s_spin1_mZp-1000_mDQ-10", "DMsimp_SVJ_t_mPhi-1000_mDQ-10"]

# Initialise the canvas and set aesthetics
canv = TCanvas("canv", "canv", 600, 600)
canv.SetLogy()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

# Initialise legend and set colours
myLeg = TLegend(0.55, 0.8, 0.9, 0.9)
myLeg.SetTextSize(0.015)
rootColours = [4, 2, 3, 1, 6, 5, 7, 8, 9] # length needs to be >= len(models)

nJetHist = [None] * len(models)
jetPtHist = [None] * len(models)
leadJetPtHist = [None] * len(models)
metPtHist = [None] * len(models)

for i, model in enumerate(models):
    # Initialise histograms
    nJetHist[i] = TH1F("nJet"+model, "nJet dist for "+model, 30, 0, 29)
    jetPtHist[i] = TH1F("jetPt"+model, "Jet pT dist for "+model, 50, 0, 2000)
    leadJetPtHist[i] = TH1F("leadJetPt"+model, "Lead jet pT dist for "+model, 50, 0, 2000)
    metPtHist[i] = TH1F("met"+model, "MET dist for model "+model, 50, 0, 2000)
    

# Open root files, then draw individual histograms
for i, model in enumerate(models):
    rootFile = os.path.join(baseDir, model+"_nanoAOD_final.root")
    openFile = TFile(rootFile)
    tree = openFile.Get("Events")
    nEntries = tree.GetEntries()
#    canv.cd()

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

        pbar.update(entry+1)
        

    pbar.finish()

    # Add a single legend entry per model
    myLeg.AddEntry(nJetHist[i], model, 'l')

    # Draw histogram(s) and save
    drawIndivHistos(model, nJetHist[i], canv, myLeg, "nJet", "nJet", index=i)
    drawIndivHistos(model, jetPtHist[i], canv, myLeg, "Jet pT", "jetPT", index=i)
    drawIndivHistos(model, leadJetPtHist[i], canv, myLeg, "Leading jet pT", "leadJetPT", index=i)
    drawIndivHistos(model, metPtHist[i], canv, myLeg, "MET", "MET", index=i)
    
    myLeg.Clear()

# Tidy all of the following up
for i, model in enumerate(models):
    myLeg.AddEntry(nJetHist[i], model, 'l')
    if i == 0:
        nJetHist[i].Draw()
    else:
        nJetHist[i].Draw("SAME")
    myLeg.Draw()

canv.SaveAs("./Plots/all_nJet.pdf")
myLeg.Clear()

for i, model in enumerate(models):
    myLeg.AddEntry(jetPtHist[i], model, 'l')
    if i == 0:
        jetPtHist[i].Draw()
    else:
        jetPtHist[i].Draw("SAME")
    myLeg.Draw()

canv.SaveAs("./Plots/all_jetPT.pdf")
myLeg.Clear()

for i, model in enumerate(models):
    myLeg.AddEntry(leadJetPtHist[i], model, 'l')
    if i == 0:
        leadJetPtHist[i].Draw()
    else:
        leadJetPtHist[i].Draw("SAME")
    myLeg.Draw()

canv.SaveAs("./Plots/all_leadJetPT.pdf")
myLeg.Clear()

for i, model in enumerate(models):
    myLeg.AddEntry(metPtHist[i], model, 'l')
    if i == 0:
        metPtHist[i].Draw()
    else:
        metPtHist[i].Draw("SAME")
    myLeg.Draw()

canv.SaveAs("./Plots/all_MET.pdf")
