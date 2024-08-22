# # Nominal or OHE Encoding..

# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# df = pd.DataFrame({
#     'colors':["red","blue","green","green","red","blue","green","red","green"]
# })

# # Create an instance of OHE
# encoder = OneHotEncoder()

# encoded = encoder.fit_transform(df[['colors']])

# encoded_df = pd.DataFrame(encoded.toarray(),columns=encoder.get_feature_names_out())

# final_df = pd.concat([df,encoded_df],axis=1)

# print(final_df)

# Internal assignment...

# import seaborn as sns
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# encoder = OneHotEncoder()

# df = sns.load_dataset('tips')

# encoded = encoder.fit_transform(df[["day"]])

# encoded_df = pd.DataFrame(encoded.toarray(),columns=encoder.get_feature_names_out())

# # print(encoded_df)

# final_df = pd.concat([df,encoded_df],axis=1)

# print(final_df)

# import pandas as pd
# import seaborn as sns
# from sklearn.preprocessing import OneHotEncoder

# df = sns.load_dataset("iris")

# encoder = OneHotEncoder()

# enocded = encoder.fit_transform(df[["species"]])

# encoded_df = pd.DataFrame(enocded.toarray(),columns=encoder.get_feature_names_out())

# final_df = pd.concat([df,encoded_df],axis=1)

# print(final_df)


# import pandas as pd
# import seaborn as sns
# from sklearn.preprocessing import OneHotEncoder

# encoder = OneHotEncoder()

# df = sns.load_dataset("penguins")
# encoded = encoder.fit_transform(df[["island"]])

# encoded_df = pd.DataFrame(encoded.toarray(),columns=encoder.get_feature_names_out())


# final_df = pd.concat([df,encoded_df],axis=1)
# print(final_df)

# import pandas as pd
# import seaborn as sns
# from sklearn.preprocessing import OneHotEncoder
# import numpy as np


# encoder = OneHotEncoder()

# df = sns.load_dataset("flights")
# # print(df.head)
# mode = df[["month"]].mode()
# new_df = df[["month"]].fillna(mode)

# encoded = encoder.fit_transform(new_df[["month"]])

# encoded_df = pd.DataFrame(encoded.toarray(),columns=encoder.get_feature_names_out())

# final_df = pd.concat([df,encoded_df],axis=1)
# print(df)
# print(final_df)






