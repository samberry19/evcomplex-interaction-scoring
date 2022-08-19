# EVcomplex interaction scoring

This is code for using [EVcomplex](https://elifesciences.org/articles/03430) to generate "interaction scores" for individual sequences 
in a multiple sequence alignment, as done in the paper:

> Katherine Hummels, Samuel Berry, Zhaoqi Li, Atsushi Taguchi, Joseph Min, Suzanne Walker, Debora Marks and Thomas G. Bernhardt (2022) A regulatory interaction between committed enzymes links lipopolysaccharide and peptidoglycan biogenesis in Pseudomonas aeruginosa. doi: ???

## Installation

This code relies installation of [EVcouplings](https://github.com/debbiemarkslab/EVcouplings) for working with DCA models and [Bioviper](https://github.com/samberry19/bioviper) for efficiently dealing with multiple sequence alignments and protein structures.

## Contents

The function used for scoring sequences is located in the python script score.py, and the usage of it in the paper can be found in a series of Jupyter notebooks under the notebooks/ subdirectory.

Inquiries about the code should be addressed to sberry@g.harvard.edu.
