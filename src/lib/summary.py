from lib.feature_selection import calculatePrecision, calculateFPTandTPR

def make_summary(X, accuracy, accuracy_no, matrix, matrix_no):
    print('ORIGINAL_NB_OF_FEATURES: ', X.shape[1])
    print('ACCURACY_SELECTION: ', accuracy)
    print('ACCURACY_NO_SELECTION: ', accuracy_no)
    print('PRECISION_SELECTION: ', calculatePrecision(matrix))
    print('PRECISION_NO_SELECTION: ', calculatePrecision(matrix_no))
    print('FPT_TPR_SELECTION: ', calculateFPTandTPR(matrix))
    print('FPT_TPR_NO_SELECTION: ', calculateFPTandTPR(matrix_no))
    print('MATRIX: ', matrix)
    print('MATRIX_NO_SELECTION: ', matrix_no)
