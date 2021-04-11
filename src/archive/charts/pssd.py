import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('../data/porto-seguro-safe-driver.csv')
colors = ["#0101DF", "#DF0101"]

sns.countplot('target', data=df, palette=colors)
plt.title('Dystrybucja klas zbioru PSSD \n 0: Właściciel nie złożył roszczenia, 1: Właściciel złożył roszczenie', fontsize=14)
plt.show()
