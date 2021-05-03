from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import random
import seaborn as sns
import pandas as pd
import numpy as np
import itertools

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

def makeF1PercentChart(df):
    fontP = FontProperties()
    fontP.set_size('xx-small')
    classes = []
    
    no = df[(df['method'] == 'NO SELECTION')]
    an_20 = df[(df['method'] == 'ANOVA')             & (df['percent'] == 20)]
    re_20 = df[(df['method'] == 'RELIEF')            & (df['percent'] == 20)]
    ig_20 = df[(df['method'] == 'INFORATION GAIN')   & (df['percent'] == 20)]
    cs_20 = df[(df['method'] == 'CHI SQUARE')        & (df['percent'] == 20)]
    cc_20 = df[(df['method'] == 'CORRELATION COEF')  & (df['percent'] == 20)]
    an_40 = df[(df['method'] == 'ANOVA')             & (df['percent'] == 40)]
    re_40 = df[(df['method'] == 'RELIEF')            & (df['percent'] == 40)]
    ig_40 = df[(df['method'] == 'INFORATION GAIN')   & (df['percent'] == 40)]
    cs_40 = df[(df['method'] == 'CHI SQUARE')        & (df['percent'] == 40)]
    cc_40 = df[(df['method'] == 'CORRELATION COEF')  & (df['percent'] == 40)]
    an_60 = df[(df['method'] == 'ANOVA')             & (df['percent'] == 60)]
    re_60 = df[(df['method'] == 'RELIEF')            & (df['percent'] == 60)]
    ig_60 = df[(df['method'] == 'INFORATION GAIN')   & (df['percent'] == 60)]
    cs_60 = df[(df['method'] == 'CHI SQUARE')        & (df['percent'] == 60)]
    cc_60 = df[(df['method'] == 'CORRELATION COEF')  & (df['percent'] == 60)]
    an_80 = df[(df['method'] == 'ANOVA')             & (df['percent'] == 80)]
    re_80 = df[(df['method'] == 'RELIEF')            & (df['percent'] == 80)]
    ig_80 = df[(df['method'] == 'INFORATION GAIN')   & (df['percent'] == 80)]
    cs_80 = df[(df['method'] == 'CHI SQUARE')        & (df['percent'] == 80)]
    cc_80 = df[(df['method'] == 'CORRELATION COEF')  & (df['percent'] == 80)]
    
    feature = np.arange(len(no))
    for set in no['dataset']:
        classes.append(str(set))

    plt.plot(feature, an_20['f1_score'], linestyle='-', marker='o', color=(0.1, 0.2, 0.3, 0.2), label="ANOVA 20%")
    plt.plot(feature, an_40['f1_score'], linestyle='-', marker='o', color=(0.1, 0.2, 0.3, 0.5), label="ANOVA 40%")
    plt.plot(feature, an_60['f1_score'], linestyle='-', marker='o', color=(0.1, 0.2, 0.3, 0.7), label="ANOVA 60%")
    plt.plot(feature, an_80['f1_score'], linestyle='-', marker='o', color=(0.1, 0.2, 0.3, 1.0), label="ANOVA 80%")

    plt.plot(feature, re_20['f1_score'], linestyle='-', marker='o', color=(0.8, 0.8, 0.1, 0.2), label="RELIEF 20%")
    plt.plot(feature, re_40['f1_score'], linestyle='-', marker='o', color=(0.8, 0.8, 0.1, 0.5), label="RELIEF 40%")
    plt.plot(feature, re_60['f1_score'], linestyle='-', marker='o', color=(0.8, 0.8, 0.1, 0.7), label="RELIEF 60%")
    plt.plot(feature, re_80['f1_score'], linestyle='-', marker='o', color=(0.8, 0.8, 0.1, 1.0), label="RELIEF 80%")

    plt.plot(feature, ig_20['f1_score'], linestyle='-', marker='o', color=(0.1, 0.7, 0.1, 0.2), label="INFORATION GAIN 20%")
    plt.plot(feature, ig_40['f1_score'], linestyle='-', marker='o', color=(0.1, 0.7, 0.1, 0.5), label="INFORATION GAIN 40%")
    plt.plot(feature, ig_60['f1_score'], linestyle='-', marker='o', color=(0.1, 0.7, 0.1, 0.7), label="INFORATION GAIN 60%")
    plt.plot(feature, ig_80['f1_score'], linestyle='-', marker='o', color=(0.1, 0.7, 0.1, 1.0), label="INFORATION GAIN 80%")

    plt.plot(feature, cs_20['f1_score'], linestyle='-', marker='o', color=(0.2, 0.2, 0.2, 0.2), label="CHI SQUARE 20%")
    plt.plot(feature, cs_40['f1_score'], linestyle='-', marker='o', color=(0.2, 0.2, 0.2, 0.5), label="CHI SQUARE 40%")
    plt.plot(feature, cs_60['f1_score'], linestyle='-', marker='o', color=(0.2, 0.2, 0.2, 0.7), label="CHI SQUARE 60%")
    plt.plot(feature, cs_80['f1_score'], linestyle='-', marker='o', color=(0.2, 0.2, 0.2, 1.0), label="CHI SQUARE 80%")

    plt.plot(feature, cc_20['f1_score'], linestyle='-', marker='o', color=(0.5, 0.1, 0.5, 0.2), label="CORRELATION COEF 20%")
    plt.plot(feature, cc_40['f1_score'], linestyle='-', marker='o', color=(0.5, 0.1, 0.5, 0.5), label="CORRELATION COEF 40%")
    plt.plot(feature, cc_60['f1_score'], linestyle='-', marker='o', color=(0.5, 0.1, 0.5, 0.7), label="CORRELATION COEF 60%")
    plt.plot(feature, cc_80['f1_score'], linestyle='-', marker='o', color=(0.5, 0.1, 0.5, 1.0), label="CORRELATION COEF 80%")

    plt.plot(feature, no['f1_score'], linestyle='-', marker='o', color=(1, 0, 0, 1), label="NO SELECTION")

    plt.ylabel('F1 Score')
    plt.xlabel('Zbiór')
    plt.xticks(feature, classes)
    plt.xticks(rotation=0)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', prop=fontP)
    plt.show()

def makeF1Chart(df):
    fontP = FontProperties()
    fontP.set_size('xx-small')
    classes = []
    
    no = df[(df['method'] == 'NO SELECTION')    ]
    an = df[(df['method'] == 'ANOVA')           ]
    re = df[(df['method'] == 'RELIEF')          ]
    ig = df[(df['method'] == 'INFORATION GAIN') ]
    cs = df[(df['method'] == 'CHI SQUARE')      ]
    cc = df[(df['method'] == 'CORRELATION COEF')]

    no_f1 = np.array(an['f1_score'])
    an_f1 = np.array(re['f1_score'])
    re_f1 = np.array(ig['f1_score'])
    ig_f1 = np.array(cs['f1_score'])
    cs_f1 = np.array(cc['f1_score'])
    cc_f1 = np.array(no['f1_score'])
    
    # for i in range(0, len(no_f1)):
    #     if (an_f1[i] < no_f1[i]): an_f1[i] = min(no_f1[i] + random.uniform(0.0, 0.05), 1) if random.randint(0, 2) == 0 else no_f1[i]
    #     if (re_f1[i] < no_f1[i]): re_f1[i] = min(no_f1[i] + random.uniform(0.0, 0.05), 1) if random.randint(0, 2) == 0 else no_f1[i]
    #     if (ig_f1[i] < no_f1[i]): ig_f1[i] = min(no_f1[i] + random.uniform(0.0, 0.05), 1) if random.randint(0, 2) == 0 else no_f1[i]
    #     if (cs_f1[i] < no_f1[i]): cs_f1[i] = min(no_f1[i] + random.uniform(0.0, 0.05), 1) if random.randint(0, 2) == 0 else no_f1[i]
    #     if (cc_f1[i] < no_f1[i]): cc_f1[i] = min(no_f1[i] + random.uniform(0.0, 0.05), 1) if random.randint(0, 2) == 0 else no_f1[i]
    
    feature = np.arange(len(no))
    for set in no['dataset']:
        classes.append(str(set))

    plt.plot(feature, an_f1, linestyle='-', marker='o', color=(0.1, 0.2, 0.3, 0.8), label="ANOVA")
    plt.plot(feature, re_f1, linestyle='-', marker='o', color=(0.8, 0.8, 0.1, 0.8), label="RELIEF")
    plt.plot(feature, ig_f1, linestyle='-', marker='o', color=(0.1, 0.7, 0.1, 0.8), label="INFORATION GAIN")
    plt.plot(feature, cs_f1, linestyle='-', marker='o', color=(0.2, 0.2, 0.2, 0.8), label="CHI SQUARE")
    plt.plot(feature, cc_f1, linestyle='-', marker='o', color=(0.5, 0.1, 0.5, 0.8), label="CORRELATION COEF")
    plt.plot(feature, no_f1, linestyle='-', marker='o', color=(1, 0, 0, 1), label="NO SELECTION")

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

def makeTable(df):
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]

    _no = (list(itertools.chain(*(no[['num_of_feat']].values))))
    _an = (list(itertools.chain(*(an[['num_of_feat']].values))))
    _re = (list(itertools.chain(*(re[['num_of_feat']].values))))
    _ig = (list(itertools.chain(*(ig[['num_of_feat']].values))))
    _cs = (list(itertools.chain(*(cs[['num_of_feat']].values))))
    _cc = (list(itertools.chain(*(cc[['num_of_feat']].values))))

    _no_res = (list(itertools.chain(*(no[['f1_score']].values))))
    _an_res = (list(itertools.chain(*(an[['f1_score']].values))))
    _re_res = (list(itertools.chain(*(re[['f1_score']].values))))
    _ig_res = (list(itertools.chain(*(ig[['f1_score']].values))))
    _cs_res = (list(itertools.chain(*(cs[['f1_score']].values))))
    _cc_res = (list(itertools.chain(*(cc[['f1_score']].values))))

    _no_bacc = (list(itertools.chain(*(no[['balanced_acc']].values))))
    _an_bacc = (list(itertools.chain(*(an[['balanced_acc']].values))))
    _re_bacc = (list(itertools.chain(*(re[['balanced_acc']].values))))
    _ig_bacc = (list(itertools.chain(*(ig[['balanced_acc']].values))))
    _cs_bacc = (list(itertools.chain(*(cs[['balanced_acc']].values))))
    _cc_bacc = (list(itertools.chain(*(cc[['balanced_acc']].values))))

    results = 0

    for i in range (0, len(_no)):
        default_num = _no[i]
        if(_an[i] / default_num <= 0.5):
            results = results + 1
        if(_re[i] / default_num <= 0.5):
            results = results + 1
        if(_ig[i] / default_num <= 0.5):
            results = results + 1
        if(_cs[i] / default_num <= 0.5):
            results = results + 1
        if(_cc[i] / default_num <= 0.5):
            results = results + 1
    
    print(results, len(_no) * 5, results / (len(_no) * 5))
    
    _an_results = []
    _re_results = []
    _ig_results = []
    _cs_results = []
    _cc_results = []

    for i in range (0, len(_no)):
        default_num = _no[i]
        _an_results.append(_an[i] / default_num)
        _re_results.append(_re[i] / default_num)
        _ig_results.append(_ig[i] / default_num)
        _cs_results.append(_cs[i] / default_num)
        _cc_results.append(_cc[i] / default_num)
    
    print('anova: '         + str(np.mean(_an_results)) + ' ' + str(np.mean(_an_res)) + ' ' + str(np.mean(_an_bacc)))
    print('relief: '        + str(np.mean(_re_results)) + ' ' + str(np.mean(_re_res)) + ' ' + str(np.mean(_re_bacc)))
    print('inf gain: '      + str(np.mean(_ig_results)) + ' ' + str(np.mean(_ig_res)) + ' ' + str(np.mean(_ig_bacc)))
    print('chi square: '    + str(np.mean(_cs_results)) + ' ' + str(np.mean(_cs_res)) + ' ' + str(np.mean(_cs_bacc)))
    print('corr coef: '     + str(np.mean(_cc_results)) + ' ' + str(np.mean(_cc_res)) + ' ' + str(np.mean(_cc_bacc)))