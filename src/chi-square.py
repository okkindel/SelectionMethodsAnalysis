from lib.data_preprocessing import getSafeDriverData, getMushroomData, getCreditCardData, getHearthData
from sklearn.feature_selection import SelectKBest, chi2
from lib.feature_selection import get_average_score
from sklearn.preprocessing import MinMaxScaler
from lib.summary import make_summary

def select_best_features(X, Y, numOfFeatures = 'all'):
	X_Norm = MinMaxScaler().fit_transform(X)
	return SelectKBest(score_func=chi2, k=numOfFeatures).fit_transform(X_Norm, y)

# -----------------------------------------------------------------------------------------------

[X, y] = getHearthData()

X_Fit = select_best_features(X, y, 5)

accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no)
