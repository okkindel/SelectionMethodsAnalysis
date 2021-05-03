from lib.charts import makeF1Chart, makeMeanChart
import pandas as pd


df = pd.read_csv("../results/f1_best/f1_best_all.csv", sep="; ", engine='python')
makeF1Chart(df)
