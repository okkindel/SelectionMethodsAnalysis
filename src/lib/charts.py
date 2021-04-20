from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def makePCAChart(X, y, title='redukcja PCA'):
    df = pd.DataFrame(X)
    df['target'] = y
    colors = ["#0101DF", "#DF0101"]
    markers = ['o', 's']
    _, ax = plt.subplots(1, 1, figsize=(8,8))
    
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)
    
    for l, c, m in zip(np.unique(y), colors, markers):
        plt.scatter(
            X[y==l, 0],
            X[y==l, 1],
            c=c, label=l, marker=m
        )
    plt.legend(loc='upper right')
    
    ax.set_title(title, fontsize=14)
    ax.set_xlim()
    
    plt.show()

def makeFullChart(X, y, title1='Dystrybucja klas', title2='Dystrybucja danych (redukcja PCA)'):
    df = pd.DataFrame(X)
    df['target'] = y
    colors = ["#0101DF", "#DF0101"]
    markers = ['o', 's']
    fig, ax = plt.subplots(1, 2, figsize=(18,4))
    
    sns.countplot('target', data=df, ax=ax[0], palette=colors)
    ax[0].set_title(title1, fontsize=14)
    ax[0].set_xlim()
    
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)
    
    for l, c, m in zip(np.unique(y), colors, markers):
        plt.scatter(
            X[y==l, 0],
            X[y==l, 1],
            c=c, label=l, marker=m
        )
    plt.legend(loc='upper right')
    
    ax[1].set_title(title2, fontsize=14)
    ax[1].set_xlim()
    
    plt.show()

def makePrecChart():
    df = pd.read_csv("../../results/complete.csv", sep=",")
    
    fontP = FontProperties()
    fontP.set_size('xx-small')
    classes = []
    
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]

    # for dataset, method, num_of_feat, num_of_elems, accuracy, precision, ftp, tpr, f1_score, matrix in zip(
    #     df['dataset'], df['method'], df['num_of_feat'], df['num_of_elems'], df['accuracy'],
    #     df['precision'], df['ftp'], df['tpr'], df['f1_score'], df['matrix']
    # ):
    #     classes.append(str(dataset))

    feature = np.arange(len(no))
    for set in no['dataset']:
        classes.append(str(set))

    plt.plot(feature, no['f1_score'], linestyle='-', marker='o', color='r', label="NO SELECTION")
    plt.plot(feature, an['f1_score'], linestyle='-', marker='o', color='g', label="ANOVA")
    plt.plot(feature, re['f1_score'], linestyle='-', marker='o', color='b', label="RELIEF")
    plt.plot(feature, ig['f1_score'], linestyle='-', marker='o', color='c', label="INFORATION GAIN")
    plt.plot(feature, cs['f1_score'], linestyle='-', marker='o', color='m', label="CHI SQUARE")
    plt.plot(feature, cc['f1_score'], linestyle='-', marker='o', color='y', label="CORRELATION COEF")

    plt.ylabel('F1 Score')
    plt.xlabel('Zbiór')
    plt.xticks(feature, classes)
    plt.xticks(rotation=90)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
    plt.show()

makePrecChart()