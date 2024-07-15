import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

s = df["Name"]
# print(s)
s1 = df["Name"][0:10]
# print(s1)

l1 = list(s1)
il = ['a','b','c','d','e','f','g','h','i','j']
s2 = pd.Series(l1,index=il)
print(s2)