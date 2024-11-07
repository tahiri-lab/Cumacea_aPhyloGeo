library(ggplot2)

#Import dataset
DS<-read.csv(file = "SciPy_2024_data_preprocessing.csv", header=T)

# Create a data frame with the data
dataF5 <- data.frame(Families = DS$Family, Water_masses = DS$Water_mass)

# ggplot2 Distribution of Cumacea families by water mass
p <- ggplot(dataF5, aes(x = Water_masses, fill = Families )) +
  geom_bar() +
  labs(x = "Water masses",
       y = "Number of specimens") +
  theme_minimal(base_size = 15) +  # Set a base size for text
  theme(
    axis.title.x = element_text(size = 18),  # X-axis title size
    axis.title.y = element_text(size = 18),  # Y-axis title size
    axis.text.x = element_text(size = 14),   # X-axis labels size
    axis.text.y = element_text(size = 14),   # Y-axis labels size
    legend.title = element_text(size = 16),  # Legend title size
    legend.text = element_text(size = 14)    # Size of legend texts
  )

# Display the distribution
print(p)
