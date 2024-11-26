#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
input= pd.DataFrame(pd.read_csv("Dataset_Tree.csv")) 
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import pandas as pd
import pingouin as pg
x =input['Lat_end_DD']
y= input['Long_start_DD']

# Plot
plt.scatter(x,y, color='red')
#plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})

# Decorate
plt.title('Scatter plot of Lat_end against Long_start')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




