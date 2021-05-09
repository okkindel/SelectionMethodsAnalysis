from matplotlib.font_manager import FontProperties
from scipy.stats import wilcoxon
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
import itertools

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

def time_table(df):
    no = df[(df['method'] == 'NO SELECTION')]
    an = df[(df['method'] == 'ANOVA')]
    re = df[(df['method'] == 'RELIEF')]
    ig = df[(df['method'] == 'INFORATION GAIN')]
    cs = df[(df['method'] == 'CHI SQUARE')]
    cc = df[(df['method'] == 'CORRELATION COEF')]

    _an = (list(itertools.chain(*(an[['time']].values))))
    _re = (list(itertools.chain(*(re[['time']].values))))
    _ig = (list(itertools.chain(*(ig[['time']].values))))
    _cs = (list(itertools.chain(*(cs[['time']].values))))
    _cc = (list(itertools.chain(*(cc[['time']].values))))
    
    _an_elems = (list(itertools.chain(*(an[['num_of_elems']].values))))
    _re_elems = (list(itertools.chain(*(re[['num_of_elems']].values))))
    _ig_elems = (list(itertools.chain(*(ig[['num_of_elems']].values))))
    _cs_elems = (list(itertools.chain(*(cs[['num_of_elems']].values))))
    _cc_elems = (list(itertools.chain(*(cc[['num_of_elems']].values))))

    _an_feats = (list(itertools.chain(*(an[['num_of_feat']].values))))
    _re_feats = (list(itertools.chain(*(re[['num_of_feat']].values))))
    _ig_feats = (list(itertools.chain(*(ig[['num_of_feat']].values))))
    _cs_feats = (list(itertools.chain(*(cs[['num_of_feat']].values))))
    _cc_feats = (list(itertools.chain(*(cc[['num_of_feat']].values))))
    
    _an_time_for_elem = [i / j / k for i, j, k in zip(_an, _an_elems, _an_feats)]
    _re_time_for_elem = [i / j / k for i, j, k in zip(_re, _re_elems, _re_feats)]
    _ig_time_for_elem = [i / j / k for i, j, k in zip(_ig, _ig_elems, _ig_feats)]
    _cs_time_for_elem = [i / j / k for i, j, k in zip(_cs, _cs_elems, _cs_feats)]
    _cc_time_for_elem = [i / j / k for i, j, k in zip(_cc, _cc_elems, _cc_feats)]
    
    print('anova: '         + str(np.mean(_an)) + ' ' + str('{:f}'.format(np.mean(_an_time_for_elem))))
    print('relief: '        + str(np.mean(_re)) + ' ' + str('{:f}'.format(np.mean(_re_time_for_elem))))
    print('inf gain: '      + str(np.mean(_ig)) + ' ' + str('{:f}'.format(np.mean(_ig_time_for_elem))))
    print('chi square: '    + str(np.mean(_cs)) + ' ' + str('{:f}'.format(np.mean(_cs_time_for_elem))))
    print('corr coef: '     + str(np.mean(_cc)) + ' ' + str('{:f}'.format(np.mean(_cc_time_for_elem))))
