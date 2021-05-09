from matplotlib.font_manager import FontProperties
from scipy.stats import wilcoxon
import matplotlib.pyplot as plt
import numpy as np
import itertools

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def f1_percent_chart(df):
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

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def percent_wilcoxon(df):
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
    
    f1_no = (list(itertools.chain(*(no[['f1_score']].values))))
    f1_an_20 = (list(itertools.chain(*(an_20[['f1_score']].values))))
    f1_re_20 = (list(itertools.chain(*(re_20[['f1_score']].values))))
    f1_ig_20 = (list(itertools.chain(*(ig_20[['f1_score']].values))))
    f1_cs_20 = (list(itertools.chain(*(cs_20[['f1_score']].values))))
    f1_cc_20 = (list(itertools.chain(*(cc_20[['f1_score']].values))))
    f1_an_40 = (list(itertools.chain(*(an_40[['f1_score']].values))))
    f1_re_40 = (list(itertools.chain(*(re_40[['f1_score']].values))))
    f1_ig_40 = (list(itertools.chain(*(ig_40[['f1_score']].values))))
    f1_cs_40 = (list(itertools.chain(*(cs_40[['f1_score']].values))))
    f1_cc_40 = (list(itertools.chain(*(cc_40[['f1_score']].values))))
    f1_an_60 = (list(itertools.chain(*(an_60[['f1_score']].values))))
    f1_re_60 = (list(itertools.chain(*(re_60[['f1_score']].values))))
    f1_ig_60 = (list(itertools.chain(*(ig_60[['f1_score']].values))))
    f1_cs_60 = (list(itertools.chain(*(cs_60[['f1_score']].values))))
    f1_cc_60 = (list(itertools.chain(*(cc_60[['f1_score']].values))))
    f1_an_80 = (list(itertools.chain(*(an_80[['f1_score']].values))))
    f1_re_80 = (list(itertools.chain(*(re_80[['f1_score']].values))))
    f1_ig_80 = (list(itertools.chain(*(ig_80[['f1_score']].values))))
    f1_cs_80 = (list(itertools.chain(*(cs_80[['f1_score']].values))))
    f1_cc_80 = (list(itertools.chain(*(cc_80[['f1_score']].values))))
    
    _methods = ['ANOVA 20%', 'RELIEF 20%', 'INFORATION GAIN 20%', 'CHI SQUARE 20%', 'CORRELATION COEF 20%',
                'ANOVA 40%', 'RELIEF 40%', 'INFORATION GAIN 40%', 'CHI SQUARE 40%', 'CORRELATION COEF 40%',
                'ANOVA 60%', 'RELIEF 60%', 'INFORATION GAIN 60%', 'CHI SQUARE 60%', 'CORRELATION COEF 60%',
                'ANOVA 80%', 'RELIEF 80%', 'INFORATION GAIN 80%', 'CHI SQUARE 80%', 'CORRELATION COEF 80%',
                'ANOVA 100%', 'RELIEF 100%', 'INFORATION GAIN 100%', 'CHI SQUARE 100%', 'CORRELATION COEF 100%']

    _list = [f1_an_20, f1_re_20, f1_ig_20, f1_cs_20, f1_cc_20,
             f1_an_40, f1_re_40, f1_ig_40, f1_cs_40, f1_cc_40,
             f1_an_60, f1_re_60, f1_ig_60, f1_cs_60, f1_cc_60,
             f1_an_80, f1_re_80, f1_ig_80, f1_cs_80, f1_cc_80,
             f1_no, f1_no, f1_no, f1_no, f1_no]
    res = []
    
    for i in range(0, len(_list)):
        res.append([])
        for j in range (0, len(_list)):
            if (i != j):
                try: _, p = wilcoxon(_list[i], _list[j])
                except ValueError: p = 1
                print(p)
                res[i].append(p)
            else:
                res[i].append(-1)
                
    fi_matrix = np.array(res)
    
    fig, ax = plt.subplots()
    im = ax.imshow(fi_matrix)
    
    ax.set_xticks(np.arange(len(_methods)))
    ax.set_yticks(np.arange(len(_methods)))
    ax.set_xticklabels(_methods)
    ax.set_yticklabels(_methods)
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    for i in range(len(_methods)):
        for j in range(len(_methods)):
            text = ax.text(j, i, '' if fi_matrix[i, j] == -1 else "{:.2f}".format(round(fi_matrix[i, j], 2)), ha="center", va="center", color="black")
    
    fig.tight_layout()
    plt.show()
