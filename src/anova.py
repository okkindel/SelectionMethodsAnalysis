from lib.data_preprocessing import getCreditCardData, getHeartData
from sklearn.feature_selection import SelectKBest, f_classif
from lib.feature_selection import get_average_score
from lib.summary import make_summary

def select_best_features(X, Y, numOfFeatures = 'all'):
	return SelectKBest(score_func=f_classif, k=numOfFeatures).fit_transform(X, y)

# -----------------------------------------------------------------------------------------------

[X, y] = getHeartData()
X_Fit = select_best_features(X, y, 3)

accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no)
