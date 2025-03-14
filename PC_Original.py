# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:23:50 2025

@author: Wallace Peaslee
"""


from PIL import Image
import numpy as np


'''
Assume masks have labeled pixels as white.
'''
classMasks_filepaths = [] #list with foreground and background mask filepaths
invertMasks = False #if masks have labeled pixels in black, set this to True
referenceImage_filepath = '' #filepath of reference image
save_filepath = ''
numBins = None #The number of bins used to computer potential contrast. 
#The number of bins is typically 256, since that mirrors an 8-bit image.
dataRange = None #dataRange can be set here, or allowed to be default
#The default takes the maximum and minimum of the image
#This is mostly relevant for PC (not normalized)
#For an 8-bit image, dataRange can be set to (0, 255)


assert dataRange is None or (dataRange[0] < dataRange[1] and len(dataRange) == 2), 'please give data range in the format (min, max).'

numClasses = len(classMasks_filepaths)
assert (numClasses == 2), 'This is for PC, and should have exactly two masks.'

def normArray(arr):
    arrMax = np.max(arr)
    arrMin = np.min(arr)
    return (arr - arrMin)/(arrMax - arrMin)

try:
    if invertMasks:
        maskArrs = [np.array(Image.open(x).convert('L')) == 0 for x in classMasks_filepaths]
    else:
        maskArrs = [np.array(Image.open(x).convert('L')) != 0 for x in classMasks_filepaths]
    refArr = np.array(Image.open(referenceImage_filepath).convert('L'))
except IOError:
    print('Please input valid fle names.')
#assert numBins <= np.unique(refArr), 'Please ensure there are not too many bins'
#or assert number of sampled pixels is at least as large as the number of bins

if dataRange is None:
    dataRange = (np.min(refArr), np.max(refArr))
    
#To compute PC, we first compute the binarized image.
histograms = [np.histogram(refArr[x], bins=numBins, range=dataRange, density=True) for x in maskArrs]
binEdges = histograms[0][1]

binClassAssignments = np.zeros((numBins)) - 1
for binIndex in range(numBins):
    binClassAssignments[binIndex] = max(range(numClasses),
                                        key = lambda x: histograms[x][0][binIndex])
binEdges[-1] += 1
mappedBins = np.digitize(refArr, binEdges, right = False) - 1
mappedClasses = binClassAssignments[mappedBins]
mappedClassesImageRange = mappedClasses*(dataRange[1] - dataRange[0]) + dataRange[0]

PC = mappedClassesImageRange[maskArrs[1]] - mappedClassesImageRange[maskArrs[0]]
#End of PC computation
NPC = PC/(dataRange[1] - dataRange[0])
print('data range:', dataRange)
print('PC:', PC)
print('NPC:', NPC)

visualization = Image.fromarray(np.round(normArray(mappedClasses)*255).astype('uint8'))
try:
    visualization.save(save_filepath)
except IOError:
    print('Please input valid output filepath.')
    




    
    



