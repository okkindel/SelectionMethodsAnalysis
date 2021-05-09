from lib.charts.ch_best import best_feat_table, best_mean_chart, best_rank_charts, best_wilcoxon
from lib.charts.ch_percent import f1_percent_chart, percent_wilcoxon
from lib.charts.ch_wilcoxon import feats_num_wilcoxon
from lib.charts.ch_f1score import f1score_chart
from lib.charts.ch_pca import pca_distribution
from lib.charts.ch_time import time_table
import pandas as pd

df0 = pd.read_csv("../results/percent/percent_part0.csv", sep="; ", engine='python')
df1 = pd.read_csv("../results/percent/percent_part1.csv", sep="; ", engine='python')
df2 = pd.read_csv("../results/percent/percent_part2.csv", sep="; ", engine='python')
df3 = pd.read_csv("../results/percent/percent_part3.csv", sep="; ", engine='python')
df4 = pd.read_csv("../results/percent/percent_part4.csv", sep="; ", engine='python')

combine = pd.concat([df0, df1])

df = pd.read_csv("../results/time/time_all.csv", sep="; ", engine='python')

time_table(df)
