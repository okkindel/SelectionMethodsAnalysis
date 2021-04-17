from lib.data_preprocessing import getCreditCardData, getCustomData, getInsuranceData, getMushroomData
from lib.summary import make_simple_summary, get_string_summary
from lib.feature_selection import get_average_score
from lib.charts import makePCAChart
from lib.parse import parseKEEL

from lib.methods.information_gain import information_gain
from lib.methods.correlation_coef import correlation_coef
from lib.methods.chi_square import chi_square
from lib.methods.relief import relief
from lib.methods.anova import anova

FEAT_NUMNER = 3

def make_experiment(file, set):
    # [X, y] = elements
    [X, y] = parseKEEL('../data/KEEL/part2/' + set)
    print(set + '\n')
    file.write(set + '\n')
    
    accuracy_no, matrix_no = get_average_score(X, y)
    make_simple_summary(X, accuracy_no, matrix_no, 'NO SELECTION')
    file.write(get_string_summary(X, accuracy_no, matrix_no, 'NO SELECTION'))
    
    X_Fit = anova(X, y, FEAT_NUMNER)
    accuracy, matrix = get_average_score(X_Fit, y)
    make_simple_summary(X_Fit, accuracy, matrix, 'ANOVA')
    file.write(get_string_summary(X_Fit, accuracy, matrix, 'ANOVA'))
    
    X_Fit = relief(X, y, FEAT_NUMNER)
    accuracy, matrix = get_average_score(X_Fit, y)
    make_simple_summary(X_Fit, accuracy, matrix, 'RELIEF')
    file.write(get_string_summary(X_Fit, accuracy, matrix, 'RELIEF'))
    
    X_Fit = information_gain(X, y, FEAT_NUMNER)
    accuracy, matrix = get_average_score(X_Fit, y)
    make_simple_summary(X_Fit, accuracy, matrix, 'INFORATION GAIN')
    file.write(get_string_summary(X_Fit, accuracy, matrix, 'INFORATION GAIN'))
    
    X_Fit = chi_square(X, y, FEAT_NUMNER)
    accuracy, matrix = get_average_score(X_Fit, y)
    make_simple_summary(X_Fit, accuracy, matrix, 'CHI SQUARE')
    file.write(get_string_summary(X_Fit, accuracy, matrix, 'CHI SQUARE'))
    
    X_Fit = correlation_coef(X, y, FEAT_NUMNER)
    accuracy, matrix = get_average_score(X_Fit, y)
    make_simple_summary(X_Fit, accuracy, matrix, 'CORRELATION COEF')
    file.write(get_string_summary(X_Fit, accuracy, matrix, 'CORRELATION COEF'))

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# sets = [
#     'ecoli-0_vs_1.dat',
#     'ecoli1.dat',
#     'ecoli2.dat',
#     'ecoli3.dat',
#     'glass0.dat',
#     'glass1.dat',
#     'glass6.dat',
#     # 'haberman.dat',
#     # 'iris0.dat',
#     'new-thyroid1.dat',
#     'newthyroid2.dat',
#     'page-blocks0.dat',
#     'pima.dat',
#     'segment0.dat',
#     'vehicle0.dat',
#     'vehicle1.dat',
#     'vehicle2.dat',
#     'vehicle3.dat',
#     'wisconsin.dat',
#     'yeast1.dat',
#     'yeast3.dat',
# ]

sets = [
    'yeast5.dat',
    'yeast-2_vs_8.dat',
    'yeast4.dat',
    'ecoli4.dat',
    'abalone9-18.dat',
    'glass2.dat',
    'glass4.dat',
    'yeast-1-2-8-9_vs_7.dat',
    'abalone19.dat',
    'yeast-1-4-5-8_vs_7.dat',
    'vowel0.dat',
    'yeast6.dat',
    'glass-0-1-6_vs_2.dat',
    'page-blocks-1-3_vs_4.dat',
    'shuttle-c0-vs-c4.dat',
    'yeast-2_vs_4.dat',
    'yeast-1_vs_7.dat',
    'shuttle-c2-vs-c4.dat',
    'glass-0-1-6_vs_5.dat',
    'yeast-0-5-6-7-9_vs_4.dat',
    'ecoli-0-1-3-7_vs_2-6.dat',
    'glass5.dat',
]

# file = open('basic_results.csv', 'w')
# make_experiment(file, getMushroomData(), 'MUSHROOM')
# make_experiment(file, getCustomData(), 'CUSTOM')
# make_experiment(file, getInsuranceData(), 'INSURANCE')
# make_experiment(file, getCreditCardData(), 'CREDIT_CARD')
# file.close()

file = open('results.csv', 'w')
for set in sets:
    make_experiment(file, set)
file.close()
