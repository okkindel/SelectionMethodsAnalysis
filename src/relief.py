from lib.feature_selection import get_average_score, calculatePrecision, calculateFPTandTPR, get_special_train
from lib.data_preprocessing import getCreditCardData
from sklearn.preprocessing import MinMaxScaler
import sklearn_relief as relief
import numpy as np

# https://gitlab.com/moongoal/sklearn-relief
def select_best_features(X, Y, numOfFeatures = 'all'):
	return relief.ReliefF(n_features=numOfFeatures).fit_transform(X, y)

df = getCreditCardData()
X_tab = df.drop('Class', axis=1)
y_tab = df['Class']
X, y = X_tab.values, y_tab.values

X_Fit = select_best_features(X, y, 3)
accuracy, matrix = get_average_score(X_Fit, y)
accuracy, matrix = get_average_score(X, y)

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

# from_train = []
# f = open('../data/heart/heart_special_train.dat', 'r')
# for line in f.readlines()[0:]:
#     el = line.strip().split(' ')
#     from_train.append(el)

# from_test = []
# f = open('../data/heart/heart_special_test.dat', 'r')
# for line in f.readlines()[0:]:
#     el = line.strip().split(' ')
#     from_test.append(el)

# train = np.array(from_train, dtype=float)
# test = np.array(from_test, dtype=float)
# X, y = train[:, :13], train[:, 13]
# X_test, y_test = test[:, :13], test[:, 13]

# X_Fit = select_best_features(X, y, 3)
# X_Test_Fit = select_best_features(X_test, y_test, 3)
# accuracy, matrix = get_special_train(X_Fit, y, X_Test_Fit, y_test)

# X_Fit = select_best_features(X, y, 3)
# X_Test_Fit = select_best_features(X_test, y_test, 3)
# accuracy_no, matrix_no = get_special_train(X, y, X_test, y_test)

# print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
# print('ACCURACY_SELECTION: ', accuracy)
# print('ACCURACY_NO_SELECTION: ', accuracy_no)
# print('PRECISION_SELECTION: ', calculatePrecision(matrix))
# print('PRECISION_NO_SELECTION: ', calculatePrecision(matrix_no))
# print('FPT_TPR_SELECTION: ', calculateFPTandTPR(matrix))
# print('FPT_TPR_NO_SELECTION: ', calculateFPTandTPR(matrix_no))