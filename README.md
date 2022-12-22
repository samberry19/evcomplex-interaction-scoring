# EVcomplex interaction scoring

This is code for using [EVcomplex](https://elifesciences.org/articles/03430) to generate "interaction scores" for individual sequences 
in a multiple sequence alignment, as done in the paper:

> Katherine Hummels, Samuel Berry, Zhaoqi Li, Atsushi Taguchi, Joseph Min, Suzanne Walker, Debora Marks and Thomas G. Bernhardt (2022) Coordination of bacterial cell wall and outer membrane biosynthesis.

## Installation

This code relies installation of [EVcouplings](https://github.com/debbiemarkslab/EVcouplings) for working with DCA models and [Bioviper](https://github.com/samberry19/bioviper) for efficiently dealing with multiple sequence alignments and protein structures. Additional libraries used are the standard numpy, pandas, matplotlib, and seaborn along with sklearn for Gaussian mixture models, [ETE3](http://etetoolkit.org/) for taxonomic mapping, and mpl-interactions](https://github.com/ianhi/mpl-interactions) entirely optionally to add sliders and interactive features to some of the plots in the notebook.

## Contents

The function used for scoring sequences is located in the python script score.py, and the usage of it in the paper can be found in a series of Jupyter notebooks under the notebooks/ subdirectory. This section contains code to generate all figures in the paper other than - at the moment - the phylogenetic tree.

To allow for interactive exploration of the data beyond what's in the paper, I make use of [mpl-interactions](https://github.com/ianhi/mpl-interactions), which needs to be installed if you want to use the sliders in the notebook! I use these to explore some of the admittedly relatively arbitrary choices that we make in the paper, so you can see how certain distributions would be shifted if we used different numbers of couplings in various places.

The two notebooks at the moment are:

* "Analyzing murA and lpxC EVcomplex runs" for code to initially identify couplings that match the AlphaFold model and generate a new subset of the concatenated multiple sequence alignment to rerun EVcomplex

* "Final interaction scores": After rerunning EVcomplex, calculation the final interaction scores from the new model along with taxonomy and mixture model analysis.

Inquiries about the code should be addressed to sberry@g.harvard.edu.
