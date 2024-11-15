#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.impute import KNNImputer
import tensorflow as tf 


# In[ ]:


df = pd.read_excel ("data_missing_values.xlsx") 
df.to_csv ("data_missing_values.csv",  
                  index = None, 
                  header=True) 
df= pd.DataFrame(pd.read_csv("data_missing_values.csv"))  


# In[ ]:





# In[ ]:


def KNN_impute(input_data, k):

    
    imputer = KNNImputer(n_neighbors=k)
    df_filled = imputer.fit_transform(input_data)

    matrix = pd.DataFrame(df_filled, columns=["Habitat","Sector","Water_mass","Sediment","Lat_end_dec","Long_start_dec","Depth_CTD","Wind_end","Wind_speed_start","Wind_speed_end","Temperature_CTD","O2_saturation_CTD"])
    
    matrix.to_csv("DataKNN_imputed" + str(k) + ".csv")
    
    return matrix


# In[ ]:


for k in range(1, 11,1):  

    matrix = KNN_impute(df, k)
    

    aws = KNeighborsRegressor(n_neighbors=k)
    

    X = matrix.drop(columns=['O2_saturation_CTD']) 
    y = matrix['O2_saturation_CTD']  
    
    
    aws.fit(X, y)
    
    
    cv_scores = cross_val_score(aws, X, y, cv=10, scoring='neg_mean_squared_error')
    
    
    print(f"Mean Squared Error for k={k}: {tf.math.abs(cv_scores.mean()).numpy()}")


# In[ ]:




