import pandas as pd

# data = {"a":[1,2,3,4],
#        "b":[4,5,6,7],
#        "c":["sudh" , "krish","hitesh","navin"]}

# df = pd.DataFrame(data)

# # print(df)

# # for i,j in df.iterrows():
# #     print(i,j)

# for i in df.items():
#     print(i)

df = pd.Series([1,2,3,4,5,6])

print(df.plot())

