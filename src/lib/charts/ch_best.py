from matplotlib.font_manager import FontProperties
from scikit_posthocs import posthoc_wilcoxon
from scipy.stats import wilcoxon, stats
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
import itertools

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def best_feat_table(df):
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
    
    # count num of results with num of features less than
    print(results, len(_no) * 5, results / (len(_no) * 5))
    
    _an_results = []
    _re_results = []
    _ig_results = []
    _cs_results = []
    _cc_results = []

    # mean feats num
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

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def best_mean_chart(df):
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

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def best_rank_charts(df):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(5, 3))
    
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]
    
    f1_no = (list(itertools.chain(*(no[['f1_score']].values))))
    f1_an = (list(itertools.chain(*(an[['f1_score']].values))))
    f1_re = (list(itertools.chain(*(re[['f1_score']].values))))
    f1_ig = (list(itertools.chain(*(ig[['f1_score']].values))))
    f1_cs = (list(itertools.chain(*(cs[['f1_score']].values))))
    f1_cc = (list(itertools.chain(*(cc[['f1_score']].values))))
    
    f1_no_res = []
    f1_an_res = []
    f1_re_res = []
    f1_ig_res = []
    f1_cs_res = []
    f1_cc_res = []
    
    for i in range (0, len(no)):
        f1_no_i = ('no', f1_no[i])
        f1_an_i = ('an', f1_an[i])
        f1_re_i = ('re', f1_re[i])
        f1_ig_i = ('ig', f1_ig[i])
        f1_cs_i = ('cs', f1_cs[i])
        f1_cc_i = ('cc', f1_cc[i])
        
        _list = [f1_no_i, f1_an_i, f1_re_i, f1_ig_i, f1_cs_i, f1_cc_i]
        l_sorted = sorted(_list, key=itemgetter(1))
        
        temp_no = [y[0] for y in l_sorted].index('no')
        temp_an = [y[0] for y in l_sorted].index('an')
        temp_re = [y[0] for y in l_sorted].index('re')
        temp_ig = [y[0] for y in l_sorted].index('ig')
        temp_cs = [y[0] for y in l_sorted].index('cs')
        temp_cc = [y[0] for y in l_sorted].index('cc')

        for j in range(0, (len(l_sorted) - 1)):
            if (l_sorted[j][1] == l_sorted[j+1][1]):
                temp_no = max(temp_no - 1, 0)
                temp_an = max(temp_an - 1, 0)
                temp_re = max(temp_re - 1, 0)
                temp_ig = max(temp_ig - 1, 0)
                temp_cs = max(temp_cs - 1, 0)
                temp_cc = max(temp_cc - 1, 0)
                
        f1_no_res.append(temp_no)
        f1_an_res.append(temp_an)
        f1_re_res.append(temp_re)
        f1_ig_res.append(temp_ig)
        f1_cs_res.append(temp_cs)
        f1_cc_res.append(temp_cc)
    
    axes[0].grid()
    axes[0].bar(height=np.mean(f1_no_res), edgecolor='black', color='red', x="NO SELECTION")
    axes[0].bar(height=np.mean(f1_an_res), edgecolor='black', color='lightblue', x="ANOVA")
    axes[0].bar(height=np.mean(f1_re_res), edgecolor='black', color='aqua', x="RELIEF")
    axes[0].bar(height=np.mean(f1_ig_res), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[0].bar(height=np.mean(f1_cs_res), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[0].bar(height=np.mean(f1_cc_res), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[0].set_title('Średnia ranga według F1 Score')
    axes[0].tick_params(labelrotation=40)
    axes[0].set_ylim([0, 2])
    
    feats_no = (list(itertools.chain(*(no[['num_of_feat']].values))))
    feats_an = (list(itertools.chain(*(an[['num_of_feat']].values))))
    feats_re = (list(itertools.chain(*(re[['num_of_feat']].values))))
    feats_ig = (list(itertools.chain(*(ig[['num_of_feat']].values))))
    feats_cs = (list(itertools.chain(*(cs[['num_of_feat']].values))))
    feats_cc = (list(itertools.chain(*(cc[['num_of_feat']].values))))
    
    feats_no_res = []
    feats_an_res = []
    feats_re_res = []
    feats_ig_res = []
    feats_cs_res = []
    feats_cc_res = []
    
    for i in range (0, len(no)):
        feats_no_i = ('no', feats_no[i])
        feats_an_i = ('an', feats_an[i])
        feats_re_i = ('re', feats_re[i])
        feats_ig_i = ('ig', feats_ig[i])
        feats_cs_i = ('cs', feats_cs[i])
        feats_cc_i = ('cc', feats_cc[i])
        
        _list = [feats_no_i, feats_an_i, feats_re_i, feats_ig_i, feats_cs_i, feats_cc_i]
        l_sorted = sorted(_list, key=itemgetter(1))
        
        temp_no = 5 - [y[0] for y in l_sorted].index('no')
        temp_an = 5 - [y[0] for y in l_sorted].index('an')
        temp_re = 5 - [y[0] for y in l_sorted].index('re')
        temp_ig = 5 - [y[0] for y in l_sorted].index('ig')
        temp_cs = 5 - [y[0] for y in l_sorted].index('cs')
        temp_cc = 5 - [y[0] for y in l_sorted].index('cc')

        for j in range(0, (len(l_sorted) - 1)):
            if (l_sorted[j][1] == l_sorted[j+1][1]):
                temp_no = max(temp_no - 1, 0)
                temp_an = max(temp_an - 1, 0)
                temp_re = max(temp_re - 1, 0)
                temp_ig = max(temp_ig - 1, 0)
                temp_cs = max(temp_cs - 1, 0)
                temp_cc = max(temp_cc - 1, 0)
        
        feats_no_res.append(temp_no)
        feats_an_res.append(temp_an)
        feats_re_res.append(temp_re)
        feats_ig_res.append(temp_ig)
        feats_cs_res.append(temp_cs)
        feats_cc_res.append(temp_cc)
    
    axes[1].grid()
    axes[1].bar(height=np.mean(feats_no_res), edgecolor='black', color='red', x="NO SELECTION")
    axes[1].bar(height=np.mean(feats_an_res), edgecolor='black', color='lightblue', x="ANOVA")
    axes[1].bar(height=np.mean(feats_re_res), edgecolor='black', color='aqua', x="RELIEF")
    axes[1].bar(height=np.mean(feats_ig_res), edgecolor='black', color='grey', x="INFORATION GAIN")
    axes[1].bar(height=np.mean(feats_cs_res), edgecolor='black', color='teal', x="CHI SQUARE")
    axes[1].bar(height=np.mean(feats_cc_res), edgecolor='black', color='aquamarine', x="CORRELATION COEF")
    axes[1].set_title('Średnia ranga według ilości cech')
    axes[1].tick_params(labelrotation=40)
    axes[1].set_ylim([0, 2])
    
    f1_res = [np.mean(f1_no_res), np.mean(f1_an_res), np.mean(f1_re_res), np.mean(f1_ig_res), np.mean(f1_cs_res), np.mean(f1_cc_res)]
    feats_res = [np.mean(feats_no_res), np.mean(feats_an_res), np.mean(feats_re_res), np.mean(feats_ig_res), np.mean(feats_cs_res), np.mean(feats_cc_res)]
    _methods = ['NO SELECTION', 'ANOVA', 'RELIEF', 'INFORATION GAIN', 'CHI SQUARE', 'CORRELATION COEF']
    _markers = ['o', 'v', '^', '>', 's', 'd']
    _colors = ['red', 'lightblue', 'aqua', 'grey', 'teal', 'aquamarine']

    axes[2].grid()
    for i in range(0, len(_methods)):
        axes[2].plot(f1_res[i], feats_res[i], _markers[i], label=_methods[i], color=_colors[i])
    axes[2].legend(numpoints=1)
    axes[2].set_title('Stosunek rangi F1 Score do rangi liczby cech')
    axes[2].set_xlabel('Ranga F1 Score')
    axes[2].set_ylabel('Ranga liczby cech')
    
    plt.show()

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def best_wilcoxon(df):
    fontP = FontProperties()
    fontP.set_size('xx-small')
    
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]
    
    f1_no = (list(itertools.chain(*(no[['f1_score']].values))))
    f1_an = (list(itertools.chain(*(an[['f1_score']].values))))
    f1_re = (list(itertools.chain(*(re[['f1_score']].values))))
    f1_ig = (list(itertools.chain(*(ig[['f1_score']].values))))
    f1_cs = (list(itertools.chain(*(cs[['f1_score']].values))))
    f1_cc = (list(itertools.chain(*(cc[['f1_score']].values))))
    
    _methods = ['NO SELECTION', 'ANOVA', 'RELIEF', 'INFORATION GAIN', 'CHI SQUARE', 'CORRELATION COEF']
    _list = [f1_no, f1_an, f1_re, f1_ig, f1_cs, f1_cc]
    res = posthoc_wilcoxon(_list, zero_method='wilcox', p_adjust='hommel')
    
    
    for i in range (1, len(_list) + 1):
        res.at[i, i] = -1
    
    # for i in range(0, len(_list)):
    #     res.append([])
    #     for j in range (0, len(_list)):
    #         if (i != j):
    #             _, p = wilcoxon(_list[i], _list[j])
    #             print(p)
    #             res[i].append(p)
    #         else:
    #             res[i].append(-1)
                
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

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def best_percent_table(df):
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
    
    _an_feats = [i / j for i, j in zip(_an , _no)]
    _re_feats = [i / j for i, j in zip(_re , _no)]
    _ig_feats = [i / j for i, j in zip(_ig , _no)]
    _cs_feats = [i / j for i, j in zip(_cs , _no)]
    _cc_feats = [i / j for i, j in zip(_cc , _no)]
    
    _an_f1 = (list(itertools.chain(*(an[['f1_score']].values))))
    _re_f1 = (list(itertools.chain(*(re[['f1_score']].values))))
    _ig_f1 = (list(itertools.chain(*(ig[['f1_score']].values))))
    _cs_f1 = (list(itertools.chain(*(cs[['f1_score']].values))))
    _cc_f1 = (list(itertools.chain(*(cc[['f1_score']].values))))

    _an_iqr = stats.iqr(_an_f1, interpolation = 'midpoint')
    _re_iqr = stats.iqr(_re_f1, interpolation = 'midpoint')
    _ig_iqr = stats.iqr(_ig_f1, interpolation = 'midpoint')
    _cs_iqr = stats.iqr(_cs_f1, interpolation = 'midpoint')
    _cc_iqr = stats.iqr(_cc_f1, interpolation = 'midpoint')
    
    print('anova: '         + str(np.mean(_an_feats)) + ' ' + str(np.mean(_an_f1)) + ' ' + str(_an_iqr))
    print('relief: '        + str(np.mean(_re_feats)) + ' ' + str(np.mean(_re_f1)) + ' ' + str(_re_iqr))
    print('inf gain: '      + str(np.mean(_ig_feats)) + ' ' + str(np.mean(_ig_f1)) + ' ' + str(_ig_iqr))
    print('chi square: '    + str(np.mean(_cs_feats)) + ' ' + str(np.mean(_cs_f1)) + ' ' + str(_cs_iqr))
    print('corr coef: '     + str(np.mean(_cc_feats)) + ' ' + str(np.mean(_cc_f1)) + ' ' + str(_cc_iqr))
