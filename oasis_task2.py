# -*- coding: utf-8 -*-
"""Sales Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tNb4rzCUcN0zRiykkTVSZ0qqfVV9N7bt

# ***SALES PREDICTION***
"""

#IMPORT LIBRARIES

import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

"""*DATA PROCESSING*"""

path = '/content/drive/MyDrive/DATASETS/Advertising.csv'

sales_df = pd.read_csv(path)

sales_df

sales_df.head(5)

sales_df.shape

sales_df.info()

sales_df.tail(5)

sales_df.describe()

sales_df.columns

sales_df.duplicated().sum()

"""***DATA VISUALIZATION***"""

plt.figure(figsize=(4,4))
sns.scatterplot(data=sales_df,x=sales_df['TV'],y=sales_df['Sales'])
plt.show()

plt.figure(figsize=(4,4))
sns.scatterplot(data=sales_df,x=sales_df['Radio'],y=sales_df['Sales'])
plt.show()

plt.figure(figsize=(4,4))
sns.scatterplot(data=sales_df,x=sales_df['Newspaper'],y=sales_df['Sales'])
plt.show()

sns.jointplot(x='TV', y ='Sales', data = sales_df)

sns.jointplot(x='Radio', y ='Sales', data = sales_df)

sns.jointplot(x='Newspaper', y ='Sales', data = sales_df)

plt.figure(figsize=(17,7))
plt.xticks(rotation=180)
sns.histplot(x=sales_df['Radio'], y=sales_df['Newspaper'] , color = "orange")
plt.show()

plt.style.use("dark_background")

color_palette = sns.diverging_palette(250,0,center = 'dark' , as_cmap = True)

plt.figure(figsize=(17,7))

plt.xticks(rotation=180)
sns.lineplot(x=sales_df['Radio'], y=sales_df['Sales'] , color = "orange")
plt.show()

plt.style.use("dark_background")

color_palette = sns.diverging_palette(250,0,center = 'dark' , as_cmap = True)

plt.figure(figsize=(17,7))

plt.xticks(rotation=180)
sns.lineplot(x=sales_df['Newspaper'], y=sales_df['Sales'] , color = "orange")
plt.show()

plt.style.use("dark_background")

color_palette = sns.diverging_palette(250,0,center = 'dark' , as_cmap = True)

plt.figure(figsize=(17,7))

plt.xticks(rotation=180)
sns.lineplot(x=sales_df['TV'], y=sales_df['Sales'] , color = "orange")
plt.show()

plt.style.use("dark_background")

color_palette = sns.diverging_palette(250,0,center = 'dark' , as_cmap = True)

X = sales_df.drop('Sales', axis = 1)
y = sales_df['Sales']

X

"""***TRAINING AND TESTING DATA***"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LinearRegression

mlr = LinearRegression()

mlr.fit(X_train,y_train)

print("intercep", mlr.intercept_)
print("coefficents: ")
list(zip(X,mlr.coef_))

y_pred = mlr.predict(X_test)
print("prediction{}".format(y_pred))

mlr_dif = pd.DataFrame({"gerçek değer": y_test, "tahmin edilen": y_pred})

mlr_dif.head()

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

model_dt = DecisionTreeRegressor()
model_dt.fit(X_train, y_train)
y_pred_dt = model_dt.predict(X_test)
mse_dt = mean_squared_error(y_test , y_pred_dt)
print('Decision Tree MSE:' , mlr)

model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)
mse_rf = mean_squared_error(y_test , y_pred_rf)
print('Random Forest:' , mse_rf)

print("Linear Regression R^2:" , mlr.score(X_test, y_test))
print("Decision Tree R^2:" , model_dt.score(X_test, y_test))
print("Random Forest R^2:" , model_rf.score(X_test, y_test))

