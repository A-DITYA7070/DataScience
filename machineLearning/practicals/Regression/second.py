#multiple linear regression...

from sklearn.datasets import fetch_california_housing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

california = fetch_california_housing()

dataset = pd.DataFrame(california.data,columns=california.feature_names)

dataset["Price"] = california.target

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=10)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression

regression = LinearRegression()

regression.fit(X_train_scaled,y_train)

y_pred_test = regression.predict(X_test_scaled)

# performance metrics cost function..

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

from sklearn.metrics import r2_score

score = r2_score(y_test,y_pred_test)

adjusted_r_squared = 1-(1-score) * (len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)

import pickle
pickle.dump(scaler,open('scaler.pkl','wb'))
pickle.dump(regression,open('regressor.pkl','wb'))

model_regressor = pickle.load(open('regressor.pkl','rb'))
model_regressor.predict(X_test_scaled)

standard_scaler = pickle.load(open('scaler.pkl','rb'))

model_regressor.predict(standard_scaler.transform(X_test))