"""
Min-Max scaling ... It scales data between 0 to 1
Normalization :- second feature scaling method ...
Mostly used in deep learning.

X-scaled = (X-Xmin)/(xmax - xmin)
means x-scaled will be value between 0 to 1.

"""

import numpy as np

"""
Function for Normalization feature scaling technique it Scale down the datasets between 0 to 1
formula used  X-Scaled = (X-Xmin) / (Xmax - Xmin)
"""
# def Normalization(l):
#     min = np.min(l)
#     max = np.max(l)
#     normalised = []
#     for ele in l:
#         val = (ele - min)/(max - min)
#         normalised.append(val)
#     return normalised

# age = [24,25,26,27,28]
# print("Age ",age)
# normalised_age = Normalization(age)
# print("Normalised age ",normalised_age)


# we can verify it by plotting as well.

import seaborn as sns
import matplotlib.pyplot as plt

# sns.histplot(age)
# sns.histplot(normalised_age)
# plt.show()


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = sns.load_dataset("taxis")

min_max = MinMaxScaler()
min_max.fit(df[['distance','fare','tip']])
normalised_min_max = pd.DataFrame(min_max.fit_transform(df[['distance','fare','tip']]),columns=['distance','fare','tip'])
print(normalised_min_max)








