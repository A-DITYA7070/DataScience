1. sorting , counting , searching function in numpy.

2. we can sort the elements using np.sort(arr) function.
3. np.searchsort(arr,ele) :- it will tell that at which index the ele will go after sorting.
4. np.countnonzero(arr) :- it will tell how many non-zero data are there in array.
5. np.where(arr > 6) :- it will return the index of ele in the array where ele > 6 ( we can write any condition acc to our need)
6. if we want the data acc to condition we can use np.extract(arr > 6 , arr)
7. arr.byteswapping() it returns the arr after reperesenting it into bytes of the corresponding element.
8. arr.view() is shallow copy 
9. we have matlib library in numpy which does the same thing as numpy array but for matrices ex:- 
   import numpy.matlib as nm
   nm.zeros(5) it will generate (5*5) matrix with ele having value zero.

10. to do matrix multiplication we can use @ ex :- arr3 = arr2@arr1
11. to do dot product we can use np.dot(arr1,arr2).