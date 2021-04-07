from sklearn.model_selection import RepeatedStratifiedKFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np

random_state = 10

# divide data by sets (Cross-validation)
def divide_by_sets():
  return RepeatedStratifiedKFold(n_splits=2, n_repeats=5, random_state=random_state)

# create network
def create_kNN():
  return KNeighborsClassifier(n_neighbors=10, n_jobs=2)

# make KNN neural network
def makeKNN(XTrain, YTrain, XTest, YTest):
    knn = create_kNN()
    knn.fit(XTrain, YTrain)
    predictions = knn.predict(XTest)
    matrix = confusion_matrix(YTest, predictions)
    accuracy = knn.score(XTest, YTest)
    return accuracy, matrix

# count average score (using cross validation)
def get_average_score(X, Y):
    rkf = divide_by_sets()
    confusion = []
    score = []

    for train, test in rkf.split(X, Y):
        x_train, x_test = X[train], X[test]
        y_train, y_test = Y[train], Y[test]
        temp_score, matrix = makeKNN(x_train, y_train, x_test, y_test)
        score.append(temp_score)
        confusion.append(matrix)

    return np.mean(score), np.mean(confusion, axis=0)

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

# calculate TP, TN, FP, FN
def calculateConfusionMatrixValuesForClass(matrix):
    TP = matrix[0][0]
    matrixTN = matrix[1:,1:]
    TN = np.sum(matrixTN)
    matrixFP = matrix[0][1:]
    FP = np.sum(matrixFP)
    matrixFN = matrix[1:, 0]
    FN = np.sum(matrixFN)
    return TP, TN, FP, FN

# calculating FPT and TPR for creating ROC curve to see Gini coeeficient
def calculateFPTandTPR(matrix):
    TP, TN, FP, FN = calculateConfusionMatrixValuesForClass(matrix)
    FPR = FP/(TN+FP)
    TPR = TP/(TP+FN)
    return FPR, TPR

# calculating precision
def calculatePrecision(matrix):
    TP, _, FP, _ = calculateConfusionMatrixValuesForClass(matrix)
    precision = TP/(TP+FP)
    return precision