
what is pandas ? 
    Pandas is a popular open-source Python library used for data manipulation and analysis. It provides easy-to-use data structures and functions that allow users to efficiently manipulate large datasets, perform data cleaning, transformation, and analysis tasks.

    The primary data structures in Pandas are Series and DataFrame.

    A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.).
    A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types. It is similar to a spreadsheet or SQL table.
    Pandas provides functionalities for:

    Reading and writing data from various file formats such as CSV, Excel, SQL databases, etc.
    Handling missing data.
    Filtering, sorting, and selecting data.
    Applying functions and transformations to data.
    Grouping and aggregating data.
    Merging and joining datasets.
    Visualization of data.
    Due to its simplicity and efficiency, Pandas is widely used in data science, machine learning, finance, and other domains where data manipulation and analysis are critical.

    It read only structured form of data.. (tabular format)


=> pandas thinks its first record as column name... 
=> head function in pandas..
   The head() function in Pandas is used to display the first few rows of a DataFrame. By default, it displays the first 5 rows, but you can specify the number of rows you want to display by passing an integer argument to the function.
   Here's an example of how you can use the head() function:
   ex :- df.head(3) it will display the first 3 rows 
=> by default the first record/row is treated as column name if we dont want this we can specify a parameter called none 
   ex :- df.head(3,none) 

   If you want to read the last lines of tables... 

=> pd.tail()
=> To be specific pd.tail(3)
   it will display the last three rows 


