import pandas as pd

# data = [4,5,6,7,8]
# series = pd.Series(data)
# print(series)

# data = ['a','b','c','adi','raj','rahul','rohit','ram','kunal','surya']
# series = pd.Series(data)
# print(series)


# data = [
#     ["Alice",25,"Female"],
#     ["Bob",30,"Male"],
#     ["Claire",27,"Female"]
# ]
# df = pd.DataFrame(data,columns=["Name","Age","Gender"])
# print(df)


names = pd.Series(["adi","alice","bob"])
ages = pd.Series([23,34,45])
grades = pd.Series([9,8,7])
data = {
    "name":names,
    "age":ages,
    "grade":grades
}
df = pd.DataFrame(data)
print(df)
