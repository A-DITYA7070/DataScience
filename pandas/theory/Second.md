<!-- pandas functions -->

1. describe :- It gives the description about the whole dataset, with count,mean,std deviation,
min,25th percentile,50th percentile,75th percentile and max.

2. df.dtypes :- This method tells about the data type of the columns.

3. We can check which column of the table is object by df.types == "object" or any other data types.

4. We can also get the index of the column having types
print(df.dtypes[df.dtypes == 'object'].index)

5. We can even describe the columns also ..
print(df[df.dtypes[df.dtypes == 'object']].describe())

6. We can define our range and length to get the data ex :- print(df[['Ticket','Cabin']][4:11:2]) :- It means retrieve data from 4 to 11 with difference of 2.

7. We can create a new column in the table itself.
Ex :- df["new_col"] = df["PassengerId"] + df["Pclass"]

8. We can get the categories of the columns in the table / file.
pd.Categorical(df['Pclass'])
pd.Categorical(df['Survived'])

9. We can retrive unique data from the datasets ex :- print(df["Cabin"].unique())

10. We can apply conditions while retrieving. 
Ex :- print(len(df[df['Age'] > 18]))

11. Getting People Who have age > 18 eg:- print(df[df['Age'] > 18])

12. Retriving People who have 0 fare e.g print(df[df['Fare'] == 0])

13. Retreiving only male print(df[df["Sex"] == "Male"])

14. We can even chain the query ex :- query1 = df[(df['Sex'] == 'female') & (df['Fare'] > 32)] :- This will retrieve all the row where sex is female and fare is greater than 32.

15. We can apply or operator as well. ex :- query2 = df[(df['Sex'] == 'female') | (df['Fare'] > 32)]

16. query3 = df[df['Fare'] == max(df['Fare'])]['Name']

17. we can retreive all the data by skipping certain time let's retrieve data by skipping 2 times eg :- df[0::2] this will retrieve all the data but after skipping 2 times.

18. The df.iloc[0:2, [0, 1, 2]] command is used to select a subset of rows and columns from a Pandas DataFrame df. Here’s a breakdown of what this command does:
df refers to the DataFrame from which you are selecting data.
iloc is an index-based selection method provided by Pandas.
0:2: This specifies the range of rows to select. It uses Python's slice notation.

0:2 means "select from the 0th row up to, but not including, the 2nd row."
This will select the first two rows (index 0 and 1).
[0, 1, 2]: This specifies the list of columns to select.

0, 1, 2 refers to the columns by their positional indices.
This will select the first three columns (index 0, 1, and 2).
Example
Assume you have the following DataFrame df:

import pandas as pd

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
}
df = pd.DataFrame(data)
The DataFrame looks like this:


   A  B   C   D
0  1  5   9  13
1  2  6  10  14
2  3  7  11  15
3  4  8  12  16
Executing df.iloc[0:2, [0, 1, 2]] will give:


   A  B   C
0  1  5   9
1  2  6  10
This selects the first two rows and the first three columns of the DataFrame.

In summary, df.iloc[0:2, [0, 1, 2]] extracts a sub-DataFrame that contains the first two rows and the first three columns of the original DataFrame df.

19. The df.loc[0:2, ['PassengerId', 'Survived', 'Pclass']] command is used to select a subset of rows and columns from a Pandas DataFrame df using labels. Here's a breakdown of what this command does:

df refers to the DataFrame from which you are selecting data.
loc is a label-based selection method provided by Pandas.
Breakdown of loc[0:2, ['PassengerId', 'Survived', 'Pclass']]
0:2: This specifies the range of rows to select by their labels.

In loc, 0:2 means "select from the row with label 0 up to and including the row with label 2."
This will select rows with labels 0, 1, and 2.
['PassengerId', 'Survived', 'Pclass']: This specifies the list of columns to select by their names.

This will select the columns named 'PassengerId', 'Survived', and 'Pclass'.
Example
Assume you have the following DataFrame df:

import pandas as pd

data = {
    'PassengerId': [1, 2, 3, 4],
    'Survived': [0, 1, 1, 0],
    'Pclass': [3, 1, 3, 1],
    'Name': ['Allen', 'Braund', 'Cummings', 'Davies']
}
df = pd.DataFrame(data)
The DataFrame looks like this:

   PassengerId  Survived  Pclass     Name
0            1         0       3    Allen
1            2         1       1   Braund
2            3         1       3 Cummings
3            4         0       1   Davies
Executing df.loc[0:2, ['PassengerId', 'Survived', 'Pclass']] will give:

   PassengerId  Survived  Pclass
0            1         0       3
1            2         1       1
2            3         1       3
This selects rows with labels 0, 1, and 2, and the columns 'PassengerId', 'Survived', and 'Pclass' of the DataFrame.

In summary, df.loc[0:2, ['PassengerId', 'Survived', 'Pclass']] extracts a sub-DataFrame that contains the specified rows (by label) and the specified columns (by name) from the original DataFrame df.


