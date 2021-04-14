from sklearn.preprocessing import LabelEncoder
import numpy as np

def parseKEEL(dataset):
    from_file = []
    lines = open(dataset, 'r').readlines()
    idx = lines.index('@data\n') + 2
    y_pos = len(lines[idx].split(',')) - 1
    for line in lines[idx:]:
        el = line.strip().split(',')
        from_file.append(el)
    data = np.array(from_file)
    Encoder_X = LabelEncoder()
    X, y_tab = data[:, :y_pos], data[:, y_pos]
    X = np.array(X, dtype=float)
    y = Encoder_X.fit_transform(y_tab)
    return [X, y]