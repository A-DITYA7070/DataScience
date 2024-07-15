Q1. List any five functions of the pandas library with execution ?
ans:- Five function of pandas library are :-
      a. read_csv(): This function is used to read a CSV file and convert it into a DataFrame.
      b. head(): This function returns the first n rows of a DataFrame. 
      c. describe(): This function generates descriptive statistics of a DataFrame.
      d. groupby(): This function is used to group the DataFrame using a column or series of columns.
      e. merge(): This function merges two DataFrames based on a key or keys.

Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
    DataFrame with a new index that starts from 1 and increments by 2 for each row ?
ans :-  import pandas as pd
        # Function to reindex the dataframe.
        def reindex_dataframe(df):
            new_index = range(1, 2 * len(df) + 1, 2)
            df = df.set_index(pd.Index(new_index))
            return df

        data = {
            'A':[1,2,3],
            'B':[4,5,6],
            'C':[7,8,9]
        }
        df = pd.DataFrame(data)
        # Printing the dataframe before applying reindexing
        print(df)
        # Printing the datafrane after applying reindexing.
        reindex = reindex_dataframe(df)
        print(reindex)

Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
    iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
    function should print the sum to the console.
ans:-   import pandas as pd
        # Function to calculate the sum of first 3 elements of Column Values of DataFrame df
        def SumOfEle(df):
            val = df["Values"]
            sum = val[0] + val[1] + val[2]
            return sum

        data = {
            "Values":[23,12,50,48,50,30]
        }

        df = pd.DataFrame(data)
        print(SumOfEle(df))

Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
    'Word_Count' that contains the number of words in each row of the 'Text' column.
ans :-  import pandas as pd
        # Function to count word count in a string
        def wordCount(str):
            words = str.split()
            return len(words)
        # Function to create new Column word_count and add word Counts of Text
        def NewColumnWordCount(df):
            ele = df["Text"]
            for i in range(0,len(ele)):
                df["word_count"] = df["Text"].apply(wordCount)
            return df

        data = {
            "Text":["I am a good boy","you are bad","very good","bad boy"]
        }

        df = pd.DataFrame(data)
        print(NewColumnWordCount(df))

Q5 :- How are DataFrame.size() and DataFrame.shape() different?
ans :-  DataFrame.size and DataFrame.shape are attributes of a Pandas DataFrame that provide information about the size and shape of the
        DataFrame but they differ in what specific information they provide.
       
        DataFrame.shape
        Description: DataFrame.shape returns a tuple representing the dimensionality of the DataFrame.
        Output: The output is a tuple of the form (number of rows, number of columns).
        Example:
        python
        Copy code
        import pandas as pd

        data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        }
        df = pd.DataFrame(data)
        print(df.shape)
        Output:
        (3, 3)
        This indicates the DataFrame has 3 rows and 3 columns.
        DataFrame.size
        Description: DataFrame.size returns the number of elements in the DataFrame.
        Output: The output is a single integer which is the total number of elements in the DataFrame (i.e., number of rows * number of columns).
        Example:
        import pandas as pd

        data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        }
        df = pd.DataFrame(data)
        print(df.size)
        Output:
        9
        This indicates the DataFrame has 9 elements in total (3 rows * 3 columns).


Q6. Which function of pandas do we use to read an excel file?
ans:- pd.read_excel("file_name.xlxs")

Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
    addresses in the format 'username@domain.com'. Write a Python function that creates a new column
    'Username' in df that contains only the username part of each email address.
ans :- 
        import pandas as pd
        # Function to extract part of email before '@'
        def extract_username(email):
            if "@" in email:
                return email.split('@')[0]
            else:
                return None
        # Function to create new column Username and assign usernames
        def NewColumnUsername(df):
            ele = df["Email"]
            for i in range(0,len(ele)):
                df["Username"] = df["Email"].apply(extract_username)
            return df

        data = {
            "Email":["adi@gmail.com","raj@gmail.com","singh@gmail.com","rahul@gmail.com","raushan@gmail.com"]
        }

        df = pd.DataFrame(data)
        print(NewColumnUsername(df))

Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
    all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
    function should return a new DataFrame that contains only the selected rows.
ans:- 
        import pandas as pd
        def Func(df):
            filtered_df = df[(df['A'] > 5) & (df['B'] < 10)]
            return filtered_df

        data = {
            'A': [3, 8, 6, 2, 9],
            'B': [5, 2, 9, 3, 1],
            'C': [1, 7, 4, 5, 2]
        }

        df = pd.DataFrame(data)
        print(Func(df))

Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
    median, and standard deviation of the values in the 'Values' column.
ans :- 
        import pandas as pd
        def Func(df):
            mean = df["Values"].mean()
            median = df["Values"].median()
            standard_deviation = df["Values"].std()
            return {
                "mean":mean,
                "median":median,
                "standard deviation":standard_deviation
            }

        data = {
            "Values":[10,20,30,40,50]
        }

        df = pd.DataFrame(data)
        print(Func(df))

Q10.    Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
        create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
        for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
        should include the current day.
ans:- 
        def calculate_moving_average(df):
            df = df.sort_values('Date')
            df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
            return df

        data = {
            'Date': pd.date_range(start='2021-01-01', periods=10, freq='D'),
            'Sales': [200, 220, 210, 230, 250, 240, 260, 270, 280, 290]
        }

        df = pd.DataFrame(data)
        result_df = calculate_moving_average(df)
        print(result_df)

Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
    column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
    Monday, Tuesday) corresponding to each date in the 'Date' column.
    For example, if df contains the following values:
    Date
    0 2023-01-01
    1 2023-01-02
    2 2023-01-03
    3 2023-01-04
    4 2023-01-05
    Your function should create the following DataFrame:

    Date Weekday
    0 2023-01-01 Sunday
    1 2023-01-02 Monday
    2 2023-01-03 Tuesday
    3 2023-01-04 Wednesday
    4 2023-01-05 Thursday
    The function should return the modified DataFrame.

ans:- 
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

Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
     function to select all rows where the date is between '2023-01-01' and '2023-01-31'.
ans:-
    import pandas as pd

    def filter_dates(df):
        df['Date'] = pd.to_datetime(df['Date'])
        start_date = '2023-01-01'
        end_date = '2023-01-31'
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        return filtered_df

    data = {
        'Date': ['2023-01-01', '2023-01-15', '2023-01-31', '2023-02-01', '2022-12-31'],
        'Value': [10, 20, 30, 40, 50]
    }

    df = pd.DataFrame(data)
    result_df = filter_dates(df)
    print(result_df)

Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
    be imported? 
ans:- To use the basic functions of pandas the basic the first and foremost basic library that needs to be imported 
      id pandas ex:- import pandas as pd

