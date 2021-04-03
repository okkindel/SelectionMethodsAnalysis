from lib.feature_selection import get_average_score, calculatePrecision, calculateFPTandTPR
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler
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

print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
print('RANK: ', X_Fit.shape)
print('ACCURACY: ', accuracy)
print('PRECISION: ', calculatePrecision(matrix))
print('FPT TPR: ', calculateFPTandTPR(matrix))
