from sklearn.feature_selection import SelectKBest, f_classif

def anova(X, y, numOfFeatures = 'all'):
	return SelectKBest(score_func=f_classif, k=numOfFeatures).fit_transform(X, y)
