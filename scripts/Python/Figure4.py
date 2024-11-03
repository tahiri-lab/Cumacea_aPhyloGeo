import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('SciPy_2024_data_preprocessing.csv')

# Create a new figure for the frequency graph
fig, ax = plt.subplots(figsize=(13, 8)) # Increase figure size

# Create a color palette based on families
palette = sns.color_palette("Set2", len(df['Family'].unique()))  # Use 'Set2' palette

# Create a countplot with the family as hue
sns.countplot(y='Scientific_name', data=df, order=df['Scientific_name'].value_counts().index, 
              palette=palette, hue='Family')

# Add labels and title
ax.set_xlabel("Number of specimens", fontsize=13)
ax.set_ylabel("Species", fontsize=13, labelpad=20) # Adjust label space
ax.tick_params(axis='both', labelsize=13) # Adjust label size

# Italicize species names
ax.set_yticklabels([f'{label.get_text()}' for label in ax.get_yticklabels()], style='italic')

# Calculate statistics
total = len(df)
counts = df['Scientific_name'].value_counts()
mean = counts.mean()
median = counts.median()
mode = counts.mode()[0]

# Annotate bars with percentages
for p in ax.patches:
    if p.get_width() > 0: # Do not display annotations 0.0%
        percentage = '{:.1f}%'.format(100 * p.get_width()/total)
        x = p.get_x() + p.get_width() + 0.02
        y = p.get_y() + p.get_height()/2
        ax.annotate(percentage, (x, y), xytext=(15, 0), textcoords='offset points', fontsize=13)

# Position legend at center left with larger text size
ax.legend(title="Families", bbox_to_anchor=(1, 0.5), loc='center left', fontsize=16, title_fontsize=16) # Increase legend size

# Add visible axes, except right and top
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('Figure4.png', format='png', dpi=300) # Save in png format

# Display graphic
plt.show()