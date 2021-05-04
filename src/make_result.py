from lib.charts import makeWilcoxon, makeF1Chart
import pandas as pd


df = pd.read_csv("../results/f1_best/f1_best_all.csv", sep="; ", engine='python')
makeF1Chart(df)

# df = pd.read_csv("../results/f1_wilcoxon/wilcoxon_part1.csv", sep="; ", engine='python')
# makeWilcoxon(df)
