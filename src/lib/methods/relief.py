import sklearn_relief as _relief

def relief(X, y, numOfFeatures = 'all'):
	return _relief.ReliefF(n_features=numOfFeatures).fit_transform(X, y)
