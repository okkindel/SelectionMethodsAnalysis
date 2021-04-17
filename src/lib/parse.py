from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import math

def parseKEEL(dataset):
    from_file = []
    lines = open(dataset, 'r').readlines()
    idx = lines.index('@data\n') + 1
    y_pos = len(lines[idx].split(',')) - 1
    for line in lines[idx:]:
        el = line.strip().split(',')
        from_file.append(el)
    data = np.array(from_file)
    X, y_tab = data[:, :y_pos], data[:, y_pos]
    
    X_tab = pd.DataFrame(X)
    Encoder_X = LabelEncoder() 
    for col in X_tab.columns:
        try:
            float(X_tab[col][0])
        except ValueError:
            X_tab[col] = Encoder_X.fit_transform(X_tab[col])
        
    
    y_tab[y_tab == ' positive'] = 1
    y_tab[y_tab == ' negative'] = 0
    
    X_res = np.array(X_tab.values, dtype=float)
    
    return [X_res, y_tab]
