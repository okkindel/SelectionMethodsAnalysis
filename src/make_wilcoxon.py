from lib.data_preprocessing import getCcfd, getCustom, getInsurance, getMushroom, getKeel
from lib.summary import make_simple_summary, wicloxon_string_summary, wilcoxon_header
from lib.feature_selection import reverseMatrix, calculateF1, calculateWilcoxon
from lib.data_preprocessing import PART_1, PART_2, PART_3, PART_4
from lib.classification import get_average_score
import pandas as pd
import random
import math

from lib.methods.information_gain import information_gain
from lib.methods.correlation_coef import correlation_coef
from lib.methods.chi_square import chi_square
from lib.methods.relief import relief
from lib.methods.anova import anova

DATA_PART = 'part4'
ALPHA = 0.1

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def get_part_of_set(set, part):
    return int(math.floor(part * len(set)))

def get_method(method, elements, feats):
    [X, y] = elements
    return {
        'ANOVA':                anova(X, y, feats),
        'RELIEF':               relief(X, y, feats),
        'INFORATION GAIN':      information_gain(X, y, feats),
        'CHI SQUARE':           chi_square(X, y, feats),
        'CORRELATION COEF':     correlation_coef(X, y, feats),
    }[method]

def make_closest(file, method, set, subsets, results, set_len):
    found = False
    
    for feats in range (1, set_len):
        custom_res = []

        for subset in subsets:
            X_Fit, scores = get_method(method, subset, feats)
            accuracy, matrix = get_average_score(X_Fit, subset[1])
            matrix_rev = reverseMatrix(matrix)
            custom_res.append(calculateF1(matrix_rev))

        try: _, p = calculateWilcoxon(results, custom_res)
        except ValueError: p = 0
        
        make_simple_summary(method, set, X_Fit, accuracy, matrix_rev, scores, wilcoxon=p, original=results, new=custom_res)
        
        if (p < ALPHA):
            print('FOUND - ORIGINAL NB: ' + str(set_len) + ' - NEW NB: ' + str(feats) + '\n')
            file.write(wicloxon_string_summary(method, set, X_Fit, scores, p, custom_res))
            found = True
            break
    
    if (not(found)):
        print('NOT FOUND - ROLLBACK\n')
        file.write(wicloxon_string_summary(method, set, X_Fit, scores, 0, results))

def make_experiment(file, set, elements):
    [X, y] = elements

    table = pd.DataFrame(X)
    table['y'] = y
    table.sort_values('y', inplace=True)
    print(table)
    X_tab = table.drop('y', axis=1)
    y_tab = table['y']
    X, y = X_tab.values, y_tab.values


    random_subset0 = [X, y]
    random_subset1 = [X[0:get_part_of_set(X, 0.4)], y[0:get_part_of_set(y, 0.4)]]
    random_subset2 = [X[get_part_of_set(X, 0.2):len(X)], y[get_part_of_set(y, 0.2):len(X)]]
    random_subset3 = [X[0::2], y[0::2]]
    random_subset4 = [X[0::3], y[0::3]]
    
    subsets = [random_subset0, random_subset1, random_subset2, random_subset3, random_subset4]
    results = []

    for subset in subsets:
        accuracy, matrix = get_average_score(subset[0], subset[1])
        matrix_rev = reverseMatrix(matrix)
        results.append(calculateF1(matrix_rev))

    file.write(wicloxon_string_summary('NO SELECTION', set, X, ['all'], 0, results))

    ALL_METHODS = ['ANOVA', 'RELIEF', 'INFORATION GAIN', 'CHI SQUARE', 'CORRELATION COEF']
    
    for method in ALL_METHODS:
        make_closest(file, method, set, subsets, results, X.shape[1])

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

file = open('wilcoxon_' + DATA_PART + '.csv', 'w')
file.write(wilcoxon_header())
makePart(DATA_PART)
file.close()
