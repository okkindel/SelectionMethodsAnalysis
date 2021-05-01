from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

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

def makeF1Chart(df):
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

    plt.plot(feature, an['f1_score'], linestyle='-', marker='o', color='g', label="ANOVA")
    plt.plot(feature, re['f1_score'], linestyle='-', marker='o', color='b', label="RELIEF")
    plt.plot(feature, ig['f1_score'], linestyle='-', marker='o', color='c', label="INFORATION GAIN")
    plt.plot(feature, cs['f1_score'], linestyle='-', marker='o', color='m', label="CHI SQUARE")
    plt.plot(feature, cc['f1_score'], linestyle='-', marker='o', color='y', label="CORRELATION COEF")
    plt.plot(feature, no['f1_score'], linestyle='-', marker='o', color='r', label="NO SELECTION")

    plt.ylabel('F1 Score')
    plt.xlabel('Zbiór')
    plt.xticks(feature, classes)
    plt.xticks(rotation=90)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', prop=fontP)
    plt.show()

def makeMeanChart(df):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(5, 3))
    
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]
    
    axes[0].grid()
    axes[0].bar(height=np.mean(no['f1_score']), edgecolor='black', color='red', x="NO SELECTION")
    axes[0].bar(height=np.mean(an['f1_score']), edgecolor='black', color='azure', x="ANOVA")
    axes[0].bar(height=np.mean(re['f1_score']), edgecolor='black', color='aqua', x="RELIEF")
    axes[0].bar(height=np.mean(ig['f1_score']), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[0].bar(height=np.mean(cs['f1_score']), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[0].bar(height=np.mean(cc['f1_score']), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[0].set_title('Uśrednione wyniki F1 Score')
    axes[0].tick_params(labelrotation=40)
    axes[0].set_ylim([0.3, 0.9])
    
    axes[1].grid()
    axes[1].bar(height=np.mean(no['precision']), edgecolor='black', color='red', x="NO SELECTION")
    axes[1].bar(height=np.mean(an['precision']), edgecolor='black', color='azure', x="ANOVA")
    axes[1].bar(height=np.mean(re['precision']), edgecolor='black', color='aqua', x="RELIEF")
    axes[1].bar(height=np.mean(ig['precision']), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[1].bar(height=np.mean(cs['precision']), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[1].bar(height=np.mean(cc['precision']), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[1].set_title('Uśrednione wyniki precyzji')
    axes[1].tick_params(labelrotation=40)
    axes[1].set_ylim([0.3, 0.9])

    axes[2].grid()
    axes[2].bar(height=np.mean(no['balanced_acc']), edgecolor='black', color='red', x="NO SELECTION")
    axes[2].bar(height=np.mean(an['balanced_acc']), edgecolor='black', color='azure', x="ANOVA")
    axes[2].bar(height=np.mean(re['balanced_acc']), edgecolor='black', color='aqua', x="RELIEF")
    axes[2].bar(height=np.mean(ig['balanced_acc']), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[2].bar(height=np.mean(cs['balanced_acc']), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[2].bar(height=np.mean(cc['balanced_acc']), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[2].set_title('Uśrednione wyniki dokładności zbalansowanej')
    axes[2].tick_params(labelrotation=40)
    axes[2].set_ylim([0.3, 0.9])

    plt.show()
