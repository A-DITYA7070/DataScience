
Python lang. can be used in Data industry because it has very good no of libraries..
It can be used in big data,data analytics,data science,gaming industry,gui apps,web application,robotics,automation,numeric & scientific calculation,db interaction,web scrapping.. 


It is slower than cpp but its computation can be optimised using various libraries.. 


                                              VARIABLES :- 

In Python, a variable is a symbolic name that references or holds a value. Unlike some other programming languages, Python is dynamically typed, meaning you don't need to declare the type of a variable when you create one

    In Python, variables can generally be categorized into the following types based on their scope and usage:

  1. Local Variables: These are variables defined within a function. They have local scope, meaning they can only be accessed within    the function in which they are defined.

    def my_function():
        x = 10  # Local variable
        print(x)
    
    my_function()  # Output: 10
  2. Global Variables: These are variables defined outside of any function. They have global scope, meaning they can be accessed from any part of the code, including inside functions.

    y = 20  # Global variable

    def my_function():
        print(y)  # Accessing global variable inside function

    my_function()  # Output: 20
    print(y)  # Output: 20
  3. Instance Variables: These are variables defined within a class and are bound to an instance of the class. Each instance of the class can have different values for these variables.
                            
    class MyClass:
        def __init__(self, value):
            self.value = value  # Instance variable

    obj1 = MyClass(5)
    obj2 = MyClass(10)

    print(obj1.value)  # Output: 5
    print(obj2.value)  # Output: 10
  4. Class Variables (Static Variables): These are variables that are shared among all instances of a class. They are defined within the class but outside of any method.

    class MyClass:
        class_variable = 100  # Class variable

        def __init__(self, value):
            self.value = value

    obj1 = MyClass(5)
    obj2 = MyClass(10)

    print(obj1.class_variable)  # Output: 100
    print(obj2.class_variable)  # Output: 100
    These are the primary types of variables in Python. Understanding the differences between them is crucial for writing organized and maintainable code.


NOTE :- we can check the type of data by using type() func.. 

      
                                                            Mutable and immutable object..

     -> forward direction indexing..                                                       
     012345
s = "aditya"
    -6-5-4-3-2-1
    <-  Backward direction indexing..

    same can be assigned in list also... 

string is immutable object but list is mutable object at particular index.

