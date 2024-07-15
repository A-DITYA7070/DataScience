Q1. Write a code to print the data present in the second row of the dataframe, df?
ans :- import pandas as pd
       print(df[1:2])

Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?
ans:- loc :- (location based indexing) is used to access data in dataFrame,
             It selects rows and columns by labels (names) or boolean array.
             eg:- df.loc[row_label,column_label]
                  df.loc['row_name','column_name']
      iloc :- (integer based indexing) :- is used to access data in dataFrame,
              It selects rows and columns by their integer positions.
              eg:- df.iloc[row_index,column_index]
                   df.iloc[0,0]

Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
    then find the output for both new_df.loc[2] and new_df.iloc[2].
ans:- import pandas as pd
      reindex = [3,0,1,2]
      new_df = df.reindex(reindex)
      print(new_df.loc[2])
      print(new_df.iloc[2])
      
      Ex:- new_df.loc[2] retrieve course_name Big Data and duration 6.
           new_df.iloc[2] retrieve course_name Machine Learning and duration 3.
           Reindexing: The reindex method is used to change the order of the rows according to the given list [3, 0, 1, 2].
                        Accessing rows:
                        .loc[2]: Accesses the row with the label 2.
                        .iloc[2]: Accesses the row at the integer position 2.

Q4. Write a code to find the following statistical measurements for the above dataframe df1:
    (i) mean of each and every column present in the dataframe.
    (ii) standard deviation of column, ‘column_2’
ans:- i)    import pandas as pd
            import numpy as np
            columns = ['column_1','column_2','column_3','column_4','column_5','column_6']
            indeces = [1,2,3,4,5,6]
            df = pd.dataFrame(np.rand(6,6),columns=columns,index=indeces)
            df['mean'] = df.mean(axis=1)
            print(df)
      ii)   import pandas as pd
            sd = df['column_2].std()
            print(sd)

Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
    mean of column, column_2.
    If you are getting errors in executing it then explain why.
ans :- It will give typeError because we are trying to calculate standard deviation of non-numeric value at row 2 and column_2.
       we can update the value by using following code...
       a) df.loc[2,'column_2'] = "aditya"
       b) df.iloc[1,1] = "aditya"
       c) df.at[2,'column_2'] = "aditya"

Q6. What do you understand about the windows function in pandas and list the types of windows
    functions?
ans :-  The window functions in pandas provide a way to perform operations over a sliding window of data, enabling complex and efficient     
        and various statistical computations.

        eg:- Rolling Window: This function computes statistics over a sliding window of a specified size.
            Common Methods: rolling.mean(), rolling.sum(), rolling.min(), rolling.max(), rolling.std(), rolling.var(), rolling.median(), etc.
            Example:
            import pandas as pd
            data = {'A': [1, 2, 3, 4, 5]}
            df = pd.DataFrame(data)
            df['rolling_mean'] = df['A'].rolling(window=3).mean()
            print(df)
            Expanding Window: This function computes statistics over an expanding window, which starts from the beginning of the series and grows as it moves forward.
            Common Methods: expanding.mean(), expanding.sum(), expanding.min(), expanding.max(), expanding.std(), expanding.var(), expanding.median(), etc.
            Example:
            df['expanding_mean'] = df['A'].expanding(min_periods=1).mean()
            print(df)
            Exponentially Weighted Window: This function computes statistics using weights that decrease exponentially.
            Common Methods: ewm.mean(), ewm.sum(), ewm.std(), ewm.var(), ewm.median(), etc.
            Example:
            df['ewm_mean'] = df['A'].ewm(span=3).mean()
            print(df)


Q7.      