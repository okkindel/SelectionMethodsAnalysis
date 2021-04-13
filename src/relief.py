from lib.data_preprocessing import getCreditCardData, getMushroomData, getCustomData, getInsuranceData, getSafeDriverData
from lib.feature_selection import get_average_score
from lib.summary import make_summary
import sklearn_relief as relief

# https://gitlab.com/moongoal/sklearn-relief
def select_best_features(X, Y, numOfFeatures = 'all'):
	return relief.ReliefF(n_features=numOfFeatures).fit_transform(X, y)

# -----------------------------------------------------------------------------------------------

X, y = getMushroomData()

X_Fit = select_best_features(X, y, 5)

accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no)

