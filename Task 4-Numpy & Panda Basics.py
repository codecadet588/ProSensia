 #day6_numpy_pandas_basics.py

# Importing the two main libraries we will use
import numpy as np
import pandas as pd

# NumPy Basics
# ------------------------------

# Create a simple NumPy array
numbers = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", numbers)

# Perform vectorized operations 
print("Array + 10:", numbers + 10)
print("Array squared:", numbers ** 2)

# Create a 2D array 
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", matrix)

# ------------------------------
#  Pandas Basics
# ------------------------------

# Create a Pandas Series 
fruits = pd.Series(["Apple", "Banana", "Mango", "Orange", "Banana"])
print("\nPandas Series:\n", fruits)

# Create a Pandas DataFrame 
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zara", "Ali"],
    "Age": [20, 22, 19, None, 20],
    "Marks": [85, 90, None, 78, 85]
}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

# --------------------------
#  Data Cleaning
# ------------------------------

# Handle missing values 
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# Drop rows where "Age" is missing
df.dropna(subset=["Age"], inplace=True)

# Convert Age column to integer
df["Age"] = df["Age"].astype(int)

print("\nCleaned DataFrame:\n", df)

# ------------------------------
# Data Selection & Filtering
# ------------------------------

# Select a single column
print("\nNames Column:\n", df["Name"])

# Filter: Students with Marks greater than 80
top_students = df[df["Marks"] > 80]
print("\nStudents with Marks > 80:\n", top_students)

# Get summary statistics
print("\nSummary Statistics:\n", df.describe())

# ------------------------------
# Remove duplicates
# ------------------------------
df_unique = df.drop_duplicates()
print("\nDataFrame without duplicates:\n", df_unique)
