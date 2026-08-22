function npcValue = npc(im, masks, num_bins, min_val, max_val)
%   Computes the NPC value for a reference image given a set of class
%   masks, following the paper:
%   W. Peaslee, A. Breger and C. -B. Schönlieb,
%   "Potential Contrast: Properties, Equivalences, 
%   Generalization to Multiple Classes," 
%   2025 33rd European Signal Processing Conference (EUSIPCO), 
%   doi: 10.23919/EUSIPCO63237.2025.11226174.
%   Claude Sonnet 5 used to generate some of this code 
%   and support conversion from python code.
%
%   Inputs:
%       im       - 2D grayscale reference image (numeric array)
%       masks    - cell array of 2D binary masks (logical arrays),
%                  each the same size as im
%       num_bins - number of bins for the grayscale histogram
%       min_val  - minimum value of the data range
%       max_val  - maximum value of the data range
%
%   Output:
%       npcValue - the computed NPC value (double)
%
%   Example:
%       val = npc(rgb2gray(imread('gray1.png')), ...
%                 {rgb2gray(imread('bg1.png')) ~= 0, ...
%                  rgb2gray(imread('fg1.png')) ~= 0, ...
%                  rgb2gray(imread('fg2.png')) ~= 0}, ...
%                 256, 0, 256);

    assert(ismatrix(im), 'im must be a 2D array.');
    assert(iscell(masks), 'masks must be a cell array of binary masks.');
    assert(numel(masks) > 1, 'Please supply more than 1 mask.');

    numClasses = numel(masks);
    for i = 1:numClasses
        assert(ismatrix(masks{i}), sprintf('Mask %d must be a 2D array.', i));
        assert(islogical(masks{i}), sprintf('Mask %d must be a logical (binary) array.', i));
        assert(isequal(size(masks{i}), size(im)), ...
            sprintf('Mask %d size does not match im size.', i));
    end

    refArr = im;
    maskArrs = masks;

    dataRange = [min_val, max_val];
    distributions = cell(1, length(maskArrs));
    for i = 1:length(maskArrs)
        pixelValues = double(refArr(maskArrs{i}));
        counts = histcounts(pixelValues, num_bins, 'BinLimits', dataRange);
        distributions{i} = counts / sum(counts);
    end

    distMatrix = cell2mat(distributions');
    maxPerBin = max(distMatrix, [], 1);
    npcValue = (sum(maxPerBin) - 1) / (length(masks) - 1);

end
