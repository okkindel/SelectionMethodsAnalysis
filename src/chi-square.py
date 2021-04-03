from lib.feature_selection import get_average_score, calculatePrecision, calculateFPTandTPR
import numpy as np

from_file = []
f = open('../data/wine.dat', 'r')
for line in f.readlines()[19:]:
    el = line.strip().split(',')
    from_file.append(el)

data = np.array(from_file, dtype=float)
X, y = data[:, :13], data[:, 13]

accuracy, matrix = get_average_score(X, y)

print('accuracy')
print(accuracy)
print('precision')
print(calculatePrecision(matrix))
print('fpt tpr')
print(calculateFPTandTPR(matrix))
