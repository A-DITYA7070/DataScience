
what is pandas ? 
    Pandas is a popular open-source Python library used for data manipulation and analysis. It provides easy-to-use data structures and functions that allow users to efficiently manipulate large datasets, perform data cleaning, transformation, and analysis tasks.

   NOTE :- Pandas only read structured datasets it does not read unstructured data sets.

   => The primary data structures in Pandas are Series and DataFrame.

    A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.).
    A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types. It is similar to a spreadsheet or SQL table.

   => Pandas provides functionalities for:

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


=> To know the columns name of the data we can use df.columns
=> If we want to convert the output in list we can use list(df.columns)
=> To select the specific single column name from the dataframe we can use df["column_name"]
=> Type of single column is series which is euqivalent to list.
=> In series we can see the default indexes which is not visible in list.
=> To select multiple columns we can do that like this :- df[["column_name1","column_name2","column_name3]]
=> To know the data types of each columns we can use df.dtypes  => print(df.dtypes)

=> READING EXCEL FILES ::-
1) To read a excel file we can use pd.read_excel("data.xlsx")

=> If some data is on some link we can use df.read_csv("https://example.com/master.csv")

=> To read html file we can use file_html = df.read_html("https://example.com/home.html")
=> This will return us a list.
=> To extract tables from this list we can use li = file_html[0] for first list 


=> To store data in some files we can use li.to_csv("players_name.csv,index=False")