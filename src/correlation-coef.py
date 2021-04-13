from lib.data_preprocessing import getSafeDriverData, getMushroomData, getCreditCardData, getInsuranceData, getCustomData
from lib.feature_selection import get_average_score
from lib.summary import make_summary
from Py_FS.filter import PCC
from sklearn import datasets
import pandas as pd

# https://github.com/krishnadulal/Feature-Selection-in-Machine-Learning-using-Python-All-Code/
# blob/master/Filtering%20Method/Feature%20Selection%20with%20Filtering%20Method-%20Constant%2
# C%20Quasi%20Constant%20and%20Duplicate%20Feature%20Removal.ipynb
def select_best_features(X, Y, treshold = 0.8):
    corr_col = set()
    corrmat = pd.DataFrame(X).corr()
    for i in range(len(corrmat.columns)):
        for j in range(i):
            if abs(corrmat.iloc[i, j]) > treshold:
                colname = corrmat.columns[i]
                corr_col.add(colname)
    x_drop = pd.DataFrame(X)[corr_col]
    return x_drop.values

# def select_best_features(X, Y, num_of_features = 'all'):
#     scores = PCC(X, y).ranks
#     scores = scores[:num_of_features]
#     x_drop = pd.DataFrame(X)[scores]
#     return x_drop.values

# -----------------------------------------------------------------------------------------------

[X, y] = getCustomData()

X_Fit = select_best_features(X, y, 0.00775)

# print(X_Fit.shape[1])

accuracy, matrix = get_average_score(X_Fit, y)
accuracy_no, matrix_no = get_average_score(X, y)

make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no)
