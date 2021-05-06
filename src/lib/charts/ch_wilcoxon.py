from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def feats_num_wilcoxon(df):
    fontP = FontProperties()
    fontP.set_size('xx-small')
    classes = []
    
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]
    
    no_feats = np.array(no['num_of_feat'])
    an_feats = np.array(an['num_of_feat'])
    re_feats = np.array(re['num_of_feat'])
    ig_feats = np.array(ig['num_of_feat'])
    cs_feats = np.array(cs['num_of_feat'])
    cc_feats = np.array(cc['num_of_feat'])
    
    for i in range(0, len(no_feats)):
        full = no_feats[i]
        an_feats[i] = (an_feats[i] / full) * 100
        re_feats[i] = (re_feats[i] / full) * 100
        ig_feats[i] = (ig_feats[i] / full) * 100
        cs_feats[i] = (cs_feats[i] / full) * 100
        cc_feats[i] = (cc_feats[i] / full) * 100
        no_feats[i] = 100

    feature = np.arange(len(no))
    for set in no['dataset']:
        classes.append(str(set))

    plt.plot(feature, an_feats, linestyle='-', marker='o', color=(0.1, 0.2, 0.3, 0.8), label="ANOVA")
    plt.plot(feature, re_feats, linestyle='-', marker='o', color=(0.8, 0.8, 0.1, 0.8), label="RELIEF")
    plt.plot(feature, ig_feats, linestyle='-', marker='o', color=(0.1, 0.7, 0.1, 0.8), label="INFORATION GAIN")
    plt.plot(feature, cs_feats, linestyle='-', marker='o', color=(0.2, 0.2, 0.2, 0.8), label="CHI SQUARE")
    plt.plot(feature, cc_feats, linestyle='-', marker='o', color=(0.5, 0.1, 0.5, 0.8), label="CORRELATION COEF")
    plt.plot(feature, no_feats, linestyle='-', marker='o', color=(1, 0, 0, 1), label="NO SELECTION")

    plt.ylabel('Procent cech')
    plt.xlabel('Zbiór')
    plt.xticks(feature, classes)
    plt.xticks(rotation=90)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', prop=fontP)
    plt.show()
