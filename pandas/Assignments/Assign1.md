Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
ans:- import pandas as pd
      data = [4,8,15,16,23,42]
      series = pd.Series(data)
      print(series)

Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the variable print it.
ans :- import pandas as pd
       data = ['a','b','d','adi','raj','singh','rahul','raushan','rohit','kunal']
       series = pd.Series(data)
       print(series)
      
Q3. Create a pandas dataframe that contains following data and print it.
    Name     Age    Gender

    Alice    25     Female
    Bob      30     Male
    Claire   27     Female

ans :- import pandas as pd
       data = [
        ["Alice",25,"Female"],
        ["Bob",30,"Male],
        ["Claire",27,"Female"]
       ]
       df = pd.DataFrame(data,columns=["Name","Age","Gender"])
       print(df)

Q4.  What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
ans :   A Series is a one-dimensional array-like object.
        A DataFrame is a two-dimensional table-like structure.

        Structure:
        A Series has a single axis (index).
        A DataFrame has two axes (rows and columns).

        Use Cases:
        A Series is typically used for a single column of data.
        A DataFrame is used for datasets with multiple columns, resembling a table or spreadsheet.

        Ex1 :- data = ['a','b','c','d']
              series = df.Series(data)
              print(series)
              
              output :- 
              0 a
              1 b
              2 c
              3 d

        Ex2 :- data = {
            'a':["aditya","raj"],
            'b':["rohit","sharma"],
            'c':["virat","kohli"]
        }
        df = pd.DataFrame(data)
        print(df)

        output:- 
                a       b       c
        0     aditya   rohit   virat
        1     raj      sharma  kohli

Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
    you give an example of when you might use one of these functions?
ans:-       head() and tail()

            Purpose: Display the first or last few rows of the DataFrame.
            Example: Useful for quickly inspecting the data structure.

            df.head()  # Displays the first 5 rows
            df.tail(3) # Displays the last 3 rows
            info()

            Purpose: Provides a concise summary of the DataFrame.
            Example: Useful for checking the data types and non-null counts of each column.

            df.info()
            describe()

            Purpose: Generates descriptive statistics.
            Example: Useful for getting a quick statistical summary of the data.
            df.describe()
            loc and iloc

            Purpose: Access a group of rows and columns by labels or positions.
            Example: Useful for selecting specific rows and columns.
            df.loc[0:2, ['A', 'B']]  # Selects rows 0 to 2 and columns 'A' and 'B'
            df.iloc[0:2, 0:2]        # Selects the first two rows and first two columns by index
            drop()

            Purpose: Remove rows or columns.
            Example: Useful for deleting unnecessary data.
            df.drop('column_name', axis=1)  # Drops a column
            df.drop([0, 1], axis=0)         # Drops rows with index 0 and 1
            apply()

            Purpose: Apply a function along an axis of the DataFrame.
            Example: Useful for applying custom functions to each row or column.
            df['A'] = df['A'].apply(lambda x: x * 2)
            groupby()

            Purpose: Group data by one or more columns and apply a function to each group.
            Example: Useful for aggregating data.
            df.groupby('column_name').sum()
            merge()

            Purpose: Merge DataFrames.
            Example: Useful for combining data from different DataFrames.
            merged_df = pd.merge(df1, df2, on='key')
            pivot_table()

            Purpose: Create a spreadsheet-style pivot table as a DataFrame.
            Example: Useful for summarizing data.
            pivot = df.pivot_table(values='value', index='index', columns='columns', aggfunc='mean')
            fillna()

            Purpose: Fill missing values.
            Example: Useful for handling missing data.
            df.fillna(0)  # Replaces all NaNs with 0
 
 Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
 ans :- Both Series and DataFrame are mutable in nature , whereas Panel is depricated now and not used.

 Q7. Create a DataFrame using multiple Series. Explain with an example.
 ans :- import pandas as pd
        names = pd.Series(["adi","alice","bob"])
        ages = pd.Series([23,34,25])
        grades = pd.Series([9,8,9])

        data = {
            "name":names,
            "age":ages,
            "grade":grades
        }

        df = pd.DataFrame(data)
        print(df)