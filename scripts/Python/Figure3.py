# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

# Load data from a CSV file into a DataFrame
df = pd.read_csv('SciPy_2024_data_preprocessing.csv')

# Define columns to visualize and their respective labels
columns = ['Lat_end_dec', 'Long_start_dec', 'Depth_start', 'Wind_speed_start', 'Watertemp_ground', 'O2-saturation_ground']  # Removed 'Wind_speed_end'
column_names = [
    "Latitude at the end of sampling (DD)", 
    "Longitude at the start of sampling (DD)", 
    "Depth at the start of sampling (m)", 
    "Wind speed at the start of sampling (m/s)", 
    "Water temperature at the sampling site (°C)", 
    "O\u2082 concentration at the sampling (mg/L)"
]

# Set up a grid of subplots with 2 rows and a calculated number of columns
fig, axs = plt.subplots(
    nrows=2, 
    ncols=math.ceil(len(columns)/2),  # Columns adjusted to fit all plots
    figsize=(8 * math.ceil(len(columns)/2), 14),  # Define figure size
    dpi=120  # Set resolution
)

# Use a color palette to have distinct colors for each plot
palette = sns.color_palette("hls", len(columns))

# Loop over each column to create individual violin plots
for i, column in enumerate(columns):
    row = i // math.ceil(len(columns)/2)  # Determine subplot row index
    col = i % math.ceil(len(columns)/2)   # Determine subplot column index
    
    # Create a violin plot for each selected column
    sns.violinplot(
        y=df[column], 
        ax=axs[row][col], 
        color=palette[i], 
        orient='v', 
        linewidth=1
    )
    
    # Remove x-axis label (since the y-axis is the focus here)
    axs[row][col].set_xlabel("")
    
    # Set y-axis label with specific font size
    axs[row][col].set_ylabel(column_names[i], fontsize=14)
    
    # Adjust the size of tick labels for clarity
    axs[row][col].tick_params(axis='both', labelsize=14)
    
    # Calculate statistical values for each variable
    mean = df[column].mean()
    median = df[column].median()
    std_dev = df[column].std()
    quartiles = df[column].quantile([0.25, 0.75]).values

    # Get x-center of the violin plot to position the median line
    x_center = axs[row][col].collections[0].get_paths()[0].vertices[:, 0].mean()
    
    # Plot the median line across the center of the violin plot
    axs[row][col].plot(
        [x_center - 0.01, x_center + 0.01],  # Slight offset around the x-center
        [median, median],  # Median y-value
        color='white', 
        linestyle='-', 
        linewidth=2
    )

# Adjust layout to avoid overlaps and enhance readability
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.subplots_adjust(hspace=0.1, wspace=0.13)  # Reduce space between subplots

# Save figure
plt.savefig('Figure3.png', format='png', dpi=300) # Save in png format

# Display the plots
plt.show()
