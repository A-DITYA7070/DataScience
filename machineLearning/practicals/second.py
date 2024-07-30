                    #    Upsampling and downsampling :--

import numpy as np
import pandas as pd

# set the random seed for reproducibility
np.random.seed(123)
# create a dataframe with two classes
n_samples = 1000
class_0_ratio = 0.9
n_class_0 = int(n_samples * class_0_ratio)
n_class_1 = n_samples - n_class_0

# print(n_class_0)
# print(n_class_1)

class_0 = pd.DataFrame({
    'feature_1' : np.random.normal(loc=0,scale=1,size=n_class_0),
    'feature_2' : np.random.normal(loc=0,scale=1,size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1' : np.random.normal(loc=2,scale=1,size=n_class_1),
    'feature_2' : np.random.normal(loc=2,scale=1,size=n_class_1),
    'target' : [1] * n_class_1
})

df = pd.concat([class_0,class_1]).reset_index(drop=True)

# print(df['target'].value_counts())

df_minority = df[df['target'] == 1]
df_majority = df[df['target'] == 0]

# print(df_majority)
# print(df_minority)

# upsampling  :- To perform upsampling we will use sklearn library

from sklearn.utils import resample

# df_minority_upsample = resample(df_minority,replace=True,n_samples=len(df_majority),random_state=42)

# print(df_minority_upsample.shape)
# print(df_minority_upsample['target'].value_counts())

# df_upsampled = pd.concat([df_majority,df_minority_upsample])
# print(df_upsampled['target'].value_counts())

# downsampling :--

df_majority_downsample = resample(df_majority,replace=False,n_samples=len(df_minority),random_state=42)
# print(df_majority_downsample.shape)

df_downsampled = pd.concat([df_minority,df_majority_downsample])
# print(df_downsampled['target'].value_counts())







