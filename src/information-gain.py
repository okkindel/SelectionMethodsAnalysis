from lib.feature_selection import get_average_score, get_no_knn_score, divide_by_hand
from lib.data_preprocessing import getCreditCardData, getCreditCardSpecialData
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import MinMaxScaler
from lib.summary import make_summary
import numpy as np

def select_best_features(X, Y, numOfFeatures = 'all'):
	return SelectKBest(score_func=mutual_info_classif, k=numOfFeatures).fit_transform(X, y)

[X, y] = getCreditCardData()
X_Fit = select_best_features(X, y, 3)

accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X, accuracy, accuracy_no, matrix, matrix_no)

print('--------------------------------')
print('CUSTOM TESTING SET')
print('--------------------------------')

[X, y] = getCreditCardSpecialData()
X_Fit = select_best_features(X, y, 5)

[X_train, X_Fit_train, y_train, X_test, X_Fit_test, y_test] = divide_by_hand(X, X_Fit, y, 20)

accuracy, matrix = get_no_knn_score(X_Fit_train, y_train, X_Fit_test, y_test)
accuracy_no, matrix_no = get_no_knn_score(X_train, y_train, X_test, y_test)

make_summary(X, accuracy, accuracy_no, matrix, matrix_no)

# --------------------------------
# HEART
# --------------------------------

# from_file = []
# f = open('../data/heart/heart.dat', 'r')
# for line in f.readlines()[0:]:
#     el = line.strip().split(' ')
#     from_file.append(el)

# data = np.array(from_file, dtype=float)
# X, y = data[:, :13], data[:, 13]

# # X_Norm = MinMaxScaler().fit_transform(X)
# X_Fit = select_best_features(X, y, 1)
# accuracy, matrix = get_average_score(X_Fit, y)

# make_summary(X, accuracy, 0, matrix, 0)
