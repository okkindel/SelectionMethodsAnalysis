# import sklearn_relief as _relief

# # https://gitlab.com/moongoal/sklearn-relief
# def relief(X, y, numOfFeatures = 'all'):
# 	selector = _relief.ReliefF(n_features=numOfFeatures).fit(X, y)
# 	x_new = selector.transform(X)
# 	scores = np.flip(np.argsort(selector.w_), 0)[0 : numOfFeatures].tolist()
# 	return x_new, scores
