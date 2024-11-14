#!/usr/bin/env python
# coding: utf-8

# In[213]:


import pandas as pd
import pingouin as pg
from scipy.stats import chisquare
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder 


# In[215]:


from sklearn import preprocessing
model = preprocessing.LabelEncoder()


# LabelEncoder for a number of columns of the abiotic dataset
class MultiColumnLabelEncoderforAbioticDataset:

     def __init__(self, columns = None):
        self.columns = columns # list of column to encode the strings of the abiotic dataset
     def fit(self, X, y=None):
        return self
     def transform(self, X):
        

        output = X.copy()

        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname, col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)

        return output
     def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)




# In[216]:


# change the strings to int
input= pd.DataFrame(pd.read_csv("Final_data_Article.csv")) 
model = MultiColumnLabelEncoderforAbioticDataset()
input=model.fit_transform(input)


# In[ ]:





# In[217]:


X=input[["Habitat", "Sector", "Water_mass", "Sediment", "Wind start",  "Wind_end"]]
y_1=input[["Habitat"]]
#df["Habitat", "Sector", "Water_mass", "Sediment", "Wind start",  "Wind_end"] = pd.to_number(df["Habitat", "Sector", "Water_mass", "Sediment", "Wind start",  "Wind_end" , errors='coerce')
y=input[["Lat_end_dec", "Long_start_dec", "Depth_CTD", "Wind_speed_start", "Wind_speed_end", "Temperature_CTD", "O2_concentration_CTD"]]


# In[220]:


from scipy.stats import chi2_contingency

def chi_square_test( col1, col2):
    
    contingency_table = pd.crosstab(col1, col2)

 
    chi2, p, dof, expected = chi2_contingency(contingency_table)

 
    significant = p < 0.05 
    return chi2, p, significant
Habitat=X.iloc[:,0]
Sector=X.iloc[:,1]
Water_mass=X.iloc[:,2]
Sediment=X.iloc[:,3]
Wind_start=X.iloc[:,4]
Wind_end=X.iloc[:,5]
#O2_concentration_CTD=X.iloc[:,7]

# create list of categorical variable 
variables = ['Habitat', 'Sector', 'Water_mass', 'Sediment', 'Wind_start',  'Wind_end']


for i in range(len(variables)):
    for j in range(i+1,len(variables)):
        # calculate Chi Square correlation coefficient,  p-value and significants
        chi2, p, significant = chi_square_test(eval(variables[i]), eval(variables[j]))
      
        print("Categorical Analysis:Chi Square correlation coefficient,  p-value and significants between", variables[i], "and", variables[j], "are",chi2, p, significant)


# In[219]:


from scipy.stats import pearsonr

from scipy.stats import pearsonr
import numpy as np
Lat_end_dec=y.iloc[:,0]
Long_start_dec=y.iloc[:,1]
Depth_CTD=y.iloc[:,2]
Wind_speed_start=y.iloc[:,3]
Wind_speed_end=y.iloc[:,4]
Temperature_CTD=y.iloc[:,5]
O2_concentration_CTD=y.iloc[:,6]

# create list of variable names
variables = ['Lat_end_dec', 'Long_start_dec', 'Depth_CTD', 'Wind_speed_start', 'Wind_speed_end', 'Temperature_CTD', 'O2_concentration_CTD']

# loop through all possible pairs of variables
for i in range(len(variables)):
    for j in range(i+1,len(variables)):
        # calculate Pearson correlation coefficient and p-value
        corr_coef, p_value = pearsonr(eval(variables[i]), eval(variables[j]))
        # print result
        print("Numerical Analysis: Pearson correlation coefficient and p-value", variables[i], "and", variables[j], "is", corr_coef, p_value)



# In[ ]:




