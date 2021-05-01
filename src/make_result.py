from lib.charts import makeF1Chart, makeMeanChart
import pandas as pd
import numpy as np
import itertools

df = pd.read_csv("../results/f1_best/f1_best_all.csv", sep="; ", engine='python')
makeMeanChart(df)

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

# results = 0

# for i in range (0, len(_no)):
#     default_num = _no[i]
#     if(_an[i] / default_num <= 0.5):
#         results = results + 1
#     if(_re[i] / default_num <= 0.5):
#         results = results + 1
#     if(_ig[i] / default_num <= 0.5):
#         results = results + 1
#     if(_cs[i] / default_num <= 0.5):
#         results = results + 1
#     if(_cc[i] / default_num <= 0.5):
#         results = results + 1

# print(results, len(_no) * 5, results / (len(_no) * 5))

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