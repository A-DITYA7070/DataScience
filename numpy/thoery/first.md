1.  NumPy is a fundamental package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. NumPy is essential for tasks involving numerical data and is widely used in scientific computing, data analysis, machine learning, and more. Its array object, numpy.ndarray, is a powerful structure that allows for efficient computation on large datasets.

2. Type of array in numpy is ndarray means n-dimensional array.
3. we can create array using numpy ex:- l = np.array([1,2,3]) -> 1-d array l2 = np.array[[1,2],[3,4],[5,6]] -> 2-d array
4. 1-d is represented in 1-dimensional means only in x-axis.
5. 2-d is represented in 2-dimensional means in x-axis and y-axis.
6. 3-d is represented max to max in numpy.
7. asanyarray can be also used to create array using numpy.
8. np.asarray can be also used to create array using numpy.
9. we can create matrix using np.matrix([1,2,3]) :- by default matrix is 2-d.
10. if matrix is passed into np.asarray() function it will not convert it back into array because matrix is subset of array.
11. The np array points to same array if two arrays are equalized. (means it follows shallow copy).
12. we can also copy the array using np.copy() function. (and it follows deep copy).
13. np.formfunction(lambda i,j : i==j,(3,3)) .formfunction is used to generate matrix it takes a function as an argument,
    and generates matrix based on the condition in the function.
14. we can create array from np.formiter() function as well.
    ex :-   iterable = (i*i for i in range(0,5))
            arr = np.fromiter(iterable,int)
            print(arr)
15. np.formstring('adi raj as aditya',sep=' ') :- it is a function that takes string as function parameter and sep as delimeter
    we can give our delimeter and this function will convert it into array.

16. To know about the dimension of the array we can use function ndim ex.  ar.ndim will give the dimension of the array.
17. ar.size tells how many elements are there in the array.
18. ar.shape will tell what is the number of row and columns in the matrix.
19. ar.dtype will tell the datatype of the array.
20. ar.itemsize will tell the size of the array.
21. we can create array from the given range ex:- arr = np.arange(1,5)
    => we can also set the jump value ex:- let we want to skip by 2 we can give the jump as 2 arr = np.arange(1,10,2)
    => np.arange(0.2,3.5) can also take floating number as range. which was not possible in normal list.
    => we can convert array to list ex:- list(np.arange(3,10))
22.  np.linspace(start_point,end_point,num_of_data_to_produce) :- it takes 3 values start_point end_point and number_of_data_to_produce.
     ex :- ar = np.linspace(1,5,10) :- it will produce the certain number of data between the given range.

23. np.zeros(num_of_zeroes_to_produce) :- it takes value as argument and produce that number of zeros as array.
    we can also specify dimensions eg. np.zeros((3,4)) it will create matrix of size (3,4) and assign value zero to them.
    it can also create 3-d array ex:- np.zeros((3,4,2)) => means we have two (3*4) matrices.
    we can even create further dimensions as well ex:- np.zeros((3,4,2,3))

24. np.ones((2,3,4)) :- it is same as np.zeroes() but it assigns the value 1.
    => we can multiply the values of np.ones() ex:- ar = np.ones((2,3)) 
                                                    ar*4 will assign value 4 in place of 1.

25. np.empty() it will create empty array of the dimensions we specify.
26. np.eye(4) it will create identity matrix of the dimensions we specify. (it takes only 1-d values).
27. np.logspace(start_range,end_range,no_of_data) :- it will give no_of_data between start_range and end_range and it will give value after
    calculating their log.
    by default the base is 10 we can also specify the base ex:- ar = np.logspace(2,5,10,base=2)

28. np.random.randn(3,5) :- it will generate random value when mean=0 and s.d=1 i.e standard normal dist. and assign it in the matrix of 3*5 
29. np.random.rand(3,4) :- it will generate random value between the given range.
30. np.random.randint(3,4) :- it will generate random value in integer only.

31. np.reshape(6,2) :- it will reshape the existing data into the given range.

32. we can perform matrix addition,substraction and multiplication as well.

33. we can directly calculate sqrt,exp,log etc on array ex:- ar = np.sqrt([2,3,5]) np.log10([2,3,4])
