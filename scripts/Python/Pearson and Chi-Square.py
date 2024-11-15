#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pingouin as pg
from scipy.stats import chisquare
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder 


# In[2]:


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




# In[3]:


# change the strings to ints]
input= pd.DataFrame(pd.read_csv("Final_data_Article.csv")) 
model = MultiColumnLabelEncoderforAbioticDataset()
input=model.transform_abiotic(input)


# In[ ]:





# In[4]:


X_categorical=input[["Habitat", "Sector", "Water_mass", "Sediment", "Wind start",  "Wind_end"]]

#df["Habitat", "Sector", "Water_mass", "Sediment", "Wind start",  "Wind_end"] = pd.to_number(df["Habitat", "Sector", "Water_mass", "Sediment", "Wind start",  "Wind_end" , errors='coerce')
y_numerical=input[["Lat_end_dec", "Long_start_dec", "Depth_CTD", "Wind_speed_start", "Wind_speed_end", "Temperature_CTD", "O2_concentration_CTD"]]


# In[5]:


from scipy.stats import chi2_contingency

def perform_chi_square_test( col1, col2):
    
    contingency_table = pd.crosstab(col1, col2)

    # Perform the Chi-Square Test
    chisquare, p, dof, expected = chi2_contingency(contingency_table)

  
    significant = p < 0.05  
    return chisquare, p, significant
Habitat=X_categorical.iloc[:,0]
Sector=X_categorical.iloc[:,1]
Water_mass=X_categorical.iloc[:,2]
Sediment=X_categorical.iloc[:,3]
Wind_start=X_categorical.iloc[:,4]
Wind_end=X_categorical.iloc[:,5]
#O2_concentration_CTD=X.iloc[:,7]

# create list of different categories
features = ['Habitat', 'Sector', 'Water_mass', 'Sediment', 'Wind_start',  'Wind_end']

# run through the pairs of features
for n in range(len(features)):
    for m in range(n+1,len(features)):
        # calculate Chi Square correlation coefficient,  p-value and significants
        chisquare, p, significant = perform_chi_square_test(eval(features[n]), eval(features[m]))
        # show the result
        print("Categorical Analysis:Chi Square correlation coefficient,  p-value and significants between", features[n], "and", features[m], "are",chisquare, p, significant)


# In[6]:


from scipy.stats import pearsonr

from scipy.stats import pearsonr
import numpy as np
Lat_end_dec=y_numerical.iloc[:,0]
Long_start_dec=y_numerical.iloc[:,1]
Depth_CTD=y_numerical.iloc[:,2]
Wind_speed_start=y_numerical.iloc[:,3]
Wind_speed_end=y_numerical.iloc[:,4]
Temperature_CTD=y_numerical.iloc[:,5]
O2_concentration_CTD=y_numerical.iloc[:,6]

# create list of variable names
features = ['Lat_end_dec', 'Long_start_dec', 'Depth_CTD', 'Wind_speed_start', 'Wind_speed_end', 'Temperature_CTD', 'O2_concentration_CTD']

# loop through all possible pairs of variables
for n in range(len(features)):
    for m in range(n+1,len(features)):
        # calculate Pearson correlation coefficient and p-value
        corr_coef, p_value = pearsonr(eval(features[n]), eval(features[m]))
        # print result
        print("Numerical Analysis: Pearson correlation coefficient and p-value", features[n], "and", features[m], "is", corr_coef, p_value)



# In[ ]:




