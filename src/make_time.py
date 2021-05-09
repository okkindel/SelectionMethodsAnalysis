from lib.data_preprocessing import getCcfd, getCustom, getInsurance, getMushroom, getKeel
from lib.summary import make_simple_summary, get_string_summary, get_header
from lib.data_preprocessing import PART_1, PART_2, PART_3, PART_4
from lib.classification import get_average_score
from lib.feature_selection import reverseMatrix
import time

from lib.methods.information_gain import information_gain
from lib.methods.correlation_coef import correlation_coef
from lib.methods.chi_square import chi_square
from lib.methods.relief import relief
from lib.methods.anova import anova

import math

DATA_PART = 'part4'

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def make_experiment(file, set, elements):
    [X, y] = elements
    
    accuracy, matrix = get_average_score(X, y)
    maririx_rev = reverseMatrix(matrix)
    make_simple_summary('NO SELECTION', set, X, accuracy, maririx_rev, ['all'], 0)
    file.write(get_string_summary('NO SELECTION', set, X, accuracy, maririx_rev, ['all'], 0))
    
    feat_num = math.floor(X.shape[1] / 5 * 5)

    start = time.time()
    X_Fit, scores = anova(X, y, feat_num)
    end = time.time()
    accuracy, matrix = get_average_score(X_Fit, y)
    maririx_rev = reverseMatrix(matrix)
    make_simple_summary('ANOVA', set, X_Fit, accuracy, maririx_rev, scores, end - start)
    file.write(get_string_summary('ANOVA', set, X_Fit, accuracy, maririx_rev, scores, end - start))
    
    start = time.time()
    X_Fit, scores = relief(X, y, feat_num)
    end = time.time()
    accuracy, matrix = get_average_score(X_Fit, y)
    maririx_rev = reverseMatrix(matrix)
    make_simple_summary('RELIEF', set, X_Fit, accuracy, maririx_rev, scores, end - start)
    file.write(get_string_summary('RELIEF', set, X_Fit, accuracy, maririx_rev, scores, end - start))
    
    start = time.time()
    X_Fit, scores = information_gain(X, y, feat_num)
    end = time.time()
    accuracy, matrix = get_average_score(X_Fit, y)
    maririx_rev = reverseMatrix(matrix)
    make_simple_summary('INFORATION GAIN', set, X_Fit, accuracy, maririx_rev, scores, end - start)
    file.write(get_string_summary('INFORATION GAIN', set, X_Fit, accuracy, maririx_rev, scores, end - start))
    
    start = time.time()
    X_Fit, scores = chi_square(X, y, feat_num)
    end = time.time()
    accuracy, matrix = get_average_score(X_Fit, y)
    maririx_rev = reverseMatrix(matrix)
    make_simple_summary('CHI SQUARE', set, X_Fit, accuracy, maririx_rev, scores, end - start)
    file.write(get_string_summary('CHI SQUARE', set, X_Fit, accuracy, maririx_rev, scores, end - start))
    
    start = time.time()
    X_Fit, scores = correlation_coef(X, y, feat_num)
    end = time.time()
    accuracy, matrix = get_average_score(X_Fit, y)
    maririx_rev = reverseMatrix(matrix)
    make_simple_summary('CORRELATION COEF', set, X_Fit, accuracy, maririx_rev, scores, end - start)
    file.write(get_string_summary('CORRELATION COEF', set, X_Fit, accuracy, maririx_rev, scores, end - start))

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

file = open('time_' + DATA_PART + '.csv', 'w')
file.write(get_header())
makePart(DATA_PART)
file.close()