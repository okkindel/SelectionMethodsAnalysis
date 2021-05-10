from sklearn.datasets import make_classification
from numpy import savetxt
import pandas as pd

X, y = make_classification(
    n_classes=2, class_sep=1.5, weights=[0.9, 0.1],
    n_informative=3, n_redundant=1, flip_y=0,
    n_features=20, n_clusters_per_class=1,
    n_samples=200000, random_state=10
)

df = pd.DataFrame(X)
df.insert(20, 'target', y, True)
table = df.values

savetxt('custom_200000.csv', table, delimiter=',',fmt='%s')


# count average score (without cross validation)
def get_no_knn_score(X, y, X_test, y_test):
    score, matrix = makeKNN(X, y, X_test, y_test)
    return score, matrix

def divide_by_hand(X, XFit, y, numOfFeatures):
    X_train = X[:len(X - numOfFeatures)]
    X_Fit_train = XFit[:len(X - numOfFeatures)]
    y_train = y[:len(X - numOfFeatures)]
    
    X_test = X[-numOfFeatures:]
    X_Fit_test = XFit[-numOfFeatures:]
    y_test = y[-numOfFeatures:]

    return [X_train, X_Fit_train, y_train, X_test, X_Fit_test, y_test]