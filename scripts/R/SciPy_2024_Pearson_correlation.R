# Import data 
Data <- read.csv(file = "SciPy_2024_data_preprocessing.csv", header=T)

# Select numeric columns only
numeric_Data <- Data[sapply(Data, is.numeric)]

# Calculate Pearson correlation matrix
correlation_matrix <- cor(numeric_Data, use = "pairwise.complete.obs")

# Display correlation matrix
print(correlation_matrix)
