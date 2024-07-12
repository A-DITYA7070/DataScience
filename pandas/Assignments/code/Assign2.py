# import pandas as pd
# # Function to reindex the dataframe.
# def reindex_dataframe(df):
#     new_index = range(1, 2 * len(df) + 1, 2)
#     df = df.set_index(pd.Index(new_index))
#     return df

# data = {
#     'A':[1,2,3],
#     'B':[4,5,6],
#     'C':[7,8,9]
# }
# df = pd.DataFrame(data)
# # Printing the dataframe before applying reindexing
# print(df)
# # Printing the datafrane after applying reindexing.
# reindex = reindex_dataframe(df)
# # print(reindex)


# import pandas as pd
# # Function to calculate the sum of first 3 elements of Column Values of DataFrame df
# def SumOfEle(df):
#     val = df["Values"]
#     sum = val[0] + val[1] + val[2]
#     return sum

# data = {
#     "Values":[23,12,50,48,50,30]
# }

# df = pd.DataFrame(data)
# print(SumOfEle(df))


# import pandas as pd
# # Function to count word count in a string
# def wordCount(str):
#     words = str.split()
#     return len(words)
# # Function to create new Column word_count and add word Counts of Text
# def NewColumnWordCount(df):
#     ele = df["Text"]
#     for i in range(0,len(ele)):
#         df["word_count"] = df["Text"].apply(wordCount)
#     return df

# data = {
#     "Text":["I am a good boy","you are bad","very good","bad boy"]
# }

# df = pd.DataFrame(data)
# print(NewColumnWordCount(df))
