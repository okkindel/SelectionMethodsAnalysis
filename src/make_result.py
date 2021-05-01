from lib.charts import makeF1Chart, makeMeanChart
import pandas as pd


df = pd.read_csv("../results/percent/percent_part0.csv", sep="; ", engine='python')
makeF1Chart(df)
