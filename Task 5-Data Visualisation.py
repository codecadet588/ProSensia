# task5_data_visualization.py


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


#Matplotlib Basics
# ------------------------------

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 16]

# Line Chart
plt.plot(x, y, marker='o', color='blue')
plt.title("Simple Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()

# Bar Chart
categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 8]
plt.bar(categories, values, color='green')
plt.title("Bar Chart Example")
plt.show()

# Pie Chart
sizes = [30, 40, 20, 10]
labels = ["Apples", "Bananas", "Mangoes", "Oranges"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart Example")
plt.show()

# Histogram
data = np.random.randn(1000)  # 1000 random values
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.show()

# ------------------------------
#  Seaborn Visualizations
# ------------------------------

# Create a sample dataset
df = pd.DataFrame({
    "Category": np.random.choice(["A", "B", "C"], size=100),
    "Values": np.random.randint(1, 100, size=100),
    "Scores": np.random.randn(100) * 10 + 50
})

# Countplot (shows frequency of categories)
sns.countplot(x="Category", data=df, palette="Set2")
plt.title("Countplot Example")
plt.show()

# Boxplot (shows spread of data)
sns.boxplot(x="Category", y="Scores", data=df, palette="Set3")
plt.title("Boxplot Example")
plt.show()

# Heatmap (correlation between numeric columns)
corr = df.corr(numeric_only=True)  # calculate correlation matrix
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap Example")
plt.show()
