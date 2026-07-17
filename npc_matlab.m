function npcValue = npc(image_filepath, mask_filepaths, num_bins, min_val, max_val)
%   Computes the NPC value for a reference image given a set of class
%   masks, following the paper:
%   W. Peaslee, A. Breger and C. -B. Schönlieb,
%   "Potential Contrast: Properties, Equivalences, 
%   Generalization to Multiple Classes," 
%   2025 33rd European Signal Processing Conference (EUSIPCO), 
%   doi: 10.23919/EUSIPCO63237.2025.11226174.
%   Claude Sonnet 5 used to support conversion from python code.
%
%   Inputs:
%       image_filepath  - path to reference grayscale image
%       mask_filepaths  - cell array of paths to binary mask images
%       num_bins        - number of bins for the grayscale histogram
%       min_val         - minimum value of the data range
%       max_val         - maximum value of the data range
%
%   Output:
%       npcValue - the computed NPC value (double)
%
%   Example:
%       val = npc('gray1.png', {'bg1.png','fg1.png','fg2.png'}, 256, 0, 256);

    maskArrs = cell(1, length(mask_filepaths));
    for i = 1:length(mask_filepaths)
        maskArrs{i} = rgb2gray(imread(mask_filepaths{i})) ~= 0;
    end
    refArr = rgb2gray(imread(image_filepath));

    dataRange = [min_val, max_val];
    distributions = cell(1, length(maskArrs));
    for i = 1:length(maskArrs)
        pixelValues = double(refArr(maskArrs{i}));
        counts = histcounts(pixelValues, num_bins, 'BinLimits', dataRange);
        distributions{i} = counts / sum(counts);
    end

    distMatrix = cell2mat(distributions');
    maxPerBin = max(distMatrix, [], 1);
    npcValue = (sum(maxPerBin) - 1) / (length(mask_filepaths) - 1);

end
