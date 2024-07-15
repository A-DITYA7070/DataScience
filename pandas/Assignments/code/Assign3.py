# import pandas as pd
# course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
# duration = [2,3,6,4]
# df = pd.DataFrame(data = {'course_name' : course_name, 'duration' : duration})

# print(df.iloc[0,0])
# print(df)
# print(df.loc['course_name','0'])

# data = {
#     'a':["Aditya","raj"],
#     'b':["singh","rahul"]
# }

# df = pd.DataFrame(data)

# print(df.loc[0:0,['a']])

# reindex = [3,0,1,2]

# new_df = df.reindex(reindex)

# print(new_df.loc[2])
# print(new_df.iloc[2])

import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

df1['mean'] = df1.mean(axis=1)

# # print(df1)
# sd = df1['column_2'].std()
# print(sd)
# df1.loc[2,'column_2'] = 'aditya'
# df1.at[2,'column_2'] = "raj"
# df1.iloc[1,1] = "singh"
# print(df1)