from lib.parse_data import parseCreditCardData, parseMushroomData, parseInsuranceData, parseKEEL
import pandas as pd

def getCreditCardData():
    df = pd.read_csv('../data/creditcard.csv')
    return parseCreditCardData(df)

def getInsuranceData():
    df = pd.read_csv('../data/health_insurance_cross_sell.csv')
    return parseInsuranceData(df)

def getMushroomData():
    df = pd.read_csv('../data/mushrooms.csv')
    return parseMushroomData(df)

def getCustomData():
    df = pd.read_csv('../data/custom_100000.csv')
    data  = df.values
    X, y = data[:, :20], data[:, 20]
    return [X, y]

def getKeelSet(dataset):
    return parseKEEL(dataset)
