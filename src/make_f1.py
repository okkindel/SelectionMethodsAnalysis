from lib.data_preprocessing import getCcfd, getCustom, getInsurance, getMushroom, getKeel
from lib.feature_selection import reverseMatrix, calculateF1, calculateWilcoxon
from lib.summary import make_simple_summary, get_string_summary, get_header
from lib.data_preprocessing import PART_1, PART_2, PART_3, PART_4
from lib.classification import get_average_score

from lib.methods.information_gain import information_gain
from lib.methods.correlation_coef import correlation_coef
from lib.methods.chi_square import chi_square
from lib.methods.relief import relief
from lib.methods.anova import anova

MODE = 'closest' # closest / best
DATA_PART = 'part4'
ALPHA = 0.05

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def get_method(method, elements, feats):
    [X, y] = elements
    return {
        'ANOVA':                anova(X, y, feats),
        'RELIEF':               relief(X, y, feats),
        'INFORATION GAIN':      information_gain(X, y, feats),
        'CHI SQUARE':           chi_square(X, y, feats),
        'CORRELATION COEF':     correlation_coef(X, y, feats),
    }[method]

def make_closest(file, method, set, elements, basic_f1):
    [X, y] = elements
    
    found = False
    for feats in range (1, X.shape[1]):
        X_Fit, scores = get_method(method, elements, feats)
        accuracy, matrix = get_average_score(X_Fit, y)
        matrix_rev = reverseMatrix(matrix)
        new_f1 = calculateF1(matrix_rev)
        p = abs(new_f1 - basic_f1)
        make_simple_summary(method, set, X_Fit, accuracy, matrix_rev, scores)

        if (p < ALPHA):
            print('FOUND - ORIGINAL NB: ' + str(X.shape[1]) + ' - NEW NB: ' + str(X_Fit.shape[1]) + '\n')
            file.write(get_string_summary(method, set, X_Fit, accuracy, matrix_rev, scores))
            found = True
            break
    
    if (not(found)):
        print('NOT FOUND - ROLLBACK\n')
        X_Fit, scores = get_method(method, elements, X.shape[1])
        accuracy, matrix = get_average_score(X_Fit, y)
        matrix_rev = reverseMatrix(matrix)
        file.write(get_string_summary(method, set, X_Fit, accuracy, matrix_rev, scores))

def make_best(file, method, set, elements):
    [X, y] = elements
    best_num_of_feats = 0
    best_f1 = 0
    
    for feats in range (1, X.shape[1]):
        X_Fit, scores = get_method(method, elements, feats)
        accuracy, matrix = get_average_score(X_Fit, y)
        matrix_rev = reverseMatrix(matrix)
        new_f1 = calculateF1(matrix_rev)
        make_simple_summary(method, set, X_Fit, accuracy, matrix_rev, scores)

        if (new_f1 > best_f1):
            best_f1 = new_f1
            best_num_of_feats = feats
    
    print('\nBEST FOR: ' + str(feats) + '\n')
    X_Fit, scores = get_method(method, elements, best_num_of_feats)
    accuracy, matrix = get_average_score(X_Fit, y)
    matrix_rev = reverseMatrix(matrix)
    make_simple_summary(method, set, X_Fit, accuracy, matrix_rev, scores)
    file.write(get_string_summary(method, set, X_Fit, accuracy, matrix_rev, scores))

def make_experiment(file, set, elements):
    [X, y] = elements
    
    accuracy, matrix = get_average_score(X, y)
    matrix_rev = reverseMatrix(matrix)

    make_simple_summary('NO SELECTION', set, X, accuracy, matrix_rev, ['all'])
    file.write(get_string_summary('NO SELECTION', set, X, accuracy, matrix_rev, ['all']))
    basic_f1 = calculateF1(matrix_rev)
    
    ALL_METHODS = ['ANOVA', 'RELIEF', 'INFORATION GAIN', 'CHI SQUARE', 'CORRELATION COEF']
    
    if (MODE == 'closest'):
        for method in ALL_METHODS:
            make_closest(file, method, set, elements, basic_f1)
    elif (MODE == 'best'):
        for method in ALL_METHODS:
            make_best(file, method, set, elements)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def makePart(part):
    if (part == 'part0'):
        make_experiment(file, 'INSURANCE',      getInsurance())
        make_experiment(file, 'MUSHROOM',       getMushroom())
        make_experiment(file, 'CUSTOM',         getCustom())
        make_experiment(file, 'CREDIT_CARD',    getCcfd())
    elif (part == 'part1'):
        for set in PART_1:
            elements = getKeel('../data/KEEL/part1/' + set)
            make_experiment(file, set, elements)
    elif (part == 'part2'):
        for set in PART_2:
            elements = getKeel('../data/KEEL/part2/' + set)
            make_experiment(file, set, elements)
    elif (part == 'part3'):
        for set in PART_3:
            elements = getKeel('../data/KEEL/part3/' + set)
            make_experiment(file, set, elements)
    elif (part == 'part4'):
        for set in PART_4:
            elements = getKeel('../data/KEEL/part4/' + set)
            make_experiment(file, set, elements)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

file = open('f1_' + MODE + '-' + DATA_PART + '.csv', 'w')
file.write(get_header())
makePart(DATA_PART)
file.close()
