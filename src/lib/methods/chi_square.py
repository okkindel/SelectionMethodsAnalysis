from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler

def chi_square(X, y, numOfFeatures = 'all'):
	X_Norm = MinMaxScaler().fit_transform(X)
	return SelectKBest(score_func=chi2, k=numOfFeatures).fit_transform(X_Norm, y)
