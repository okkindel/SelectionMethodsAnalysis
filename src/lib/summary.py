from lib.feature_selection import calculatePrecision, calculateFPR_TPR_TNR, calculateF1, calculateRecall, calculateBalancedAcc
from numpy import array2string

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def make_simple_summary(method, set, X, accuracy, matrix, scores, wilcoxon = 0, original = [], new  = []):
    print(bcolors.YELLOW + 'SET: '              + str(set)                           + bcolors.ENDC)
    print(bcolors.YELLOW + 'METHOD: '           + str(method)                        + bcolors.ENDC)
    print(bcolors.GREEN  + 'NB_OF_FEATURES: '   + str(X.shape[1])                    + bcolors.ENDC)
    print(bcolors.GREEN  + 'NB_OF_ELEMENTS: '   + str(X.shape[0])                    + bcolors.ENDC)
    print(bcolors.GREEN  + 'ACCURACY: '         + str(accuracy)                      + bcolors.ENDC)
    print(bcolors.GREEN  + 'BALANCED ACC: '     + str(calculateBalancedAcc(matrix))  + bcolors.ENDC)
    print(bcolors.GREEN  + 'PRECISION: '        + str(calculatePrecision(matrix))    + bcolors.ENDC)
    print(bcolors.GREEN  + 'RECALL: '           + str(calculateRecall(matrix))       + bcolors.ENDC)
    print(bcolors.BOLD   + 'F1 SCORE: '         + str(calculateF1(matrix))           + bcolors.ENDC)
    print(bcolors.GREEN  + 'TPR FPR TNR: '      + str(calculateFPR_TPR_TNR(matrix))  + bcolors.ENDC)
    print(bcolors.GREEN  + 'MATRIX: '           + str(matrix).replace('\n', '')      + bcolors.ENDC)
    print(bcolors.GREEN  + 'SCORES: '           + str(scores)                        + bcolors.ENDC)
    print(bcolors.BOLD   + 'WILCOXON_P: '       + str(wilcoxon)                      + bcolors.ENDC)
    print(bcolors.GREEN  + 'ORIGINAL_RES: '     + str(original)                      + bcolors.ENDC)
    print(bcolors.GREEN  + 'NEW_RES     : '     + str(new)                           + bcolors.ENDC)
    print('\n')

def get_string_summary(method, set, X, accuracy, matrix, scores):
    return (set
        + '; ' + method
        + '; ' + str(X.shape[1])
        + '; ' + str(X.shape[0])
        + '; ' + str(accuracy)
        + '; ' + str(calculateBalancedAcc(matrix))
        + '; ' + str(calculatePrecision(matrix))
        + '; ' + str(calculateRecall(matrix))
        + '; ' + str(calculateF1(matrix))
        + '; ' + str(calculateFPR_TPR_TNR(matrix)).replace(' ', '')
        + '; ' + str(array2string(matrix, separator=',').replace('\n', '').replace(' ', ''))
        + '; ' + str(scores).replace(' ', '')
        + '\n')

def get_header():
    return ('dataset; method; num_of_feat; num_of_elems; accuracy; balanced_acc; precision; recall; f1_score; tpr_fpr_tnr; matrix; scores\n')

# WILCOXON

def wicloxon_string_summary(method, set, X, scores, wilcoxon, results):
    return (set
        + '; ' + method
        + '; ' + str(X.shape[1])
        + '; ' + str(wilcoxon)
        + '; ' + str(results).replace(' ', '')
        + '; ' + str(scores).replace(' ', '')
        + '\n')

def wilcoxon_header():
    return ('dataset; method; num_of_feat; wilcoxon_p; f1_results; scores\n')