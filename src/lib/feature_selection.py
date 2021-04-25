from scipy.stats import wilcoxon
import numpy as np

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

# calculating balanced accuracy
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

def calculateWilcoxon(original, new):
    stat, p = wilcoxon(original, new)
    return stat, p
