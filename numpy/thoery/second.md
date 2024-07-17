1. we can tranpose the matrix using arr.T function.
2. we can flatten the array into 1-d using arr.flatten() function.
3. we can also expand the dimensions of the array ex :- arr = np.array([1,2,3,4,5])
   here the dimension of array is 1.
   we can expand the dimension usingn arr2 = np.expand_dims(arr1,axis=1) axis = 1 means accross column, axis=0 means across row.
4. we can also sqeeze the array from 2-d to 1-d using np.squezee(arr) function. (if single element is avaible)
5. we can repeat the elements of array to a given number of times using np.repeat(arr,3) function.
6. we can rotate the array using np.roll() funciton ex :- arr2 = np.roll(arr,2) by 2 position.
7. r2 = np.diag(arr) it will put the elements of arr in the diagonal.
8. we can perform binary operation on arrays using numpy. (element wise)
   ex:- arr1 = np.random.randint(1,10,(2,3))
        arr2 = np.random.randint(1,10,(2,3))
        add = arr1+arr2
        sub = arr1-arr2
        mult = arr1*arr2 (it's not matrix multiplication)
        div = arr1/arr2
        mod = arr1%arr2
        and = arr1 & arr2
        or = arr1 | arr2
        xor = arr1 ^ arr2
        not = ~arr1
        boolean = arr1 > arr2

9. we can create array of string. arr = np.array(["adi","raj"])
10. we can convert it to upper case or lower case ar2 = np.char.upper(arr)
11. we can capitalize it as well ar2 = np.char.capitalize(arr)
12. mathematical function of numpy.
    1. ar1 = np.sin(arr) :- it will create the sin value of the elements of the array.
    2. similarly every mathematical operation can be performed.

