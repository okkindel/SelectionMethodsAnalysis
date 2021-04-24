from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

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
        score, matrix = makeKNN(x_train, y_train, x_test, y_test)

    return score, matrix
