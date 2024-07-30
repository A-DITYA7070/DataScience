# Handling missing data (feature enginnering) :-

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

# print(df.head())

# check missing value in dataset

# print(df.isnull())

# sns.heatmap(df.isnull())
# plt.show()

# Handling missing values 
# 1. by deleting all the rows with nan values. row wise

# df1 = df.dropna()
# print(df1)

# 2. by deleting columns.

# df1 = df.dropna(axis=1)
# print(df1)

# Imputation techniques..
# 1. Mean value imputation :- fill the missing values with mean of the column.
# Ex :- fill the missing values of age column with the mean of the age column.

# sns.distplot(df['age'])
# plt.show()
# print(df['age'].isnull().sum())

# df['Age_mean'] = df['age'].fillna(df['age'].mean())
# print(df[['Age_mean','age']])
# This technique works well when your data is normally distributed.

# 2. Median value imputation :- If the data has outliers then we can use this method to fill the missing values.
# Ex :- Lets fill the age column by median value imputation technique.
# df['Age_median'] = df['age'].fillna(df['age'].median())
# print(df[['Age_median','age']])
# use this method if your data set has outliers in the dataset

# 3. Mode value imputation :- This method can be usefull while dealing with categorical features.
# If we have missing value of MCAR (missing completely as random) we can use this technique.

# print(df['embarked'].unique())

# mode = df[df['age'].notna()]['embarked'].mode()[0]

# df['embarked_mode'] = df['embarked'].fillna(mode)

# print(df['embarked_mode'].isnull().sum())

# Note :- Basically these three methods are widely used to handle missing values in the dataset but we can 
# use one method i.e we can generate random value each time and fill the missing values.










