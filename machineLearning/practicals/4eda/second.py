import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("forest.csv",header=1)
# print(df.head())
data = df.to_dict(orient="records")

# Checks to perform ..
"""
1. Check missing values
2. check duplicates
3. Check data type.
4. Check the number of unique values of each columns.
5. Check statics of data set.
6. Check various categories present in the different categorical column
"""

# 1. checking missing values..
# missing_values = df.isnull().sum()
# print(missing_values)

df[df.isnull().any(axis=1)]

df.loc[:122,"Region"]=1
df.loc[122:,"Region"]=2
df[["Region"]]=df[["Region"]].astype(int)

# print(df.isnull().sum())
df = df.dropna().reset_index(drop=True)
# print(df.shape)

df = df.drop(122).reset_index(drop=True)

# print(df.columns)

df.columns = df.columns.str.strip()
# print(df.columns)
