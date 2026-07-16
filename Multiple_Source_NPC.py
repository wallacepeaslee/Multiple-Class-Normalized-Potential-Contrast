# -*- coding: utf-8 -*-
"""
This code computes multi-class Normalized Potential Contrast.
See
[1] W. Peaslee, A. Breger and C. -B. Schönlieb,
"Potential Contrast: Properties, Equivalences, 
and Generalization to Multiple Classes," 
2025 33rd European Signal Processing Conference (EUSIPCO), 
Palermo, Italy, 2025, pp. 716-720, doi: 10.23919/EUSIPCO63237.2025.11226174.

To run this code, update the parameters below.

"""


'''
PARAMETERS:
    
MclassMasks_filepaths: list of paths to images of masks for computing mc-npc.
    Masks are binary images, where pixels to be used are white and pixels to be
    excluded are black.
invertMasks: set to True if pixels to be used in the masks are in black.
referenceImage_filepath: filepath of reference image (.png, .tif, etc)
numBins: the number of bins to discretize and image's grayscale values in.
    This is typically 256, mirroring an 8-bit image.
    If numBins is too large and data is in a 16-bit format or more, then 
    npc might always be near 1.
dataRange: the range of values possible in your data type.
    Please set this to be (0, 256) for 8-bit images, or (0,1) for normalized images.
    This is also the normalization factor applied for computing (non-normalized) PC.
    If left as None, the data range is taken as the (minimum of the image, maximum of image)
save_filepath: the filepath where a segmentation map can be saved.
    Note that for any grayscale value where there ties in a classes' proportions of pixels
    at that value, the segmentation image is arbitrary.
    Note: this is NOT generally designed to be used as segmentation, but can 
    be diagnostic for understanding the numeric NPC value.
'''
classMasks_filepaths = ['', '', ''] #list of filepaths to masks
invertMasks = False #if masks have labeled pixels in black, set this to True
referenceImage_filepath = '' #filepath of reference image
numBins = 256 #The number of bins used to computer potential contrast. 
dataRange = (0,  256) #dataRange can be set here
save_filepath = 'test2.png'
'''
End of Parmaeters
'''



from PIL import Image
import numpy as np


def normArray(arr):
    arrMax = np.max(arr)
    arrMin = np.min(arr)
    return (arr - arrMin)/(arrMax - arrMin)


assert dataRange is None or (dataRange[0] < dataRange[1] and len(dataRange) == 2), 'please give data range in the format (min, max).'

numClasses = len(classMasks_filepaths)
try:
    if invertMasks:
        maskArrs = [np.array(Image.open(x).convert('L')) == 0 for x in classMasks_filepaths]
    else:
        maskArrs = [np.array(Image.open(x).convert('L')) != 0 for x in classMasks_filepaths]
    refArr = np.array(Image.open(referenceImage_filepath).convert('L'))
except IOError:
    print('Please input valid fle names.')
assert (numClasses > 1), 'Please supply more than 1 mask.'

if dataRange is None:
    dataRange = (np.min(refArr), np.max(refArr))
    
#begin computation of NPC
histograms = [np.histogram(refArr[x], bins=numBins, range=dataRange, density=False) for x in maskArrs]
distributions = [x[0].astype('float')/np.sum(x[0]) for x in histograms] 


NPC = (sum([max([h[b] for h in distributions]) for b in range(numBins)]) - 1)/(numClasses-1)
#end computation of NPC
PC = NPC*(dataRange[1] - dataRange[0])
print('data range:', dataRange)
print('PC:', PC)
print('NPC:', NPC)

#compute and save Binarized image
binEdges = histograms[0][1]

binClassAssignments = np.zeros((numBins)) - 1
for binIndex in range(numBins):
    binClassAssignments[binIndex] = max(range(numClasses),
                                        key = lambda x: distributions[x][binIndex])
binEdges[-1] += 1
mappedBins = np.digitize(refArr, binEdges, right = False) - 1
mappedClasses = binClassAssignments[mappedBins]

assert (numClasses < 255), 'The following visualization only works if there are not too many classes.'
visualization = Image.fromarray(np.round(normArray(mappedClasses)*255).astype('uint8'))
try:
    visualization.save(save_filepath)
except IOError:
    print('Please input valid output filepath.')
    



    
    



