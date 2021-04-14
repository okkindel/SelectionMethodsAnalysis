import numpy as np

def parseKEEL(dataset):
    from_file = []
    lines = open(dataset, 'r').readlines()
    idx = lines.index('@data\n') + 2
    y_pos = len(lines[idx].split(',')) - 1
    for line in lines[idx:]:
        el = line.strip().split(',')
        from_file.append(el)
    data = np.array(from_file, dtype=float)
    X, y = data[:, :y_pos], data[:, y_pos]
    return [X, y]