from lib.feature_selection import get_average_score, calculatePrecision, calculateFPTandTPR, get_special_train
from lib.data_preprocessing import getCreditCardData, getCreditCardSpecialData
from sklearn.preprocessing import MinMaxScaler
import sklearn_relief as relief
import numpy as np

# https://gitlab.com/moongoal/sklearn-relief
def select_best_features(X, Y, numOfFeatures = 'all'):
	return relief.ReliefF(n_features=numOfFeatures).fit_transform(X, y)

[X, y] = getCreditCardData()

X_Fit = select_best_features(X, y, 3)
accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
print('ACCURACY_SELECTION: ', accuracy)
print('ACCURACY_NO_SELECTION: ', accuracy_no)
print('PRECISION_SELECTION: ', calculatePrecision(matrix))
print('PRECISION_NO_SELECTION: ', calculatePrecision(matrix_no))
print('FPT_TPR_SELECTION: ', calculateFPTandTPR(matrix))
print('FPT_TPR_NO_SELECTION: ', calculateFPTandTPR(matrix_no))

print('--------------------------------')
print('CUSTOM TESTING SET')
print('--------------------------------')

[X, y] = getCreditCardSpecialData()

X_Fit = select_best_features(X, y, 5)

X_train = X[:len(X - 20)]
X_Fit_train = X_Fit[:len(X - 20)]
y_train = y[:len(X - 20)]

X_test = X[-20:]
X_Fit_test = X_Fit[-20:]
y_test = y[-20:]

accuracy, matrix = get_special_train(X_Fit_train, y_train, X_Fit_test, y_test)
accuracy_no, matrix_no = get_special_train(X_train, y_train, X_test, y_test)

print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
print('ACCURACY_SELECTION: ', accuracy)
print('ACCURACY_NO_SELECTION: ', accuracy_no)
print('PRECISION_SELECTION: ', calculatePrecision(matrix))
print('PRECISION_NO_SELECTION: ', calculatePrecision(matrix_no))
print('FPT_TPR_SELECTION: ', calculateFPTandTPR(matrix))
print('FPT_TPR_NO_SELECTION: ', calculateFPTandTPR(matrix_no))

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

# X_Norm = MinMaxScaler().fit_transform(X)
# X_Fit = select_best_features(X, y, 1)
# accuracy, matrix = get_average_score(X_Fit, y)

# print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
# print('ACCURACY: ', accuracy)
# print('PRECISION: ', calculatePrecision(matrix))
# print('FPT TPR: ', calculateFPTandTPR(matrix))

# print('--------------------------------')
# print('CUSTOM TESTING SET')
# print('--------------------------------')

# from_data = []
# f = open('../data/heart/heart_special.dat', 'r')
# for line in f.readlines()[0:]:
#     el = line.strip().split(' ')
#     from_data.append(el)

# data = np.array(from_data, dtype=float)
# X, y = data[:, :13], data[:, 13]
# X_Fit = select_best_features(X, y, 3)

# X_train = X[:260]
# X_Fit_train = X_Fit[:260]
# y_train = y[:260]

# X_test = X[-10:]
# X_Fit_test = X_Fit[-10:]
# y_test = y[-10:]

# accuracy, matrix = get_special_train(X_Fit_train, y_train, X_Fit_test, y_test)
# accuracy_no, matrix_no = get_special_train(X_train, y_train, X_test, y_test)

# print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
# print('ACCURACY_SELECTION: ', accuracy)
# print('ACCURACY_NO_SELECTION: ', accuracy_no)
# print('PRECISION_SELECTION: ', calculatePrecision(matrix))
# print('PRECISION_NO_SELECTION: ', calculatePrecision(matrix_no))
# print('FPT_TPR_SELECTION: ', calculateFPTandTPR(matrix))
# print('FPT_TPR_NO_SELECTION: ', calculateFPTandTPR(matrix_no))