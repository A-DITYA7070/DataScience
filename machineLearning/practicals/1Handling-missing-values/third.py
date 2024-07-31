#  Handling imbalanced datasets by smote.. (interpolation technique)

# SMOTE (synthetic minority oversampling technique) :- It is a technique used in ml to address imbalanced datasets where the minority class has significantly fewer instances than the majority class.
# SMOTE involves generating synthetic instances of the minority class by interpolating between existing instances.

from sklearn.datasets import make_classification

x,y = make_classification(
    n_samples=1000,
    n_features=2,
    n_clusters_per_class=1,
    weights=[0.90],
    random_state=12,
    n_redundant=0
    )


# x = independent feature y=dependent feature
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame(x,columns=['f1','f2'])
df2 = pd.DataFrame(y,columns=['target'])

final_df = pd.concat([df1,df2],axis=1)

# print(final_df)
# print(final_df['target'].value_counts())

# plt.scatter(final_df['f1'],final_df['f2'],c=final_df['target'])
# plt.show()

from imblearn.over_sampling import SMOTE

# transform the dataset

oversample = SMOTE()

x,y = oversample.fit_resample(final_df[['f1','f2']],final_df['target'])

# print(x.shape,y.shape)

df3 = pd.DataFrame(x,columns=['f1','f2'])
df4 = pd.DataFrame(y,columns=['target'])
oversample_df = pd.concat([df3,df4],axis=1)

# plt.scatter(oversample_df['f1'],oversample_df['f2'],c=oversample_df['target'])
# plt.show()

