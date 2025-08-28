# task6_machine_learning_intro.py


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix

# Create a sample dataset
# ------------------------------
# Let's pretend this is student data
data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,10],
    "Sleep_Hours": [9,8,8,7,7,6,6,5,5,4],
    "Score": [35,40,50,55,60,65,70,75,85,90],   # continuous values
    "Pass": [0,0,0,1,1,1,1,1,1,1]               # classification (0 = Fail, 1 = Pass)
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

#  Features and Target
# ------------------------------
X = df[["Hours_Studied", "Sleep_Hours"]]   # features
y_reg = df["Score"]                        # target for regression
y_clf = df["Pass"]                         # target for classification

# Split the dataset
# ------------------------------
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.3, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.3, random_state=42)

#  Feature Scaling
# ------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#  Linear Regression Model
# ------------------------------
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train_reg)

# Make predictions
y_pred_reg = lin_reg.predict(X_test_scaled)
print("\nLinear Regression Predictions:", y_pred_reg)

# Evaluate with Mean Squared Error
mse = mean_squared_error(y_test_reg, y_pred_reg)
print("Linear Regression MSE:", mse)

#  K-Nearest Neighbors Classifier
# ------------------------------
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train_clf)

# Make predictions
y_pred_clf = knn.predict(X_test_scaled)
print("\nKNN Predictions:", y_pred_clf)

# Evaluate with Accuracy
accuracy = accuracy_score(y_test_clf, y_pred_clf)
print("KNN Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test_clf, y_pred_clf)
print("Confusion Matrix:\n", cm)
