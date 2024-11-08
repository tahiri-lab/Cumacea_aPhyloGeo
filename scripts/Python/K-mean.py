#!/usr/bin/env python
# coding: utf-8

# In[34]:


from sklearn.cluster import KMeans
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
from sklearn import linear_model, preprocessing, model_selection, pipeline, ensemble, tree, datasets, cluster


# In[4]:


df = pd.read_excel ("data_missing_values.xlsx") 
df.to_csv ("data_missing_values.csv",  
                  index = None, 
                  header=True) 
input= pd.DataFrame(pd.read_csv("data_missing_values.csv"))


# In[152]:


def kmeans_missing_oxygen_concentration(X, n_clusters, max_iter):
    mis = ~np.isfinite(X)
    mu = np.nanmean(X, 0, keepdims=1)
    X_hat = np.where(mis, mu, X)
    for i in range(max_iter):
        if i > 0:
            cls = KMeans(n_clusters, init=prev_centroids)
        else:
           
            cls = KMeans(n_clusters)

     
        labels = cls.fit_predict(X_hat)
        centroids = cls.cluster_centers_

     
        X_hat[mis] = centroids[labels][mis]

    
        if i > 0 and np.all(labels == prev_labels):
            break

        prev_labels = labels
        prev_centroids = cls.cluster_centers_

    return  labels,  X_hat


# In[155]:


def Kmean_impute(input, n_clusters):
    labels, df_filled = kmeans_missing_oxygen_concentration(input, n_clusters, max_iter=100) 
    matrix = pd.DataFrame(df_filled, columns=["Habitat","Sector","Water_mass","Sediment","Lat end dec","Long_start_dec","Depth_start","Wind_end","Wind_speed_start","Wind_speed_end","Watertemp_ground","O2-saturation_ground"])
    matrix.to_csv("DataK-Mean" +  str(n_clusters) + ".csv" )
    return  matrix, labels


# In[ ]:





# In[156]:


for n_clusters in range(1,10,1):
    matrix, labels =Kmean_impute(input, n_clusters)
    X = matrix.drop('O2-saturation_ground',axis=1)
    y =  matrix['O2-saturation_ground']
    km = pipeline.make_pipeline(preprocessing.StandardScaler(), cluster.KMeans(n_clusters = n_clusters),
                           linear_model.LinearRegression()) # we used linear regression to test the inputed value
    km.fit(X, y)
    cv_scores = cross_val_score(km, X,  y,  cv=10, scoring='neg_mean_squared_error')
    print(tf.math.abs(cv_scores.mean()))


# In[ ]:





# In[ ]:




