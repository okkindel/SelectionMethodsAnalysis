from sklearn.feature_selection import SelectKBest, mutual_info_classif

def information_gain(X, y, numOfFeatures = 'all'):
	return SelectKBest(score_func=mutual_info_classif, k=numOfFeatures).fit_transform(X, y)
