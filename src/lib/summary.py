from lib.feature_selection import calculatePrecision, calculateFPTandTPR, calculateF1

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def make_simple_summary(set, X, accuracy, matrix, method):
    print(bcolors.YELLOW +  set + ': \n'                                          + bcolors.ENDC)
    print(bcolors.YELLOW +  method + ': \n'                                          + bcolors.ENDC)
    print(bcolors.YELLOW + 'NB_OF_FEATURES: '   + str(X.shape[1])                    + bcolors.ENDC)
    print(bcolors.YELLOW + 'NB_OF_ELEMENTS: '   + str(X.shape[0])                    + bcolors.ENDC)
    print(bcolors.YELLOW + 'ACCURACY: '         + str(accuracy)                      + bcolors.ENDC)
    print(bcolors.YELLOW + 'PRECISION: '        + str(calculatePrecision(matrix))    + bcolors.ENDC)
    print(bcolors.YELLOW + 'FPT_TPR: '          + str(calculateFPTandTPR(matrix))    + bcolors.ENDC)
    print(bcolors.YELLOW + 'F1 SCORE: '         + str(calculateF1(matrix))           + bcolors.ENDC)
    print(bcolors.YELLOW + 'MATRIX: \n'         + str(matrix)                        + bcolors.ENDC)
    print('\n')

def get_string_summary(set, X, accuracy, matrix, method):
    return (set
        + ',' + method + ',' + str(X.shape[1]) + ',' + str(X.shape[0]) + ',' + str(accuracy)
        + ',' + str(calculatePrecision(matrix)) + ',' + str(calculateFPTandTPR(matrix)[0])
        + ',' + str(calculateFPTandTPR(matrix)[1]) + ',' + str(calculateF1(matrix))
        + ',' + str(matrix).replace('\n', '') + '\n')
