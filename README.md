# Multi-Class Normalized Potential Contrast

This repository includes implementations for (Normalized) Potential Contrast and its generalizations to multiple classes \[1]. If you use this repository, please cite our paper \[1] linked [here](https://ieeexplore.ieee.org/document/11226174). Additional technical details and definitions can also be found in this paper.

Potential Contrast was introduced in \[2], and PC\_Original.py follows the algorithms for computation given e.g. in \[3].

Our new efficient algorithms for potential contrast and our generalization, multi-class normalized potential contrast, are included in Multiple\_Source\_NPC.py. The only requirements for running are the python packages are the Python Imaging Library (PIL/Pillow) and NumPy.

Simply update the filepaths to a reference image and class labels/masks to use (such as those in the Example folder). For  normalized potential contrast, set parameters depending on color bit-depth.



## References

\[1] W. Peaslee, A. Breger and C. -B. Schönlieb, "Potential Contrast: Properties, Equivalences, and Generalization to Multiple Classes," 2025 33rd European Signal Processing Conference (EUSIPCO), Palermo, Italy, 2025, pp. 716-720, doi: 10.23919/EUSIPCO63237.2025.11226174.

\[2] A. Shaus, S. Faigenbaum-Golovin, B. Sober, and E. Turkel, “Potential contrast–a new image quality measure,” Electronic Imaging, vol. 29, pp. 52–58, 2017.

\[3] S. Faigenbaum, B. Sober, A. Shaus, M. Moinester, E. Piasetzky, G. Bearman, M. Cordonsky, and I. Finkelstein, “Multispectral images of ostraca: acquisition and analysis,” Journal of Archaeological Science, vol. 39, no. 12, pp. 3581–3590, 2012.

