from sklearn.preprocessing import MinMaxScaler
import pandas as pd

X = []
X_Norm = MinMaxScaler().fit_transform(X)

# mikrouśrednianie

def parseSafeDriverData(df):
    labels = df.columns[2:]
    X_tab = df[labels]
    y_tab = df['target']
    X, y = X_tab.values, y_tab.values
    return [X, y]

def getSafeDriverData():
    df = pd.read_csv('../data/porto-seguro-safe-driver.csv')
    return parseSafeDriverData(df)