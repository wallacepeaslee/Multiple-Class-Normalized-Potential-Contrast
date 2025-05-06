# Multi-Class Normalized Potential Contrast

This repository includes implementations for (Normalized) Potential Contrast and its generalizations to multiple classes [1]. For more details, see our paper at https://arxiv.org/abs/2505.01388.

Potential Contrast was introduced in [2], and PC_Original.py follows the algorithms for computation given e.g. in [3].

Our new efficient algorithms for potential contrast and our generilzation, multi-class normalized potential contrast, are included in Multiple_Source_NPC.py.

Simply update the filepaths to a reference image and class labels/masks to use. For  normalized potential contrast, set parameters depending on color bit-depth.


## References

[1] W. Peaslee, A. Breger, & C.-B. Schönlieb,"Potential Contrast: Properties, Equivalences, and Generalization to Multiple Classes," ArXiV preprint: https://arxiv.org/abs/2505.01388, 2025.

[2] A. Shaus, S. Faigenbaum-Golovin, B. Sober, and E. Turkel, “Potential contrast–a new image quality measure,” Electronic Imaging, vol. 29, pp. 52–58, 2017.

[3] S. Faigenbaum, B. Sober, A. Shaus, M. Moinester, E. Piasetzky, G. Bearman, M. Cordonsky, and I. Finkelstein, “Multispectral images of ostraca: acquisition and analysis,” Journal of Archaeological Science, vol. 39, no. 12, pp. 3581–3590, 2012.

