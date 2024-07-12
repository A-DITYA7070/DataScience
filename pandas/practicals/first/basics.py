import pandas as pd

df = pd.read_csv("services.csv")
# print(df.head(6))

#printing the dataset from the last.
# print("printing tail of the dataset")
# print(df.tail())

# print(df.head(3),None)

# print(df.columns)

# To select the specific column data.
# print(df["languages"])

# print(df["status"])
# print(list(df["status"]))

# we can select multiple columns as well.
# print(df[["name","email"]])
# print(df.dtypes)

# Reading excel files.

dex = pd.read_excel("data.xlsx")

# print(type(dex))
print(dex.head())

