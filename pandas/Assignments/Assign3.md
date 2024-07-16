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


Q7.      Write a code to print only the current month and year at the time of answering this question.
ans:-    import pandas as pd
         date_time = pd.Timestamp.now()
         print(date_time)

Q8.     Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
        calculates the difference between them in days, hours, and minutes using Pandas time delta. The
        program should prompt the user to enter the dates and display the result.
ans:- 
        import pandas as pd
        
        def get_input():
            str = input(promt)
            return pd.Timestamp(str)
        
        def main():
            start_date = get_input("Enter the start date (yyyy-mm-dd) format")
            end_date = get_input("Enter the last date (yyyy-mm-dd) format")
            time_delta = end_date - start_date

            days = time_delta.days()
            hours, remainder = divmod(time_delta.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
        
        if __name__ == "__main__":
            main()

Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified
    column to a categorical data type. The program should prompt the user to enter the file path, column
    name, and category order, and then display the sorted data.
ans:- 
        import pandas as pd
 
        def main():
            file_path = input("Enter the CSV file path: ")
            column_name = input("Enter the column name to convert to categorical: ")
            category_order = input("Enter the category order (comma-separated): ").split(',')

            df = pd.read_csv(file_path)

            df[column_name] = pd.Categorical(df[column_name], categories=category_order, ordered=True)

            df_sorted = df.sort_values(by=column_name)

            print(df_sorted)

        if __name__ == "__main__":
            main()

Q10. Write a Python program that reads a CSV file containing sales data for different products and
    visualizes the data using a stacked bar chart to show the sales of each product category over time. The
    program should prompt the user to enter the file path and display the chart.
ans:-   import pandas as pd
        import matplotlib.pyplot as plt

        def main():
            file_path = input("Enter the CSV file path: ")

            df = pd.read_csv(file_path)

            required_columns = ['Date', 'ProductCategory', 'Sales']
            if not all(column in df.columns for column in required_columns):
                print(f"The CSV file must contain the following columns: {', '.join(required_columns)}")
                return

            df['Date'] = pd.to_datetime(df['Date'])

            sales_data = df.groupby(['Date', 'ProductCategory'])['Sales'].sum().unstack(fill_value=0)

            sales_data.plot(kind='bar', stacked=True, figsize=(10, 7))

            plt.xlabel('Date')
            plt.ylabel('Sales')
            plt.title('Sales of Each Product Category Over Time')
            plt.legend(title='Product Category')
            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.show()

        if __name__ == "__main__":
            main()         


Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
    a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
    displays the results in a table.
ans:-   import pandas as pd
        def main():
            file_path = input("Enter the file path of the CSV file containing the student data: ")

            df = pd.read_csv(file_path)

            required_columns = ['Student ID', 'Test Score']
            if not all(column in df.columns for column in required_columns):
                print(f"The CSV file must contain the following columns: {', '.join(required_columns)}")
                return

            mean_score = df['Test Score'].mean()
            median_score = df['Test Score'].median()
            mode_score = df['Test Score'].mode()

            results = [
                ['Mean', f"{mean_score:.1f}"],
                ['Median', f"{median_score:.1f}"],
                ['Mode', ', '.join(map(str, mode_score))]
            ]

            print(results)

        if __name__ == "__main__":
            main()