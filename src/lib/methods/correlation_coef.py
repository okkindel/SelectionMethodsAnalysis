import pandas as pd
import numpy as np
import math

def correlation_coef(X, Y, num_of_features):
    scores = []
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
        if not(x in scores):
            scores.append(x)
    scores = scores[:num_of_features]
    x_new = pd.DataFrame(X)[scores]
    scores.sort()
    return x_new.values, scores
