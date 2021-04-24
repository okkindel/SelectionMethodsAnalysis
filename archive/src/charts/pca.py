from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math


def makePCAChart(X, y, title='redukcja PCA'):
    df = pd.DataFrame(X)
    df['target'] = y
    colors = ["#0101DF", "#DF0101"]
    markers = ['o', 's']
    _, ax = plt.subplots(1, 1, figsize=(8,8))
    
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)
    
    for l, c, m in zip(np.unique(y), colors, markers):
        plt.scatter(
            X[y==l, 0],
            X[y==l, 1],
            c=c, label=l, marker=m
        )
    plt.legend(loc='upper right')
    
    ax.set_title(title, fontsize=14)
    ax.set_xlim()
    
    plt.show()