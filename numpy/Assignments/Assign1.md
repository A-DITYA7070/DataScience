Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
    to print the data types of both the variables.
ans:- A Python list is a built-in data type in Python, while a NumPy array is an array object from the NumPy 
      library optimized for numerical operations.
      ex:- import numpy as np
           l = [1,2,4,5,6]
           arr = np.array(l)
           print(type(l))
           print(type(arr))
        
        output :- <class list>
                  <class numpy.ndarray>

Q2. Write a code to print the data type of each and every element of both the variables list_ and
    arra_list.
ans:- import numpy as np
      l = [1,2,34,54,56]
      arr = np.array(l)

      for ele in l:
        print(type(ele))
    
      for ele in arr:
        print(type(ele))

Q3. Considering the following changes in the variable, array_list:
    array_list = np.array(object = list_, dtype = int)
    Will there be any difference in the data type of the elements present in both the variables, list_ and
    arra_list? If so then print the data types of each and every element present in both the variables, list_
    and arra_list.

ans:- import numpy as np
      l = [1,2,34,5,6]
      arr = np.array(object=l,dtype=int)

      for ele in l:
        print(type(ele))

      for ele in arr:
        print(type(ele))
    
      output :- both will have different output because the list will output the datatype as int
                but the array constructed with numpy will output the datatype as numpy.int64
    
Q4. Write a code to find the following characteristics of variable, num_array:
    (i) shape
    (ii) size
ans:-  import numpy as np
       num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
       num_array = np.array(object = num_list)
       print(num_array.shape())
       print(num_array.size())

Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
    creation function.
    [Hint: The size of the array will be 9 and the shape will be (3,3).]
ans :- import numpy as np
       arr = np.zeros((3,3))
       print(arr)
    
Q6. Create an identity matrix of shape (5,5) using numpy functions?
    [Hint: An identity matrix is a matrix containing 1 diagonally and other elements will be 0.]
ans:- import numpy as np
      arr = np.eye((5,5))
      print(arr)