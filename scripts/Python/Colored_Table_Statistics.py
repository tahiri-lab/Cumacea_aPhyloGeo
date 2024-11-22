#!/usr/bin/env python
# coding: utf-8

# In[8]:


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
import pandas as pd
pd.DataFrame.iteritems = pd.DataFrame.items


# In[9]:


#import functools
input= pd.DataFrame(pd.read_csv("Dataset_Table.csv")) 
modified_table=input.describe().loc[['mean', 'std', '25%', '50%', '75%',  'min','max']]
New_table=modified_table.T
Final_table=New_table.applymap(lambda x: f"{x:0.2f}")
Final_table


# In[ ]:





# In[10]:


def background_gradient_for_abiotic_dataset(s, m, M, cmap='PuBu', low=0, high=0):
    rank_rng = M - m
    norm = colors.Normalize(m - (rank_rng  * low),
                            M + (rank_rng  * high))
    normed = norm(s.values)
    c = [colors.rgb2hex(x) for x in plt.cm.get_cmap(cmap)(normed)]
    return ['background-color: %s' % color for color in c]

New_table.style.apply(background_gradient_for_abiotic_dataset,
               cmap='PuBu',
               m=New_table.min().min(),
               M=New_table.max().max(),
               low=0,
               high=0.2)


# In[ ]:




