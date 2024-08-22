import warnings 
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("Salary_Data.csv")

"""
To train a linear regression model
1. Divide the feature based on independent and dependent feature.
2. Train Test and Split dataset.
3. Standardize the data (scaling).
4. Train the model using the linear regression.
"""

# 1. Defining the feature...

X = df["YearsExperience"].values.reshape(-1, 1)  # Independent feature
Y = df["Salary"].values.reshape(-1, 1)  # Dependent feature

# 2. Train test and split..

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

# 3. Standardize the dataset..
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)

# 4. Train the model

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred_test = regressor.predict(X_test)

# Predicting the salary based on years of experience
print("Enter the Year of Experience to predict the salary: ")
exp = float(input())  # Changed to float to accept decimal years
scaled_exp = scaler.transform([[exp]])
predicted_value = regressor.predict(scaled_exp)
print(f"The predicted salary for {exp} years of experience is: {predicted_value[0][0]:.2f}")

