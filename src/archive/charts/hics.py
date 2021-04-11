from lib.data_preprocessing import getInsuranceData
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

[X, y] = getInsuranceData()

df = pd.DataFrame(X)
df['target'] = y


# colors = ["#0101DF", "#DF0101"]
# sns.countplot('target', data=df, palette=colors)
# plt.title('Dystrybucja klas zbioru HICS', fontsize=14)
# # plt.show()

def plot_2d_space(X, y, label='Classes'):   
    colors = ["#0101DF", "#DF0101"]
    markers = ['o', 's']
    for l, c, m in zip(np.unique(y), colors, markers):
        plt.scatter(
            X[y==l, 0],
            X[y==l, 1],
            c=c, label=l, marker=m
        )
    plt.title(label)
    plt.legend(loc='upper right')
    plt.show()

pca = PCA(n_components=2)
X = pca.fit_transform(X)

plot_2d_space(X, y, 'Dystrybucja danych zbioru HICS (redukcja PCA)')
