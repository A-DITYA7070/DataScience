import numpy as np

ages_list = [23,34,23,12,34,45,56,56,4,34,34,32,25,26]

# mean
# print(np.mean(ages_list))
# variance
# print(np.var(ages_list))
# std
# print(np.std(ages_list))

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# sns.histplot(ages_list,kde=True)
# plt.show()

data = [[10,20,30],[34,45,56],[32,34,34]]

df = pd.DataFrame(data)

print(df.head())
print(df.var())
print(df.var(axis=1))
