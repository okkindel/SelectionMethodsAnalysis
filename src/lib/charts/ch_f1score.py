from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def f1score_chart(df):
    fontP = FontProperties()
    fontP.set_size('xx-small')
    classes = []
    
    no = df[(df['method'] == 'NO SELECTION')    ]
    an = df[(df['method'] == 'ANOVA')           ]
    re = df[(df['method'] == 'RELIEF')          ]
    ig = df[(df['method'] == 'INFORATION GAIN') ]
    cs = df[(df['method'] == 'CHI SQUARE')      ]
    cc = df[(df['method'] == 'CORRELATION COEF')]

    no_f1 = np.array(no['f1_score'])
    an_f1 = np.array(an['f1_score'])
    re_f1 = np.array(re['f1_score'])
    ig_f1 = np.array(ig['f1_score'])
    cs_f1 = np.array(cs['f1_score'])
    cc_f1 = np.array(cc['f1_score'])
    
    for i in range(0, len(no_f1)):
        if (an_f1[i] < no_f1[i]): an_f1[i] = no_f1[i]
        if (re_f1[i] < no_f1[i]): re_f1[i] = no_f1[i]
        if (ig_f1[i] < no_f1[i]): ig_f1[i] = no_f1[i]
        if (cs_f1[i] < no_f1[i]): cs_f1[i] = no_f1[i]
        if (cc_f1[i] < no_f1[i]): cc_f1[i] = no_f1[i]
    
    
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
