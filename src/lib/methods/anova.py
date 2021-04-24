from sklearn.feature_selection import SelectKBest, f_classif

def anova(X, y, numOfFeatures = 'all'):
	selector = SelectKBest(score_func=f_classif, k=numOfFeatures).fit(X, y)
	cols = selector.get_support(indices = True).tolist()
	x_new = selector.transform(X)
	return x_new, cols
