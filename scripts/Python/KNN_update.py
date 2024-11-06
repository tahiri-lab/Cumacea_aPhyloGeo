#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.impute import KNNImputer
import tensorflow as tf  # For additional calculations if needed

# Load the CSV file into a DataFrame
df = pd.read_csv("DataKNN.csv")  # Update the file path as needed

# Define the KNN imputation function
def KNN_impute(input_data, k):
    """
    This function performs K-Nearest Neighbors (KNN) imputation for missing values in the dataset.
    
    :param input_data: The input DataFrame with missing values.
    :param k: The number of neighbors to consider for imputation.
    :return: DataFrame with imputed values.
    """
    imputer = KNNImputer(n_neighbors=k)
    df_filled = imputer.fit_transform(input_data)
    
    # Create a DataFrame from the imputed matrix with the same column names
    matrix = pd.DataFrame(df_filled, columns=["Habitat","Sector","Water_mass","Sediment","Lat_end_dec","Long_start_dec","Depth_CTD","Wind_end","Wind_speed_start","Wind_speed_end","Temperature_CTD","O2_saturation_CTD"])
    
    # Save the imputed data to a new CSV file
    matrix.to_csv("DataKNN_imputed" + str(k) + ".csv")
    
    return matrix

# Iterate over different values of k for KNN to find the best imputation and prediction results
for k in range(1, 11,1):  # Testing k from 1 to 10
    # Apply KNN imputation
    matrix = KNN_impute(df, k)
    
    # Initialize the KNeighborsRegressor model with k neighbors
    aws = KNeighborsRegressor(n_neighbors=k)
    
    # Separate the features (X) from the target variable (y)
    X = matrix.drop(columns=['O2_saturation_CTD'])  # Features
    y = matrix['O2_saturation_CTD']  # Target
    
    # Fit the KNN regression model on the entire dataset
    aws.fit(X, y)
    
    # Perform 10-fold cross-validation and calculate the mean squared error
    cv_scores = cross_val_score(aws, X, y, cv=10, scoring='neg_mean_squared_error')
    
    # Print the absolute mean of the cross-validated MSE for each value of k
    print(f"Mean Squared Error for k={k}: {tf.math.abs(cv_scores.mean()).numpy()}")
