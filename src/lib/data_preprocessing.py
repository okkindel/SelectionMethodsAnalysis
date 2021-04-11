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

def parseSafeDriverData(df):
    labels = df.columns[2:]
    X_tab = df[labels]
    y_tab = df['target']
    X, y = X_tab.values, y_tab.values
    return [X, y]

def parseInsuranceData(df):
    df.drop(['id'], axis=1, inplace=True)
    X_tab = df.drop('Response', axis=1)
    y_tab = df['Response']
    X_tab.loc[X_tab['Gender'] == 'Male', 'Gender'] = 1
    X_tab.loc[X_tab['Gender'] == 'Female', 'Gender'] = 0
    X_tab.loc[X_tab['Vehicle_Age'] == '> 2 Years', 'Vehicle_Age'] = 2
    X_tab.loc[X_tab['Vehicle_Age'] == '1-2 Year', 'Vehicle_Age'] = 1
    X_tab.loc[X_tab['Vehicle_Age'] == '< 1 Year', 'Vehicle_Age'] = 0
    X_tab.loc[X_tab['Vehicle_Damage'] == 'Yes', 'Vehicle_Damage'] = 1
    X_tab.loc[X_tab['Vehicle_Damage'] == 'No', 'Vehicle_Damage'] = 0
    
    for col in train.columns:
        X_tab[col] = X_tab[col].astype(np.int32)
    
    X, y = X_tab.values, y_tab.values
    
    return [X, y]

def getCreditCardData():
    df = pd.read_csv('../data/creditcard.csv')
    return parseCreditCardData(df)

def getSafeDriverData():
    df = pd.read_csv('../data/porto-seguro-safe-driver.csv')
    return parseSafeDriverData(df)

def getInsuranceData():
    df = pd.read_csv('../data/health_insurance_cross_sell.csv')
    return parseInsuranceData(df)

def getCustomData():
    df = pd.read_csv('../data/custom_100000.csv')
    data  = df.values
    X, y = data[:, :20], data[:, 20]
    return [X, y]

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
    