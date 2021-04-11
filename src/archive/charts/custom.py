from lib.data_preprocessing import getCustomData, getInsuranceData, getCreditCardData, getSafeDriverData
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

[X, y] = getInsuranceData()

df = pd.DataFrame(X)
df['target'] = y
colors = ["#0101DF", "#DF0101"]
markers = ['o', 's']
fig, ax = plt.subplots(1, 2, figsize=(18,4))

sns.countplot('target', data=df, ax=ax[0], palette=colors)
ax[0].set_title('Dystrybucja klas zbioru HICS', fontsize=14)
ax[0].set_xlim()

pca = PCA(n_components=2)
X = pca.fit_transform(X)

for l, c, m in zip(np.unique(y), colors, markers):
    plt.scatter(
        X[y==l, 0],
        X[y==l, 1],
        c=c, label=l, marker=m
    )
plt.legend(loc='upper right')

ax[1].set_title('Dystrybucja danych zbioru HICS (redukcja PCA)', fontsize=14)
ax[1].set_xlim()

plt.show()
