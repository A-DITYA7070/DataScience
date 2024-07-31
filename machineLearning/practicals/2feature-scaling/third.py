"""
3. Unit vector scaling...
 unit vector := any vector with magnitude 1 is called unit vector.
 magnitude of |X| = sqrt(Xi*Xi + Yj*Yj)
 hence formula of unit vector scaling = (Xi/|X|)

"""
import numpy as np

# def UnitScaling(l):
#     scaled = []
#     magnitue = 0
#     for ele in l:
#         magnitue += ele**2
#     magnitue = np.sqrt(magnitue)
#     for ele in l:
#         scaled.append((ele/magnitue))
#     return scaled

# age = [24,25,26,27,28]
# scaled_age = UnitScaling(age)

# print("age",age)
# print("scaled age",scaled_age)
        
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import normalize


# df = sns.load_dataset("iris")

# normalize_data = pd.DataFrame(normalize(df[['sepal_length','sepal_width','petal_length','petal_width']]),columns=['sepal_length','sepal_width','petal_length','petal_width'])
# print(normalize_data)

# l = list(df['sepal_length'])

# nl = pd.Series(UnitScaling(l))

# print(nl)
# print(normalize_data['sepal_length'])






