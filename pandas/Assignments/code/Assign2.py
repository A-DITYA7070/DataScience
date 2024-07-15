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

# import pandas as pd
# # Function to extract part of email before '@'
# def extract_username(email):
#     if "@" in email:
#         return email.split('@')[0]
#     else:
#         return None
# # Function to create new column Username and assign usernames
# def NewColumnUsername(df):
#     ele = df["Email"]
#     for i in range(0,len(ele)):
#         df["Username"] = df["Email"].apply(extract_username)
#     return df

# data = {
#     "Email":["adi@gmail.com","raj@gmail.com","singh@gmail.com","rahul@gmail.com","raushan@gmail.com","raj.sahul@gmail.com"]
# }

# df = pd.DataFrame(data)
# print(NewColumnUsername(df))

# import pandas as pd
# def Func(df):
#     filtered_df = df[(df['A'] > 5) & (df['B'] < 10)]
#     return filtered_df

# data = {
#     'A': [3, 8, 6, 2, 9],
#     'B': [5, 2, 9, 3, 1],
#     'C': [1, 7, 4, 5, 2]
# }

# df = pd.DataFrame(data)
# print(Func(df))


import pandas as pd
# def Func(df):
#     mean = df["Values"].mean()
#     median = df["Values"].median()
#     standard_deviation = df["Values"].std()
#     return {
#         "mean":mean,
#         "median":median,
#         "standard deviation":standard_deviation
#     }

# data = {
#     "Values":[10,20,30,40,50]
# }

# df = pd.DataFrame(data)
# print(Func(df))


# def calculate_moving_average(df):
#     df = df.sort_values('Date')
#     df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
#     return df

# data = {
#     'Date': pd.date_range(start='2021-01-01', periods=10, freq='D'),
#     'Sales': [200, 220, 210, 230, 250, 240, 260, 270, 280, 290]
# }

# df = pd.DataFrame(data)
# result_df = calculate_moving_average(df)
# print(result_df)





import pandas as pd

def add_weekday_column(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Weekday'] = df['Date'].dt.day_name()
    return df

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
}

df = pd.DataFrame(data)
result_df = add_weekday_column(df)
print(result_df)

    
        
