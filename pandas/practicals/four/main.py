import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# print(df.columns)
# df1 = df.drop("Name",axis=1,inplace=True)
# print(df1)
# print(df)

df2 = pd.read_csv("taxonomy.csv")
print(df2)
df2.dropna(inplace=True)

