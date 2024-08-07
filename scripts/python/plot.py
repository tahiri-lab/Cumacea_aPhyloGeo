import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Create a new figure for the frequency plot
fig, ax = plt.subplots(figsize=(13, 8))  # Increased figure size

# Create a color palette
palette = sns.color_palette("hls", len(df['Scientific name'].unique()))

# Create a countplot with the color palette
sns.countplot(y='Scientific name', data=df, order=df['Scientific name'].value_counts().index, palette=palette)

# Set the labels and title
ax.set_xlabel('Count of Scientific Names', fontsize=13)
ax.set_ylabel('Scientific name', fontsize=13, labelpad=20)  # Adjusted label padding
ax.tick_params(axis='both', labelsize=13)  # Adjust tick label size

# Add statistics
total = len(df)
counts = df['Scientific name'].value_counts()
mean = counts.mean()
median = counts.median()
mode = counts.mode()[0]

for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_width()/total)
    x = p.get_x() + p.get_width() + 0.02
    y = p.get_y() + p.get_height()/2
    ax.annotate(percentage, (x, y), xytext=(15, 0), textcoords='offset points', fontsize=13)

# Add mean, median, and mode to the plot
# ax.annotate(f'Mean: {mean:.2f}', xy=(0.75, 0.95), xycoords='axes fraction')
# ax.annotate(f'Median: {median:.2f}', xy=(0.75, 0.90), xycoords='axes fraction')
# ax.annotate(f'Mode: {mode:.2f}', xy=(0.75, 0.85), xycoords='axes fraction')

# Add axes
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()  # Adjust layout to prevent overlap

plt.savefig('figure2.jpg', format='jpg', dpi=300)  # Save the figure as a jpg file

# Show the plot
plt.show()
