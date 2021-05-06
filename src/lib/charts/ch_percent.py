from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

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
