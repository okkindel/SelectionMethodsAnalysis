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
    [X, y] = parseKEEL('../data/KEEL/part4/' + set)
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

part1 = [
    'ecoli-0_vs_1.dat',
    'ecoli1.dat',
    'ecoli2.dat',
    'ecoli3.dat',
    'glass0.dat',
    'glass1.dat',
    'glass6.dat',
    # 'haberman.dat',
    # 'iris0.dat',
    'new-thyroid1.dat',
    'newthyroid2.dat',
    'page-blocks0.dat',
    'pima.dat',
    'segment0.dat',
    'vehicle0.dat',
    'vehicle1.dat',
    'vehicle2.dat',
    'vehicle3.dat',
    'wisconsin.dat',
    'yeast1.dat',
    'yeast3.dat',
]

part2 = [
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

part3 = [
    'ecoli-0-6-7_vs_5.dat',
    'ecoli-0-2-3-4_vs_5.dat',
    'ecoli-0-6-7_vs_3-5.dat',
    'ecoli-0-2-6-7_vs_3-5.dat',
    'yeast-0-2-5-6_vs_3-7-8-9.dat',
    'ecoli-0-1-4-7_vs_5-6.dat',
    'glass-0-1-4-6_vs_2.dat',
    'ecoli-0-1_vs_5.dat',
    'glass-0-4_vs_5.dat',
    # 'cleveland-0_vs_4.dat',
    'ecoli-0-3-4-6_vs_5.dat',
    'yeast-0-3-5-9_vs_7-8.dat',
    'ecoli-0-4-6_vs_5.dat',
    'yeast-0-2-5-7-9_vs_3-6-8.dat',
    'ecoli-0-3-4_vs_5.dat',
    'ecoli-0-1_vs_2-3-5.dat',
    'glass-0-1-5_vs_2.dat',
    'ecoli-0-1-4-7_vs_2-3-5-6.dat',
    'glass-0-6_vs_5.dat',
    'ecoli-0-1-4-6_vs_5.dat',
    'led7digit-0-2-4-5-6-7-8-9_vs_1.dat',
    'ecoli-0-3-4-7_vs_5-6.dat',
]

part4 = [
    'kr-vs-k-zero_vs_eight.dat',                                                                                   
    'zoo-3.dat',                                                                                                   
    'kr-vs-k-one_vs_fifteen.dat',                                                                                  
    'winequality-red-4.dat',                                                                                       
    'dermatology-6.dat',                                                                                           
    'shuttle-2_vs_5.dat',                                                                                          
    'winequality-white-3-9_vs_5.dat',                                                                              
    'winequality-red-3_vs_5.dat',
    'winequality-red-8_vs_6-7.dat',
    'kddcup-rootkit-imap_vs_back.dat',
    'kddcup-guess_passwd_vs_satan.dat',
    'kddcup-buffer_overflow_vs_back.dat',
    'abalone-19_vs_10-11-12-13.dat',
    'abalone-17_vs_7-8-9-10.dat',
    'poker-8-9_vs_6.dat',
    'shuttle-6_vs_2-3.dat',
    'kddcup-land_vs_portsweep.dat',
    'poker-9_vs_7.dat',
    # 'car-good.dat',
    'abalone-20_vs_8-9-10.dat',
    'lymphography-normal-fibrosis.dat',
    'abalone-3_vs_11.dat',
    'flare-F.dat',
    'winequality-white-3_vs_7.dat',
    'winequality-red-8_vs_6.dat',
    # 'car-vgood.dat',
    'kddcup-land_vs_satan.dat',
    'abalone-21_vs_8.dat',
    'kr-vs-k-zero-one_vs_draw.dat',
    'poker-8_vs_6.dat',
    'winequality-white-9_vs_4.dat',
    'kr-vs-k-zero_vs_fifteen.dat',
    'kr-vs-k-three_vs_eleven.dat',
    'poker-8-9_vs_5.dat',
]

# file = open('basic_results.csv', 'w')
# make_experiment(file, getMushroomData(), 'MUSHROOM')
# make_experiment(file, getCustomData(), 'CUSTOM')
# make_experiment(file, getInsuranceData(), 'INSURANCE')
# make_experiment(file, getCreditCardData(), 'CREDIT_CARD')
# file.close()

file = open('part4.csv', 'w')
for set in part4:
    make_experiment(file, set)
file.close()
