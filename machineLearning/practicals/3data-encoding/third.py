import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder

# df = pd.DataFrame({
#     "color":["red","green","blue","blue","green","red","green","blue","red","blue"]
# })

# encoder = OrdinalEncoder()

# encoded = encoder.fit_transform(df[["color"]])

# new_df = pd.DataFrame(encoded,columns=["color"])

# encoded_df = pd.concat([df,new_df],axis=1)

# print(encoded_df)


df = sns.load_dataset("flights")
# print(df.head())

encoder = OrdinalEncoder()
encoded = encoder.fit_transform(df[["month"]])
# print(encoded)
new_df = pd.DataFrame(encoded,columns=["ordinal rank"])

encoded_df = pd.concat([df,new_df],axis=1)

print(encoded_df.head())
