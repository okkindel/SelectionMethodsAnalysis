from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math

def confMatrix(matrix):
    TP = float(matrix[0])
    TN = float(matrix[3])
    FP = float(matrix[1])
    FN = float(matrix[2])
    return TP, TN, FP, FN

def makeData(arr, dataToMake):
    res = []
    for matrix in arr['matrix']:
        unpacked = matrix.replace('[', '').replace(']', '').split()
        TP, TN, FP, FN = confMatrix(unpacked)

        if ((TN+FP) == 0):
            tnfp = 0.00001
        else:
            tnfp = TN + FP

        precision = TN/(TN+FN)
        reacll = TN/(tnfp)

        if ((precision + reacll) == 0):
            pr = 0.00001
        else:
            pr = precision + reacll

        f1 = (2 * precision * reacll) / (pr)
        
        if (dataToMake == 'precision'):
            res.append(precision)
        elif (dataToMake == 'recall'):
            res.append(reacll)
        else:
            res.append(f1)
            
    return res

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

def makeF1Chart():
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
    
    feature = np.arange(len(no))
    for set in no['dataset']:
        classes.append(str(set))
    # for dataset, method, num_of_feat, num_of_elems, accuracy, precision, ftp, tpr, f1_score, matrix in zip(
    #     df['dataset'], df['method'], df['num_of_feat'], df['num_of_elems'], df['accuracy'],
    #     df['precision'], df['ftp'], df['tpr'], df['f1_score'], df['matrix']
    # ):
    #     classes.append(str(dataset))

    plt.plot(feature, makeData(an, 'f1'), linestyle='-', marker='o', color='g', label="ANOVA")
    plt.plot(feature, makeData(re, 'f1'), linestyle='-', marker='o', color='b', label="RELIEF")
    plt.plot(feature, makeData(ig, 'f1'), linestyle='-', marker='o', color='c', label="INFORATION GAIN")
    plt.plot(feature, makeData(cs, 'f1'), linestyle='-', marker='o', color='m', label="CHI SQUARE")
    plt.plot(feature, makeData(cc, 'f1'), linestyle='-', marker='o', color='y', label="CORRELATION COEF")
    plt.plot(feature, makeData(no, 'f1'), linestyle='-', marker='o', color='r', label="NO SELECTION")

    plt.ylabel('F1 Score')
    plt.xlabel('Zbiór')
    plt.xticks(feature, classes)
    plt.xticks(rotation=90)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', prop=fontP)
    plt.show()

def makeMeanChart():
    df = pd.read_csv("../../results/complete.csv", sep=",")
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(5, 3))
    
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]
    
    axes[0].grid()
    axes[0].bar(height=np.mean(makeData(no, 'f1')), edgecolor='black', color='red', x="NO SELECTION")
    axes[0].bar(height=np.mean(makeData(an, 'f1')), edgecolor='black', color='azure', x="ANOVA")
    axes[0].bar(height=np.mean(makeData(re, 'f1')), edgecolor='black', color='aqua', x="RELIEF")
    axes[0].bar(height=np.mean(makeData(ig, 'f1')), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[0].bar(height=np.mean(makeData(cs, 'f1')), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[0].bar(height=np.mean(makeData(cc, 'f1')), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[0].set_title('Uśrednione wyniki F1 Score')
    axes[0].tick_params(labelrotation=20)
    axes[0].set_ylim([0, 0.6])
    
    axes[1].grid()
    axes[1].bar(height=np.mean(makeData(no, 'precision')), edgecolor='black', color='red', x="NO SELECTION")
    axes[1].bar(height=np.mean(makeData(an, 'precision')), edgecolor='black', color='azure', x="ANOVA")
    axes[1].bar(height=np.mean(makeData(re, 'precision')), edgecolor='black', color='aqua', x="RELIEF")
    axes[1].bar(height=np.mean(makeData(ig, 'precision')), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[1].bar(height=np.mean(makeData(cs, 'precision')), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[1].bar(height=np.mean(makeData(cc, 'precision')), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[1].set_title('Uśrednione wyniki precyzji')
    axes[1].tick_params(labelrotation=20)
    axes[1].set_ylim([0, 0.6])

    axes[2].grid()
    axes[2].bar(height=np.mean(makeData(no, 'recall')), edgecolor='black', color='red', x="NO SELECTION")
    axes[2].bar(height=np.mean(makeData(an, 'recall')), edgecolor='black', color='azure', x="ANOVA")
    axes[2].bar(height=np.mean(makeData(re, 'recall')), edgecolor='black', color='aqua', x="RELIEF")
    axes[2].bar(height=np.mean(makeData(ig, 'recall')), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[2].bar(height=np.mean(makeData(cs, 'recall')), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[2].bar(height=np.mean(makeData(cc, 'recall')), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[2].set_title('Uśrednione wyniki czułości')
    axes[2].tick_params(labelrotation=20)
    axes[2].set_ylim([0, 0.6])

    plt.show()

makeMeanChart()