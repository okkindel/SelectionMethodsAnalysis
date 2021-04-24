from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler

def chi_square(X, y, numOfFeatures = 'all'):
	X_Norm = MinMaxScaler().fit_transform(X)
	selector = SelectKBest(score_func=chi2, k=numOfFeatures).fit(X_Norm, y)
	cols = selector.get_support(indices = True).tolist()
	x_new = selector.transform(X)
	return x_new, cols
