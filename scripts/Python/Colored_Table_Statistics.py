#!/usr/bin/env python
# coding: utf-8

# In[213]:


from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import pandas as pd
import pingouin as pg
from scipy.stats import chisquare
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder 
import numpy as np
import matplotlib.pyplot as plt
import six
import statistics
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from statistics import stdev


# In[214]:


from sklearn import preprocessing
model = preprocessing.LabelEncoder()

#a slight modification of the multiColumn Label Encoder in 
#https://stackoverflow.com/questions/24458645/label-encoding-across-multiple-columns-in-scikit-learn


class MultiColumnLabelEncoderforAbioticDataset:

     def __init__(self, columns_abiotic = None):
        self.columns_abiotic = columns_abiotic # columns of the abiotic dataset
     def fit(self, X_categorical, y_numerical=None):
        return self
     def transform_abiotic(self, X_categorical):
        

        output = X_categorical.copy()

        if self.columns_abiotic is not None:
            for col_abiotic in self.columns:
                output[col_abiotic] = LabelEncoder().fit_transform(output[col_abiotic])
        else:
            for colname, col_abiotic in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col_abiotic)

        return output
     def fit_transform(self, X_categorical, y_numerical=None):
        return self.fit(X_categorical, y_numerical).transform(X_categorical)


# In[215]:


#import functools
input= pd.DataFrame(pd.read_csv("Final_data_Article.csv")) 
model = MultiColumnLabelEncoderforAbioticDataset()
input=model.transform_abiotic(input)
#input.drop(columns=['field']) 
#percentiles=tuple(functools.partial(np.percentile, q=q) for q in (75, 85,95 ))
#stat_function=(np.mean(input), np.std(input), np.median(input), np.var(input)) + percentiles
modified_table=input.describe()
New_table=modified_table.T


# In[216]:


def background_gradient_for_abiotic_dataset(s, m, M, cmap='PuBu', low=0, high=0):
    rank_rng = M - m
    norm = colors.Normalize(m - (rank_rng  * low),
                            M + (rank_rng  * high))
    normed = norm(s.values)
    c = [colors.rgb2hex(x) for x in plt.cm.get_cmap(cmap)(normed)]
    return ['background-color: %s' % color for color in c]

New_table.style.apply(background_gradient,
               cmap='PuBu',
               m=New_table.min().min(),
               M=New_table.max().max(),
               low=0,
               high=0.2)


# In[ ]:





# In[ ]:





# In[ ]:




