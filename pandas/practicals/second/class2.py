import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# print(df.head())

# print(df.dtypes)

# print(df.describe())

# desc = df[["Name","Sex","Ticket","Cabin","Embarked"]]
# print(desc)

# print(df.dtypes == "object")

# print(df.dtypes[df.dtypes == 'object'].index)

# print(df.dtypes[df.dtypes[df.dtypes == 'object'].index].describe())

# print(df[df.dtypes[df.dtypes == "float64"].index])

# print(df[df.dtypes[df.dtypes == 'int64'].index])

# print(df.columns)

# print(df[['Ticket','Cabin']][4:11:2])

# print(df)

# df["new_col1"] = df['PassengerId'] + df['Pclass']
# print(df)

# print(df["new_col1"])

# print(pd.Categorical(df['Survived']))

# print(df['Cabin'].unique())

# print(len(df[df['Age'] > 18])) 

# print(df[df['Age'] > 18])

# print(df[df['Fare'] > 32])


# print(df[df['Fare'] == 0])

# print(df[df["Sex"] == "male"])

# print(df[df["Survived"] == 1])

query1 = df[(df['Sex'] == 'female') & (df['Fare'] > 32)]
print(query1)