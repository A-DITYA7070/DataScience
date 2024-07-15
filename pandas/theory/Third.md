1. Selecting data from dataframe df["Name"] this is a series 
2. We can select chunk of data from this series as well ex:- s = df["Name"][0:10] this means 10 rows will be selected.
3. Named indexes :- we can name the indexes as our need
                    for that we need to create a list of same length as series and give the name as our need
                    ex:- s = df["Name"][0:10]
                         l = ['a','b','c','d','e','f','g','h','i','j']
                         l1 = list(s)
                         s1 = pd.Series(s,index=l1)

4. Even if we give our own indexes still series remembers the default index means if we s1[0] we will get the same data as s[0]
   means s[0] = s1[0] = s1['a']
5. Append() :- it is used to append two series let we have series s1 and series s2 then we can use append function to append both series
               ex :- s3 = s1.append(s2)