import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data2.csv')
columns = ['Lat start (dec)', 'Long start (dec)', 'Depth start (m)', 'Windspeed start (m/s)', 'Watertemp ground (°C)', 'O2-saturation ground (mg/L)']
fig, axs = plt.subplots(nrows=2, ncols=math.ceil(len(columns)/2), figsize=(8*math.ceil(len(columns)/2), 14), dpi=120)
palette = sns.color_palette("hls", len(columns))

for i, column in enumerate(columns):
    row = i // math.ceil(len(columns)/2)
    col = i % math.ceil(len(columns)/2)
    sns.violinplot(y=df[column], ax=axs[row][col], color=palette[i], orient='v', linewidth=1)
    axs[row][col].set_xlabel("")  
    axs[row][col].set_ylabel(column, fontsize=14)  
    axs[row][col].tick_params(axis='both', labelsize=14)  

    # Add statistics to the figure
    mean = df[column].mean()
    median = df[column].median()
    std_dev = df[column].std()
    quartiles = df[column].quantile([0.25, 0.75]).values
    # Position the statistics text in the top right corner
    axs[row][col].text(0.98, 0.95, f'Mean: {mean:.2f}\nMedian: {median:.2f}\nStd Dev: {std_dev:.2f}\nQ1: {quartiles[0]:.2f}\nQ3: {quartiles[1]:.2f}', 
                       transform=axs[row][col].transAxes, va='top', ha='right', fontsize=13)  

    # Position the subplot label in the top left corner
    axs[row][col].text(0.02, 0.95, f'{chr(97 + i)})', transform=axs[row][col].transAxes, va='top', ha='left', fontsize=14)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  
plt.subplots_adjust(hspace=0.1, wspace=0.13)  # Reduced hspace and wspace

plt.savefig('figure1.jpg', format='jpg', dpi=300)
plt.show()
