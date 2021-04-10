import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('../data/creditcard.csv')
colors = ["#0101DF", "#DF0101"]

sns.countplot('Class', data=df, palette=colors)
plt.title('Dystrybucja klas CCFD \n 0: No Fraud, 1: Fraud', fontsize=14)
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(18,4))

amount_val = df['Amount'].values
time_val = df['Time'].values

sns.distplot(amount_val, ax=ax[0], color='b')
ax[0].set_title('Dystrybucja cechy Amount', fontsize=14)
ax[0].set_xlim([min(amount_val), max(amount_val)])

sns.distplot(time_val, ax=ax[1], color='r')
ax[1].set_title('Dystrybucja cechy Time', fontsize=14)
ax[1].set_xlim([min(time_val), max(time_val)])

# plt.show()
