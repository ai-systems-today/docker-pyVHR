
# -- Modules and packages to import for demo
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.analysis.testsuite import TestSuite, TestResult


# -- Video object
detectors = ['mtcnn', 'dlib', 'mtcnn_kalman']
detector = detectors[0]
videoFilename = f"./sampleDataset/Jessica-5-20s-{detector}/invalidFile"
video = Video(videoFilename)

# -- extract faces
video.getCroppedFaces(detector=detector, extractor='skvideo', fps=30)
video.printVideoInfo()

print("\nShow video cropped faces, crop size:", video.cropSize)
video.showVideo()

print("-----END------")
exit()

# -- define ROIs: free rectangular regions
video.setMask(typeROI='rect', rectCoords=[[15,20,140,50],[10,120,100,30]])
video.printROIInfo()
video.showVideo()





# -- define ROIs: standard regions, i.e. 'forehead', 'lcheek', 'rcheek', 'nose'
video.setMask(typeROI='rect', rectRegions=['forehead', 'lcheek', 'rcheek', 'nose'])
video.printROIInfo()
video.showVideo()





# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()
video.showVideo()






# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_fix',skinThresh_fix=[20, 50])
video.printROIInfo()
video.showVideo()





# Apply rPPG methods

# -- Define a configuration file. 
#    It contains all the information relative to the dataset (e.g. the path), 
#    and the test procedure (e.g. hyperparamenters)
cfgFilename = '../pyVHR/analysis/sample.cfg'

# -- apply the pipeline until GT comparison
test = TestSuite(configFilename=cfgFilename)

# -- run exp and save results on a pandas file
#    change verb to see more details as follow:
#       0 - not verbose
#       1 - show the main steps
#       2 - display graphic 
#       3 - display spectra  
#       4 - display errors
#       (use also combinations, e.g. verb=21, verb=321)
result = test.start(outFilename='sampleExp.h5', verb=1)



# -- pandas file for collecting results
df = result.dataFrames
df.to_csv('basic-usage-results.csv')





# # Do fine tuning

# # -- Detailed pipeline for rafinement steps and tuning  

# # -- define some params in the form of dict (those in the cfg file) 
# params = {"video": video, "verb":2, "ROImask":"skin_adapt", "skinAdapt":0.2}

# # -- invoke the method
# m = CHROM(**params)
# #m = POS(**params)

# # -- invoke the method
# bpmES, timesES = m.runOffline(**params)







# # Compare with ground truth (GT)

# from pyVHR.datasets.sample import SAMPLE
# from pyVHR.datasets.dataset import Dataset

# # -- dataset object
# dataset = SAMPLE(videodataDIR='../sampleDataset/', BVPdataDIR='../sampleDataset/alex/alex_resting/')

# # -- ground-truth (GT) signal
# idx = 0   # index of signal within the list dataset.videoFilenames
# fname = dataset.getSigFilename(idx)

# # -- load signal and build a BVPsignal or ECGsignal object
# sigGT = dataset.readSigfile(fname)
# sigGT.plot()

# # -- plot signal + peaks
# sigGT.findPeaks(distance=20)
# sigGT.plotBPMPeaks()

# # -- compute BPM GT
# winSizeGT = 7
# bpmGT, timesGT = sigGT.getBPM(winSizeGT)




# from pyVHR.utils.errors import getErrors, printErrors, displayErrors

# # -- error metrics
# RMSE, MAE, MAX, PCC = getErrors(bpmES, bpmGT, timesES, timesGT)
# printErrors(RMSE, MAE, MAX, PCC)
# displayErrors(bpmES, bpmGT, timesES, timesGT)




# # -- print BPM
# print("BPMs of the GT signal averaged on winSizeGT = %d sec:" %winSizeGT)
# print(bpmGT)

# # -- plot spectrogram
# sigGT.displaySpectrum()