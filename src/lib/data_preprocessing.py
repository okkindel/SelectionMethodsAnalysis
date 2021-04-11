from sklearn.preprocessing import RobustScaler
import pandas as pd
import numpy as np

def parseCreditCardData(df):
    rob_scaler = RobustScaler()
    
    df['scaled_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1,1))
    df['scaled_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1,1))
    
    df.drop(['Time','Amount'], axis=1, inplace=True)
    scaled_amount = df['scaled_amount']
    scaled_time = df['scaled_time']
    df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)
    df.insert(0, 'scaled_amount', scaled_amount)
    df.insert(1, 'scaled_time', scaled_time)
    
    X_tab = df.drop('Class', axis=1)
    y_tab = df['Class']
    X, y = X_tab.values, y_tab.values

    return [X, y]

def getCreditCardData():
    df = pd.read_csv('../data/creditcard.csv')
    return parseCreditCardData(df)

def getHeartData():
    from_file = []
    f = open('../data/heart.dat', 'r')
    for line in f.readlines()[0:]:
        el = line.strip().split(' ')
        from_file.append(el)
    data = np.array(from_file, dtype=float)
    X, y = data[:, :13], data[:, 13]
    return [X, y]

def getWineData():
    from_file = []
    f = open('../data/wine.dat', 'r')
    for line in f.readlines()[19:]:
        el = line.strip().split(',')
        from_file.append(el)
    data = np.array(from_file, dtype=float)
    X, y = data[:, :13], data[:, 13]
    return [X, y]
    