from sklearn.feature_selection import SelectKBest, mutual_info_classif

def information_gain(X, y, numOfFeatures = 'all'):
	selector = SelectKBest(score_func=mutual_info_classif, k=numOfFeatures).fit(X, y)
	cols = selector.get_support(indices = True).tolist()
	x_new = selector.transform(X)
	return x_new, cols
