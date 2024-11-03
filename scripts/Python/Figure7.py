import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load the CSV file
file_path = "output_1.csv"
data = pd.read_csv(file_path)

# Filter the data to keep only rows where 'Phylogeographic tree' is 'Windspeed_start'
filtered_data = data[data['Phylogeographic tree'] == 'Windspeed_start']

# Ensure the columns in the CSV file match the distances you want to represent
robinson_foulds_distance = filtered_data['Robinson-Foulds Distance']
normalized_rf_distance = filtered_data['Normalised RF Dist']
euclidean_distance = filtered_data['Euclidean Distance']
positions = filtered_data['Position in MSA']

# Create a figure with three rows and one column
fig, axs = plt.subplots(3, 1, figsize=(7, 11))

# Function to subsample x-axis labels (space out labels)
def space_labels(x_labels, step):
    return [label if i % step == 0 else '' for i, label in enumerate(x_labels)]

# Subplot for Robinson-Foulds Distance
axs[0].bar(positions, robinson_foulds_distance, color='green')
axs[0].set_xlabel("Position in MSA (aa)")
axs[0].set_ylabel('Robinson-Foulds distance')
axs[0].tick_params(axis='x', rotation=70, labelsize=6.5)
axs[0].set_ylim(50, 67.5)
axs[0].set_yticks([50.0, 52.5, 55.0, 57.5, 60.0, 62.5, 65.0, 67.5])
axs[0].text(-0.15, 1.05, 'a)', transform=axs[0].transAxes, fontsize=12, va='top', ha='right')

# Subplot for Normalized Robinson-Foulds Distance
axs[1].bar(positions, normalized_rf_distance, color='purple')
axs[1].set_xlabel("Position in MSA (aa)")
axs[1].set_ylabel('Normalized Robinson-Foulds distance')
axs[1].tick_params(axis='x', rotation=70, labelsize=6.5)
axs[1].set_ylim(0.90, 1.02)
axs[1].set_yticks([0.90, 0.92, 0.94, 0.96, 0.98, 1.00, 1.02])
axs[1].text(-0.15, 1.05, 'b)', transform=axs[1].transAxes, fontsize=12, va='top', ha='right')

# Subplot for Euclidean Distance
axs[2].bar(positions, euclidean_distance, color='orange')
axs[2].set_xlabel("Position in MSA (aa)")
axs[2].set_ylabel('Euclidean distance')
axs[2].tick_params(axis='x', rotation=70, labelsize=6.5)
axs[2].set_ylim(0.4, 0.9)
axs[2].set_yticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
axs[2].text(-0.15, 1.05, 'c)', transform=axs[2].transAxes, fontsize=12, va='top', ha='right')

# Adjust spacing between subplots
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save plots
plt.savefig('Figure7.png', format='png', dpi=300) # Save in png format

# Show plots
plt.show()
