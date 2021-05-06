from lib.charts.ch_best import best_feat_table, mean_chart, best_rank_charts
from lib.charts.ch_wilcoxon import feats_num_wilcoxon
from lib.charts.ch_percent import f1_percent_chart
from lib.charts.ch_f1score import f1score_chart
from lib.charts.ch_pca import pca_distribution
import pandas as pd


df = pd.read_csv("../results/f1_best/f1_best_all.csv", sep="; ", engine='python')
best_rank_charts(df)

# df = pd.read_csv("../results/f1_wilcoxon/wilcoxon_part1.csv", sep="; ", engine='python')
# makeWilcoxon(df)
