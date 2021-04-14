from lib.feature_selection import get_average_score
# from lib.data_preprocessing import getMushroomData
from lib.summary import make_simple_summary
from lib.charts import makePCAChart
from lib.parse import parseKEEL

from lib.methods.information_gain import information_gain
from lib.methods.correlation_coef import correlation_coef
from lib.methods.chi_square import chi_square
from lib.methods.relief import relief
from lib.methods.anova import anova

[X, y] = parseKEEL('../data/wine.dat')

accuracy_no, matrix_no = get_average_score(X, y)
make_simple_summary(X, accuracy_no, matrix_no, 'NO SELECTION')

X_Fit = anova(X, y, 5)
accuracy, matrix = get_average_score(X_Fit, y)
make_simple_summary(X_Fit, accuracy, matrix, 'ANOVA')

X_Fit = relief(X, y, 5)
accuracy, matrix = get_average_score(X_Fit, y)
make_simple_summary(X_Fit, accuracy, matrix, 'RELIEF')

X_Fit = information_gain(X, y, 5)
accuracy, matrix = get_average_score(X_Fit, y)
make_simple_summary(X_Fit, accuracy, matrix, 'INFORATION GAIN')

X_Fit = chi_square(X, y, 5)
accuracy, matrix = get_average_score(X_Fit, y)
make_simple_summary(X_Fit, accuracy, matrix, 'CHI SQUARE')

X_Fit = correlation_coef(X, y, 5)
accuracy, matrix = get_average_score(X_Fit, y)
make_simple_summary(X_Fit, accuracy, matrix, 'CORRELATION COEF')
