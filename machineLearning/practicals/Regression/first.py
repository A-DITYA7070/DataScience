# Simple Linear Regression..

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# There is height and weight weight is independent feature and height is dependent feature train model and predict the height upon any given input weight.

df = pd.read_csv("height_weight.csv")

# print(df.head())

# plt.scatter(df['Weight'],df['Height'])
# plt.xlabel("weight")
# plt.ylabel("height")
# plt.show()

# To train a model 
"""
1) Divide the feature based on independent feature and dependent feature.
2) Train Test and split of the dataset.
3) Standradize the data. (scale down the data.)
4) Train the model using linear regression
"""

X = df[['Weight']] #Independent feature.
Y = df[['Height']] #Dependent feature.

from sklearn.model_selection import train_test_split

# (x_train is training dataset and y_test is test dataset i.e (whole dataset is divided into training and test data set, x_train is input and y_train is output of training dataset similarly x_test and y_test is separated))

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.20,random_state=42)

# print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)

# standradize the data..
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train  = scaler.fit_transform(x_train)
# print(X_train)
X_test = scaler.transform(x_test)

# plt.scatter(X_train,y_train)
# plt.show()


# Train the model (simple linear regression model)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train,y_train)

# print("The slope of coefficient of weight is ",regressor.coef_)
# print("Intercept",regressor.intercept_)

# plt.scatter(X_train,y_train)
# plt.plot(X_train,regressor.predict(X_train),'r')
# plt.show()

Y_pred_test = regressor.predict(X_test)

# plt.scatter(X_test,y_test)
# plt.plot(X_test,regressor.predict(X_test),'r')
# plt.show()

# performace metrics..
# MSE,MAE,RMSE

from sklearn.metrics import mean_squared_error,mean_absolute_error

mse = mean_squared_error(y_test,Y_pred_test)
mae = mean_absolute_error(y_test,Y_pred_test)
rmse = np.sqrt(mse)
# print(mse,mae,rmse)
from sklearn.metrics import r2_score

score = r2_score(y_test,Y_pred_test)
# print(score)
adjusted_r_square = 1 - (1-score)*(len(y_test)-1)/(len(y_test) - X_test.shape[1]-1)
# print(adjusted_r_square)

# new data point weight is 80

scaled_weight = scaler.transform([[80]])
predicted_value = regressor.predict([scaled_weight[0]])
print("the height prediction for weight 80 kg is ",predicted_value)

# Assumption for good model in simple regression model..
'''
1) Plot a scatter plot for the prediction.. (If the scatter plot is linearly distributed then the model is performing well)
2) Resuduals = y_test - Y_pred_test
3) plot residuals (if getting normal distribution then prediction is good)
4) scatter plot with respect to prediction and residuals (uniform distribution)
'''

residuals = y_test - Y_pred_test
# print(residuals)
# plt.scatter(y_test,Y_pred_test)
# plt.show()

import seaborn as sns
# sns.distplot(residuals,kde=True)
# plt.show()

# plt.scatter(Y_pred_test,residuals)
# plt.show()



