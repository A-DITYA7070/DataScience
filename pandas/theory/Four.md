1. To delete a column in dataframe we can use drop method 
   ex:- df.drop('PassengerId') but this will not delete if the axis is set to 0 hence to delete this we need to make axis=1
        df.drop('PassengerId',axis=1) This will delete the PassengerId temporarily.

2. To delete the column permanently we need to make inplace=True
   ex:- df.drop('PassengerId',axis=1,inplace=True) 

3. To delete any row we can use df.drop(0) :- it will delete the 0th row but not permanently
4. To delete permanently we can use df.drop(0,inplace=True)
5. To set any column as index we can use df.set_index("Name") function.
6. To make it permanent df.set_index("Name",inplace=True)
7. To reset the index as default we can use func :- df.reset_index()
8. To delete the rows having nan value we can use func:- df.dropna()
9. To delete the columns having nan value we can use func:- df.dropna(axis=1)
10. To delete permanently we can use df.dropna(axis=1,inplace=True)
11. To fill the value of nan we can use df.fillna("adi") :- means all the rows having nan value will be filled with "adi"
12. To fill the value of nan we can use df.fillna("adi",inplace=True)
13. To group the rows we can use func :- g = df.groupBy("Survived")
14. Apply function is similar to map function by using apply function we can manipulate the table.