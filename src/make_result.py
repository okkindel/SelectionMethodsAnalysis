from lib.charts import makeF1Chart, makeMeanChart
import pandas as pd

df = pd.read_csv("../results/part1.csv", sep="; ", engine='python')
makeF1Chart(df)
