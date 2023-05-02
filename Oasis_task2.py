# -*- coding: utf-8 -*-
"""Sales Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tNb4rzCUcN0zRiykkTVSZ0qqfVV9N7bt

# ***SALES PREDICTION***
"""

import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

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

X = sales_df.drop('Sales', axis = 1)
y = sales_df['Sales']

X

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

