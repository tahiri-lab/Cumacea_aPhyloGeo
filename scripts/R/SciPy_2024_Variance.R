# Import data
Data <- read.csv(file="SciPy_2024_data_preprocessing.csv", header=TRUE)

# Exclude specific columns
Data <- Data[ , !(names(Data) %in% c("Field_id", "Family", "Genus", "Scientific_name"))]

# Define a function to calculate entropy for categorical variables
calculate_entropy <- function(x) {
  # Calculate the frequency of each category
  freq_table <- table(x)
  
  # Calculate probabilities
  probabilities <- freq_table / sum(freq_table)
  
  # Calculate entropy using the probabilities
  entropy_value <- -sum(probabilities * log(probabilities), na.rm=TRUE)
  
  return(entropy_value)
}

# Calculate variance or entropy based on column type
variances_entropies <- sapply(Data, function(x) {
  if (is.numeric(x)) {
    # Compute variance for numeric columns
    var(x, na.rm=TRUE)
  } else if (is.factor(x) || is.character(x)) {
    # Compute entropy for categorical columns
    calculate_entropy(x)
  } else {
    NA  # Return NA for other types of columns
  }
})

# Display variances/entropies
print(variances_entropies)
