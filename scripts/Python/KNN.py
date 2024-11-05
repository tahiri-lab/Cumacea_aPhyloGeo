#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import xlrd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.impute import KNNImputer
#import rows


# In[ ]:





# In[68]:


df = pd.read_excel ("data_missing_values.xlsx") 
df.to_csv ("data_missing_values.csv",  
                  index = None, 
                  header=True) 
input= pd.DataFrame(pd.read_csv("data_missing_values.csv")) 
#input=pd.read_excel('data_missing_values.csv')


# In[69]:


def KNN_impute(input, k):
    imputer = KNNImputer(n_neighbors=k)
    df_filled = imputer.fit_transform(input)
    matrix = pd.DataFrame(df_filled, columns=["Habitat","Sector","Water_mass","Sediment","Lat end dec","Long_start_dec","Depth_start","Wind_end","Wind_speed_start","Wind_speed_end","Watertemp_ground","O2-saturation_ground"])
    matrix.to_csv("DataKNN" +  str(k) + ".csv" )
    return matrix


# In[73]:


for k in range(1,11,1):
    matrix=KNN_impute(input, k)
    aws=KNeighborsRegressor(k)
    X = matrix.drop('O2-saturation_ground',axis=1)
    y =  matrix['O2-saturation_ground']
    aws.fit(X, y)
    cv_scores = cross_val_score(aws, X, y,  cv=10, scoring='neg_mean_squared_error')
    print(tf.math.abs(cv_scores.mean()))


# # 

# In[ ]:




