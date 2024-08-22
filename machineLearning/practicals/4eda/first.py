import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# EDA

df = pd.read_csv("stud.csv")
# print(df.head())

# print(df.shape)

# To perform EDA on any datasets...
# Checks to perform ..
"""
1. Check missing values
2. check duplicates
3. Check data type.
4. Check the number of unique values of each columns.
5. Check statics of data set.
6. Check various categories present in the different categorical column
"""
# 1.check missing values
# print(df.isnull().sum())
# print(df.isna().sum())
# Observation :- There are no missing values in the data set

# 2. check duplicates.
# print(df.duplicated().sum())
# Observation :- There are no duplicates in the data set.

# 3. check data types
# print(df.info())
# Observation :- first 5 columns have object data type --- categorical feature
                #  next three columns have int64 datatypes

#4. Check the number of unique values of each columns.
# print(df.nunique())
# Observation:--

#5. Check the statics of data set.
# print(df.describe())
# Observation :- 

#6. Check various categories present in the different categorical column..
# print(df.head())
# print(df.tail())

# seggrigate categorical and numerical feature..
# categorical_feature = [feature for feature in df.columns if df[feature].dtype=="O"]
# numerical_feature = [feature for feature in df.columns if df[feature].dtype!="O"]

# print(categorical_feature)
# print(numerical_feature)

# Aggregate the total score with mean..
df['total_score'] = df["math_score"]+df["reading_score"]+df["writing_score"]
df["average"] = df["total_score"]/3
# print(df.head())

# Expore more visualisation...
# fig,axis = plt.subplots(1,2,figsize=(15,7))
# plt.subplot(121)
# sns.histplot(data=df,x="average",bins=30,kde=True,color="green")
# plt.subplot(122)
# sns.histplot(data=df,x="average",bins=30,kde=True,hue="gender")
# plt.subplot(141)
# sns.histplot(data=df,x="average",kde=True,hue="lunch")
# plt.subplot(142)
# sns.histplot(data=df[df.gender == "female"],x="average",kde=True,hue="lunch")
# plt.show()

# Inshights :- Female students tend to perform well than male students..
#  :- standard lunch helps perform well in exam..

# fig,axis = plt.subplots(1,2,figsize=(25,6))
# plt.subplot(141)
# sns.histplot(data=df,x="average",kde=True,hue="parental_level_of_education")
# plt.subplot(142)
# sns.histplot(data=df[df.gender == "female"],x="average",kde=True,hue="parental_level_of_education")
# plt.subplot(143)
# sns.histplot(data=df[df.gender == "male"],x="average",kde=True,hue="parental_level_of_education")
# plt.show()

# Observation
"""
1. In general parent education dont help student perform well
2. 2nd plot show that parents whose education is of associate of master's degree their male child tend to perform well
   in exam..
3. 3rd plot show there is no effect of parent's education on female students..
""" 

# sns.heatmap(df.corr(),annot=True)
# plt.show()