from lib.feature_selection import calculatePrecision, calculateFPTandTPR, calculateF1

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def make_summary(X_Fit, X, accuracy, accuracy_no, matrix, matrix_no):

    print(bcolors.YELLOW + 'NO SELECTION: \n' + bcolors.ENDC)

    print(bcolors.YELLOW + 'NB_OF_FEATURES: '   + str(X.shape[1])                       + bcolors.ENDC)
    print(bcolors.YELLOW + 'ACCURACY: '         + str(accuracy_no)                      + bcolors.ENDC)
    print(bcolors.YELLOW + 'PRECISION: '        + str(calculatePrecision(matrix_no))    + bcolors.ENDC)
    print(bcolors.YELLOW + 'FPT_TPR: '          + str(calculateFPTandTPR(matrix_no))    + bcolors.ENDC)
    print(bcolors.YELLOW + 'F1 SCORE: '       + str(calculateF1(matrix_no))           + bcolors.ENDC)
    print(bcolors.YELLOW + 'MATRIX: \n'         + str(matrix_no)                        + bcolors.ENDC)
    
    print(bcolors.GREEN + '\nWITH SELECTION: \n' + bcolors.ENDC)

    print(bcolors.GREEN + 'NB_OF_FEATURES: '   + str(X_Fit.shape[1])                + bcolors.ENDC)
    print(bcolors.GREEN + 'ACCURACY: '         + str(accuracy)                      + bcolors.ENDC)
    print(bcolors.GREEN + 'PRECISION: '        + str(calculatePrecision(matrix))    + bcolors.ENDC)
    print(bcolors.GREEN + 'FPT_TPR: '          + str(calculateFPTandTPR(matrix))    + bcolors.ENDC)
    print(bcolors.GREEN + 'F1 SCORE: '         + str(calculateF1(matrix))           + bcolors.ENDC)
    print(bcolors.GREEN + 'MATRIX: \n'         + str(matrix)                        + bcolors.ENDC)
