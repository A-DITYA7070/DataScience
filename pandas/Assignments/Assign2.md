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
