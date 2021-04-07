from lib.feature_selection import get_average_score, get_no_knn_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler
from lib.summary import make_summary
import numpy as np

def select_best_features(X, Y, numOfFeatures = 'all'):
	return SelectKBest(score_func=chi2, k=numOfFeatures).fit_transform(X, y)

from_file = []
f = open('../data/wine.dat', 'r')
for line in f.readlines()[19:]:
    el = line.strip().split(',')
    from_file.append(el)

data = np.array(from_file, dtype=float)
X, y = data[:, :13], data[:, 13]

# X_Norm = MinMaxScaler().fit_transform(X)
X_Fit = select_best_features(X, y, 5)
accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X, accuracy, accuracy_no, matrix, matrix_no)
