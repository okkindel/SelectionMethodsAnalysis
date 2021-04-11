from lib.data_preprocessing import getWineData, getHeartData, getSafeDriverData, getCreditCardData
from lib.feature_selection import get_average_score, get_no_knn_score, divide_by_hand
from sklearn.feature_selection import SelectKBest, chi2
from lib.summary import make_summary
import numpy as np

print('--------------------------------')
print('CUSTOM TESTING SET')
print('--------------------------------')

[X, y] = getCreditCardData()
X_Fit = select_best_features(X, y, 5)

[X_train, X_Fit_train, y_train, X_test, X_Fit_test, y_test] = divide_by_hand(X, X_Fit, y, 20)

accuracy, matrix = get_no_knn_score(X_Fit_train, y_train, X_Fit_test, y_test)
accuracy_no, matrix_no = get_no_knn_score(X_train, y_train, X_test, y_test)

make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no)


# ------- HEART -------


print('--------------------------------')
print('CUSTOM TESTING SET')
print('--------------------------------')

from_data = []
f = open('../data/heart.dat', 'r')
for line in f.readlines()[0:]:
    el = line.strip().split(' ')
    from_data.append(el)

data = np.array(from_data, dtype=float)
X, y = data[:, :13], data[:, 13]
X_Fit = select_best_features(X, y, 3)

[X_train, X_Fit_train, y_train, X_test, X_Fit_test, y_test] = divide_by_hand(X, X_Fit, y, 20)

accuracy, matrix = get_no_knn_score(X_Fit_train, y_train, X_Fit_test, y_test)
accuracy_no, matrix_no = get_no_knn_score(X_train, y_train, X_test, y_test)

make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no)