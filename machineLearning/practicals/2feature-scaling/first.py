# Feature scaling
# 1.Standralization
# 2. Normalization
# 3. unit vector 

# import numpy as np

# standralization z-score = (x-mean)/std 

# def standralization(l):
#     std_l = []
#     mean = np.mean(l)
#     std = np.std(l)
#     for ele in l:
#         std_l.append((ele-mean)/std)
#     return std_l

# age = [24,25,26,27,28]
# print("Age ",age)
# std_age = standralization(age)
# print("Standralization of age ",std_age)
# print("mean",np.mean(std_age),"std",np.std(std_age))
"""
After standralization mean becomes 0 and std becomes 1 
"""

import seaborn as sns
# import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('tips')

# total_bill = list(df['total_bill'])

# total_bill_std = standralization(total_bill)

# print(total_bill)
# print(total_bill_std)

# sns.histplot(total_bill_std)
# plt.show()


# we can directly apply the standralization function using sklearn library..
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(df[['total_bill','tip']])

df2 = pd.DataFrame(scaler.transform(df[['total_bill','tip']]),columns=['total_bill','tip'])

print(df2)



