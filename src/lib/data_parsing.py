from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
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

def parseMushroomData(df):
    df = df[(df['class'] != 'p') | (df.index % 10 == 1)]
    labels = df.columns[1:]
    X_tab = df[labels]
    y_tab = df['class']
    Encoder_X = LabelEncoder() 
    for col in X_tab.columns:
        X_tab[col] = Encoder_X.fit_transform(X_tab[col])
    
    y_tab = Encoder_X.fit_transform(y_tab)
    X, y = X_tab.values, y_tab
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
    
    for col in X_tab.columns:
        X_tab[col] = X_tab[col].astype(np.int32)
    
    X, y = X_tab.values, y_tab.values
    return [X, y]