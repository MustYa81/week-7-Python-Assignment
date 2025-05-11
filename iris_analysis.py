import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
df = pd.read_csv(url)

# Add a simulated Date column for time series
df['Date'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')

# 1. Basic Statistics
print("Basic Statistics:\n", df.describe())

# 2. Group by species and compute mean
grouped_means = df.groupby('species').mean()
print("\nMean values grouped by species:\n", grouped_means)

# Set style for plots
sns.set(style="whitegrid")

# 3. Visualizations

# Line Chart - Petal Length Over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['petal_length'], label='Petal Length', color='teal')
plt.title('Petal Length Over Time')
plt.xlabel('Date')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.tight_layout()
plt.savefig("line_chart_petal_length.png")
plt.show()

# Bar Chart - Average Petal Length per Species
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='species', y='petal_length', ci=None, palette='Set2')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.savefig("bar_chart_petal_length.png")
plt.show()

# Histogram - Sepal Width Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_width'], bins=15, kde=True, color='salmon')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("histogram_sepal_width.png")
plt.show()

# Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species', palette='viridis')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.savefig("scatterplot_sepal_vs_petal.png")
plt.show()
