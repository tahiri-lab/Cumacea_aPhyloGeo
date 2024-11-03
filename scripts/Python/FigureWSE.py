import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('SciPy_2024_data_preprocessing.csv', sep=",")

# Specify the column to plot
column = 'Wind_speed_end'
column_name = "Wind speed at the end of sampling (m/s)"

# Create a figure for the violin plot
plt.figure(figsize=(8, 6), dpi=120)

# Generate the violin plot with a specific blue color
sns.violinplot(y=df[column], color="#6DAEDB", orient='v', linewidth=1)  # Hex color for blue similar to the image
plt.ylabel(column_name, fontsize=14)
plt.xlabel("")  
plt.tick_params(axis='both', labelsize=14)

# Calculate and plot the median line
median = df[column].median()
x_center = plt.gca().collections[0].get_paths()[0].vertices[:, 0].mean()
plt.plot([x_center - 0.01, x_center + 0.01], [median, median], color='white', linestyle='-', linewidth=2)

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('FigureWSE.png', format='png', dpi=300) # Save in png format

# Show the plot
plt.show()