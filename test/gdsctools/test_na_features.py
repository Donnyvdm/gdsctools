import pandas as pd
import numpy as np
from gdsctools import ANOVA

def test_anova_with_pd_na_features():
    gf = pd.DataFrame({"COSMIC_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "GF2": [1, 1, 1, 1, 1, 0, 0, 0, 0, pd.NA]})
    ic50s = pd.DataFrame({"COSMIC_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1: [0.7, 0.8, 0.9, 0.8, 0.8, 0.4, 0.5, 0.3, 0.5, 0.5]})

    an = ANOVA(ic50=ic50s, genomic_features=gf)

    an.anova_all()


def test_anova_with_np_na_features():
    gf = pd.DataFrame({"COSMIC_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "GF2": [1, 1, 1, 1, 1, 0, 0, 0, 0, np.NaN]})
    ic50s = pd.DataFrame({"COSMIC_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1: [0.7, 0.8, 0.9, 0.8, 0.8, 0.4, 0.5, 0.3, 0.5, 0.5]})

    an = ANOVA(ic50=ic50s, genomic_features=gf)

    an.anova_all()