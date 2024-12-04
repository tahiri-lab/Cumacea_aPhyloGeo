# Load the necessary libraries
library(ggtree)
library(ggplot2)
library(aplot)
library(readr)

# Load phylogenetic tree from Newick file
tree_file <- "Final_sequences_aligned_all_treatment.nwk"
tr <- read.tree(tree_file)

# Load data from CSV file
data_file <- "Data_Density_Tree.csv"
data <- read_csv(data_file)

# Associate Depth CTD, Wind speed start, Temperature CTD and O2 concentration CTD values with tip labels
depth_data <- data.frame(
  label = data$`Specimen id`, # Tip names (must match labels in tree)
  Depth_CTD = data$`Depth CTD`, # Depth values
  Wind_speed_start = data$`Wind speed start`, # Wind speed values
  Temperature_CTD = data$`Temperature CTD`, # Temperature values
  O2_concentration_CTD = data$`O2 concentration CTD` # O2 concentration values
)

# Create heat map for Depth CTD variable (with labels)
p_depth <- ggplot(depth_data, aes(x="Depth CTD", y=label)) + 
  geom_tile(aes(fill=Depth_CTD)) + 
  scale_fill_gradient(low="cyan", high="darkblue", limits=c(313, 2568)) + 
  theme_minimal() + 
  xlab(NULL) + 
  ylab(NULL) + 
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank()) +
  labs(fill = "Wind speed start (m/s)") # Legend title for Depth CTD

# Create heatmap for Temperature CTD variable (without labels)
p_temperature <- ggplot(depth_data, aes(x="Temperature CTD", y=label)) + 
  geom_tile(aes(fill=Temperature_CTD)) + 
  scale_fill_gradient(low="blue", high="red", limits=c(-0.8511, 4.28)) + 
  theme_minimal() + 
  xlab(NULL) + 
  ylab(NULL) + 
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank(), axis.text.y=element_blank()) +
  labs(fill = "Temperature CTD (°C)") # Legend title for Temperature CTD

# Create heat map for variable O2 concentration CTD (without labels)
p_O2_concentration <- ggplot(depth_data, aes(x="O2 concentration CTD", y=label)) + 
  geom_tile(aes(fill=O2_concentration_CTD)) + 
  scale_fill_gradient(low="purple", high="orange", limits=c(245.53, 292.966)) + 
  theme_minimal() + 
  xlab(NULL) + 
  ylab(NULL) + 
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank(), axis.text.y=element_blank()) +
  labs(fill = "O2 concentration CTD (mg/L)") # Legend title for O2 concentration CTD

# Create heatmap for Wind speed start variable (without labels)
p_wind_speed <- ggplot(depth_data, aes(x="Wind speed start", y=label)) + 
  geom_tile(aes(fill=Wind_speed_start)) + 
  scale_fill_gradient(low="yellow", high="green", limits=c(2, 11)) + 
  theme_minimal() + 
  xlab(NULL) + 
  ylab(NULL) + 
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank(), axis.text.y=element_blank()) +
  labs(fill = "Wind speed start (m/s)") # Legend title for Temperature CTD

# View phylogenetic tree
g <- ggtree(tr) + 
  geom_tiplab(align=TRUE) + # Add aligned tip labels
  hexpand(.01) # Adjust horizontal spacing

# Combine tree, Depth CTD, Wind speed start, Temperature CTD and O2 concentration CTD
final_plot <- p_depth %>% 
  insert_left(g) %>% 
  insert_right(p_temperature, width = 0.9) %>% 
  insert_right(p_O2_concentration, width = 0.9) %>% 
  insert_right(p_wind_speed, width = 0.9)

# Save combined plot as SVG
ggsave("Gradient_plot_Article.svg", plot = final_plot, width = 10, height = 8, dpi = 300, device = "svg")

# Save combined plot as PNG
ggsave("Gradient_plot_Article.png", plot = final_plot, width = 10, height = 8, dpi = 300, device = "png")

# Display combined plot
final_plot
