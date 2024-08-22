# label encoding...

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# df = pd.DataFrame({
#     "color":["red","blue","green","blue","green","green","blue","red","blue"]
# })

# # print(df)

# encoder = LabelEncoder()

# encoded = encoder.fit_transform(df["color"])

# final_df = pd.DataFrame(np.array(encoded),columns=["label_encoder"])

# new_df = pd.concat([df,final_df],axis=1)
# print(new_df)
