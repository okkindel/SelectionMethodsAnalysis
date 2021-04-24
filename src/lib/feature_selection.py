from sklearn.model_selection import RepeatedStratifiedKFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np

RANDOM_STATE = 10

# divide data by sets (Cross-validation)
def divide_by_sets():
  return RepeatedStratifiedKFold(n_splits=2, n_repeats=5, random_state=RANDOM_STATE)

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

# calculate TP, TN, FP, FN
def calculateConfusionMatrix(matrix):
    TP = matrix[0][0]
    TN = matrix[1,1]
    FP = matrix[0][1]
    FN = matrix[1, 0]
    return TP, TN, FP, FN

# reverse confusuion matrix
def reverseMatrix(matrix):
    return np.flip(matrix)

# calculating FPT and TPR abd TNR
def calculateFPR_TPR_TNR(matrix):
    TP, TN, FP, FN = calculateConfusionMatrix(matrix)
    tpfn = 0.00001 if ((TP+FN) == 0) else TP + FN
    tnfp = 0.00001 if ((TN+FP) == 0) else TN + FP
    TPR = TP/(tpfn)
    FPR = FP/(tnfp)
    TNR = TN/(tnfp)
    return TPR, FPR, TNR

# calculating FPT and TPR
def calculateBalancedAcc(matrix):
    TPR, _, TNR = calculateFPR_TPR_TNR(matrix)
    return (TPR + TNR) / 2

# calculating precision
def calculatePrecision(matrix):
    TP, _, FP, _ = calculateConfusionMatrix(matrix)
    tpfp = 0.00001 if ((TP+FP) == 0) else TP + FP
    return TP / tpfp

# calculating recall
def calculateRecall(matrix):
    TP, _, _, FN = calculateConfusionMatrix(matrix)
    tpfn = 0.00001 if ((TP+FN) == 0) else TP + FN
    return TP / tpfn

# calculating f1
def calculateF1(matrix):
    prec = calculatePrecision(matrix)
    rec = calculateRecall(matrix)
    pr =  0.00001 if ((prec+rec) == 0) else prec + rec
    return (2 * prec * rec) / pr
