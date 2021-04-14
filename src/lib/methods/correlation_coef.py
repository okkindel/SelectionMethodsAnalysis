import pandas as pd
import numpy as np
import math

def correlation_coef(X, Y, num_of_features):
    corr_col = []
    corrmat = pd.DataFrame(X).corr()
    rank = []
    for i in range(len(corrmat.columns)):
        for j in range(i):
            element = abs(corrmat.iloc[i, j])
            if not(math.isnan(element)):
                rank.append((element, corrmat.columns[i]))

    rank = [x[1] for x in sorted(rank)]
    rank.reverse()
    for x in rank:
        if not(x in corr_col):
            corr_col.append(x)
    corr_col = corr_col[:num_of_features]
    x_drop = pd.DataFrame(X)[corr_col]
    return x_drop.values
