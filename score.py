import numpy as np
from numpy import char
import pandas as pd

from evcouplings.align import Alignment
from evcouplings.couplings import CouplingsModel

def score_sequences(model, ali_1, ali_2, inter_couplings, n_couplings,
                    first_index_1=1, first_index_2=1, p_thresh=0.9):

    '''Scores a set of sequences using an EVcomplex model.'''

    # If you pass a string, interprets it as "use the top N couplings"
    if type(n_couplings)==int:
        raw_pairs = np.array(inter_couplings.iloc[np.arange(n_couplings)][['i','j']])

    # Otherwise, we assume that you're telling it the indices of the couplings to use
    else:
        raw_pairs = np.array(inter_couplings.iloc[n_couplings][['i','j']])

    # Subset the appropriate positions from the alignments
    sq1 = ali_1.matrix[:, raw_pairs[:,0] - first_index_1]
    sq2 = ali_2.matrix[:, raw_pairs[:,1] - first_index_2]

    # Couplings (pairs of positions) that don't meet the p_thresh criterion will be discarded
    keep_p = np.sum((sq1!='-')&(sq2!='-'),axis=0) > p_thresh * len(sq1)

    # Keep only those positions
    sq1 = sq1[:,keep_p]; sq2 = sq2[:,keep_p]

    # Pairs to index
    p1 = raw_pairs[keep_p,0]
    p2 = raw_pairs[keep_p,1] + ali_1.L


    keep_s = np.sum((sq1!='-')&(sq2!='-'),axis=1) == np.sum(keep_p)

    sq1 = sq1[keep_s]; sq2 = sq2[keep_s]

    print('Kept', np.sum(keep_p), 'out of', len(keep_p), 'pairs and', np.sum(keep_s), 'out of', len(keep_s), 'sequences')

    X = []
    for i in range(len(sq1)):

        X.append(model.Jij(p1, p2, sq1[i], sq2[i]))

    return np.array(X), keep_s, keep_p
