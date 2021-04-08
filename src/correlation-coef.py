from lib.feature_selection import get_average_score, get_no_knn_score
from sklearn.preprocessing import MinMaxScaler
from lib.summary import make_summary
import pandas as pd
import numpy as np

# https://github.com/krishnadulal/Feature-Selection-in-Machine-Learning-using-Python-All-Code/
# blob/master/Filtering%20Method/Feature%20Selection%20with%20Filtering%20Method-%20Constant%2
# C%20Quasi%20Constant%20and%20Duplicate%20Feature%20Removal.ipynb
def select_best_features(X, Y, treshold = 0.8):
    corr_col = set()
    corrmat = pd.DataFrame(X).corr()
    for i in range(len(corrmat.columns)):
        for j in range(i):
            if abs(corrmat.iloc[i, j]) > treshold:
                colname = corrmat.columns[i]
                corr_col.add(colname)
    x_drop = pd.DataFrame(X).drop(labels=corr_col, axis = 1)
    return x_drop.values

from_file = []
f = open('../data/wine.dat', 'r')
for line in f.readlines()[19:]:
    el = line.strip().split(',')
    from_file.append(el)

data = np.array(from_file, dtype=float)
X, y = data[:, :13], data[:, 13]

# X_Norm = MinMaxScaler().fit_transform(X)
X_Fit = select_best_features(X, y, 0.5)

accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X, accuracy, accuracy_no, matrix, matrix_no)


