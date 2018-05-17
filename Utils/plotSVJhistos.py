#!/usr/bin/python 
from ROOT import TFile, TCanvas, gStyle, TLatex, TLegend, TH1F
import os
import CMS_lumi
from progressbar import ProgressBar, Percentage, Bar, ETA

# Define global variables
baseDir = "/afs/cern.ch/work/e/ebhal/Semi_visible_jets_Condor/v3"
models = ["DMsimp_SVJ_s_spin1_mZp-1000_mDQ-10", "DMsimp_SVJ_t_mPhi-1000_mDQ-10"]
rootColours = [4, 2, 3, 1, 6, 5, 7, 8, 9] # length needs to be >= len(models)

# Add CMS-style plot header
def addPlotTitle(canvas):
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.lumi_sqrtS = "13 TeV"
    CMS_lumi.CMS_lumi(canvas, 4, 0)


# Set plot aesthetics
def setTheGoodStuff(histo, model, index, xTitle, legend):
    legend.AddEntry(histo, model, 'l')
    histo.SetLineColor( rootColours[index] )
    histo.GetXaxis().SetTitle(xTitle)
    histo.GetXaxis().SetTitleOffset(1.15)
    legend.Draw()    


# Plot histograms, then save
def drawIndivHistos(model, histo, canvas, legend, xTitle, fileSuffix, index=0):
    setTheGoodStuff(histo, model, index, xTitle, legend)
    histo.Draw()
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/"+model+"_"+fileSuffix+".pdf")
    legend.Clear()


# Run over all the histograms in an array and plot together, then save
def drawMultipleHistos(histoArray, canvas, legend, xTitle, fileSuffix, modelsArray=models):
    for i, hist in enumerate(histoArray):
        setTheGoodStuff(histoArray[i], modelsArray[i], i, xTitle, legend)
        if i == 0:
            histoArray[i].Draw()
        else:
            histoArray[i].Draw("SAME")
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/all_"+fileSuffix+".pdf")
    legend.Clear()


def main():
    """
    Simply plot semi-visible jets histograms stored in nanoAOD files for a quick look at distributions
    """

    # Initialise the canvas and set aesthetics
    canv = TCanvas("canv", "canv", 600, 600)
    canv.SetLogy()
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)

    # Initialise legend and set colours
    myLeg = TLegend(0.55, 0.8, 0.9, 0.9)
    myLeg.SetTextSize(0.015)

    # Initialise histogram arrays
    nJetHist = [None] * len(models)
    jetPtHist = [None] * len(models)
    leadJetPtHist = [None] * len(models)
    metPtHist = [None] * len(models)

    # x-axis labels for plots
    nJetLabel = "n_{jet}"
    jetPtLabel = "p_{T}^{jet}"
    leadJetPtLabel = "p_{T}^{j_{1}}"
    metPtLabel = "E_{T}^{miss}"

    # Initialise histograms here so I can use them later
    for i, model in enumerate(models):
        nJetHist[i] = TH1F("nJet"+model, "nJet dist "+model, 30, 0, 29)
        jetPtHist[i] = TH1F("jetPt"+model, "Jet pT dist "+model, 30, 0, 3000)
        leadJetPtHist[i] = TH1F("leadJetPt"+model, "Lead jet pT dist "+model, 30, 0, 3000)
        metPtHist[i] = TH1F("met"+model, "MET dist "+model, 30, 0, 3000)
    

    # Open root files, then draw individual histograms
    for i, model in enumerate(models):
        print "Running over model {0}/{1}.".format(i+1, len(models))
        rootFile = os.path.join(baseDir, model+"_nanoAOD_final.root")
        openFile = TFile(rootFile)
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

            pbar.update(entry+1)
        
        pbar.finish()

        # Draw histogram(s) and save
        drawIndivHistos(model, nJetHist[i], canv, myLeg, nJetLabel, "nJet", index=i)
        drawIndivHistos(model, jetPtHist[i], canv, myLeg, jetPtLabel, "jetPT", index=i)
        drawIndivHistos(model, leadJetPtHist[i], canv, myLeg, leadJetPtLabel, "leadJetPT", index=i)
        drawIndivHistos(model, metPtHist[i], canv, myLeg, metPtLabel, "MET", index=i)
    

    # Draw histograms for different models overlaid
    drawMultipleHistos(nJetHist, canv, myLeg, nJetLabel, "nJet")
    drawMultipleHistos(jetPtHist, canv, myLeg, jetPtLabel, "jetPT")
    drawMultipleHistos(leadJetPtHist, canv, myLeg, leadJetPtLabel, "leadJetPT")
    drawMultipleHistos(metPtHist, canv, myLeg, metPtLabel, "MET")


if __name__ == '__main__':
    main()
