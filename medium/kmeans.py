import os
import pandas as pd
import numpy as np
from  sklearn.cluster import KMeans

if __name__ == '__main__':

    X = pd.DataFrame({  'x1': [2,1,2,4,6,6], 'x2': [6,6,4,4,4,3]}, index=list('abcdef'))
    est = KMeans(n_clusters=2, init=X.iloc[3:5])
    est.fit(X)
    print(est.labels_)
