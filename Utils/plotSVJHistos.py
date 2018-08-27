#!/usr/bin/python 
import CMS_lumi
import sys
try:
    from colorama import Fore, init
except ImportError:
    sys.exit('Please source the setup script first.')
from math import pi
import os
import argparse
import sys
try:
    from progressbar import ProgressBar, Percentage, Bar, ETA
except ImportError:
    sys.exit('Please source the setup script first.')
import re
from ROOT import TFile, TCanvas, gStyle, TLatex, TLegend, TH1F


# Reset terminal colours after print statement in which they've changed
init(autoreset=True)


parser = argparse.ArgumentParser()
parser.add_argument("file_list", type = str, default = 'file_list.txt', help = "Path to plain text file containing list of input files")
args = parser.parse_args()


# Define global variables
rootColours = [4, 2, 3, 1, 6, 5, 7, 8, 9] # length needs to be >= len(models)


class SVJModel(object):
    
    def __init__(self, name, file_path):
        self.name = name # model name
        self.file_path = file_path # path to root file
        #self.proc_type = proc_type # s-channel/t-channel

    def initialise_histos(self):
        """
        Initialise histograms for model. Each histogram's first argument (name) will be appended
        to the saved pdf, and its second argument (title) will be the used as the x-axis title.
        """
        self.nJetHist = TH1F("nJet", "#it{n}_{jet}", 30, 0, 29)
        self.allJetPtHist = TH1F("jetPT", "#it{p}_{T}^{jet}", 30, 0, 3000)
        self.leadJetPtHist = TH1F("leadJetPT", "#it{p}_{T}^{j_{1}}", 30, 0, 3000)
        self.metPtHist = TH1F("MET", "#it{E}_{T}^{miss}", 30, 0, 3000)
        self.dPhiJJHist = TH1F("dPhiJJ", "#Delta#it{#phi}_{j_{1} j_{2}}", 20, -1*(pi+0.1), pi+0.1)

    def write_legend_entry(self, name):
        """
        Write strings to be included in legend of plots
        """
        m_d = re.search("(?<=mDQ-)[0-9]*", name).group(0)
        r_inv = re.search('(?<=rinv-)[0-9]*p[0-9]*',name).group(0).replace('p', '.')
        if 'mZp' in name:
            mZp = re.search("(?<=mZp-)[0-9]*", name).group(0)
            self.legend = "#splitline{#it{s}-channel}"
            self.legend += "{#it{m_{Z'}} = %s, " % mZp
        elif 'mPhi' in name:
            mPhi = re.search("(?<=mPhi-)[0-9]*", name).group(0)
            self.legend = "#splitline{#it{t}-channel}"
            self.legend += "{#it{m}_{#Phi} = %s, " % mPhi
        self.legend += "#it{m_{d}} = %s, #it{r}_{inv.} = %s}" % (m_d, r_inv)

    def get_hist_colour(self, list_position):
        """
        Use the global list 'rootColours' to assign a colour to the model's histograms
        """
        self.hist_colour = rootColours[list_position]
        


def addPlotTitle(canvas):
    """
    Add CMS-style plot header
    """
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.lumi_sqrtS = "13 TeV"
    CMS_lumi.CMS_lumi(canvas, 4, 0)



def setCommonPlottingAttrs(model, histo, legend_frame):
    """
    Set plot aesthetics
    """
    legend_frame.AddEntry(histo, model.legend, 'l')
    histo.SetLineColor(model.hist_colour)
    histo.GetXaxis().SetTitle( histo.GetTitle() )
    histo.GetXaxis().SetTitleOffset(1.15)
    histo.GetYaxis().SetTitle("entries / nEvents")
    histo.GetYaxis().SetTitleOffset(1.10)
    legend_frame.SetFillStyle(0)
    legend_frame.Draw()



def drawIndivHistos(model, histo, canvas, legend_frame):
    """
    Plot histograms, then save
    """
    setCommonPlottingAttrs(model, histo, legend_frame)
    histo.Draw("HIST")
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/"+model.name+"_"+histo.GetName()+".pdf")
    legend_frame.Clear()



def drawMultipleHistos(histo_array, canvas, legend_frame, models_list):
    """
    Run over all the histograms in an array and plot together, then save
    """
    for i, hist in enumerate(histo_array):
        setCommonPlottingAttrs(models_list[i], hist, legend_frame)
        if i == 0:
            hist.Draw("HIST")
        else:
            hist.Draw("HIST SAME")
    addPlotTitle(canvas)
    canvas.SaveAs("./Plots/all_"+histo_array[0].GetName()+".pdf")
    legend_frame.Clear()



def main():
    """
    Simply plot semi-visible jets histograms stored in nanoAOD files for a quick look at distributions.
    User specifies a list of the files they wish to be read in, and one file corresponds to one "model",
    (i.e., a combination of semi-visible jet-specific parameters).
    """

    if not os.path.exists( os.path.join(os.getcwd(), 'Plots') ):
        os.mkdir('Plots')

    # Build list of files from input argument
    with open(args.file_list) as input_files:
        input_file_list = input_files.readlines()

    # Create list of models, each element in list contains object with all information about each model
    models = []
    for file in input_file_list:
        if file.startswith('#'):
            continue
        file = file.replace('\n', '')
        model_name = os.path.basename(file.replace('.root', '') )
        models.append( SVJModel(name=model_name, file_path=file) )

    # For each model, initialise histograms, set line colours and write legend entry
    for i, model in enumerate(models):
        model.initialise_histos()
        model.get_hist_colour(i)
        model.write_legend_entry(model.name)

    # Initialise the canvas and set aesthetics
    canv = TCanvas("canv", "canv", 800, 600)
    canv.SetLogy()
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)

    # Initialise legend and set colours
    leg_height = len(models) * 0.06 # make y-length of legend dependent on n_models
    legend_frame = TLegend(0.6, 0.9 - leg_height, 0.9, 0.9)
    legend_frame.SetTextSize(0.02)

    # Initialise histogram arrays for plotting multiple at once
    nJetHistArr = []
    allJetPtHistArr = []
    leadJetPtHistArr = []
    metPtHistArr = []
    dPhiJJHistArr = []


    # Open root files, then draw individual histograms
    for i, model in enumerate(models):
        print Fore.MAGENTA + "Running over model {0}/{1}".format(i+1, len(models))
        openFile = TFile(model.file_path)
        tree = openFile.Get("Events")
        nEvents = tree.GetEntries()

        # Initialise progress bar
        widgets = [Percentage(), Bar('>'), ETA()]
        pbar = ProgressBar(widgets = widgets, maxval = nEvents).start()

        # To count the number of events with >=2 jets
        nDiJetEvents = 0

        # Fill all histograms
        for entry in xrange(nEvents):
            treeEntry = tree.GetEntry(entry)
            model.nJetHist.Fill(tree.nJet)
        
            for jet in xrange( len(tree.Jet_pt) ):
                model.allJetPtHist.Fill(tree.Jet_pt[jet])

            if len(tree.Jet_pt) > 0:
                model.leadJetPtHist.Fill(tree.Jet_pt[0])
            
            model.metPtHist.Fill(tree.MET_pt)

            if len(tree.Jet_phi) >= 2:
                nDiJetEvents += 1
                deltaPhi = tree.Jet_phi[0] - tree.Jet_phi[1]
                model.dPhiJJHist.Fill(deltaPhi)        

            pbar.update(entry+1)
        
        pbar.finish()

        # Normalise histograms
        model.nJetHist.Scale(1./nEvents)
        model.allJetPtHist.Scale(1./nEvents)
        model.leadJetPtHist.Scale(1./nEvents)
        model.metPtHist.Scale(1./nEvents)
        model.dPhiJJHist.Scale(1./nDiJetEvents)

        # Draw individual histograms and save
        drawIndivHistos(model, model.nJetHist, canv, legend_frame)
        drawIndivHistos(model, model.allJetPtHist, canv, legend_frame)
        drawIndivHistos(model, model.leadJetPtHist, canv, legend_frame)
        drawIndivHistos(model, model.metPtHist, canv, legend_frame)
        drawIndivHistos(model, model.dPhiJJHist, canv, legend_frame)

        # Add histograms to respective arrays
        nJetHistArr.append(model.nJetHist)
        allJetPtHistArr.append(model.allJetPtHist)
        leadJetPtHistArr.append(model.leadJetPtHist)
        metPtHistArr.append(model.metPtHist)
        dPhiJJHistArr.append(model.dPhiJJHist)
    

    # Draw histograms for each model overlaid and save
    drawMultipleHistos(nJetHistArr, canv, legend_frame, models)
    drawMultipleHistos(allJetPtHistArr, canv, legend_frame, models)
    drawMultipleHistos(leadJetPtHistArr, canv, legend_frame, models)
    drawMultipleHistos(metPtHistArr, canv, legend_frame, models)
    drawMultipleHistos(dPhiJJHistArr, canv, legend_frame, models)
    


if __name__ == '__main__':
    main()
