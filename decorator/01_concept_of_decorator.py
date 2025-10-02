"""A decorator is a special function in Python that takes another function 
    as input and adds some extra functionality
    to it without changing the original function’s code.
"""

def decarator(func):
    def wrapper():
        print("Hi")  #Before calling the function
        func()        # Call the original function
        print("finish")    # After calling the function
    return wrapper    

# decrator with no parameter 

def some():
    print("I am some function ")
def decorator(func):
    def wrapper():
        print("HI")
        func()
        print("Finish")
    return wrapper 
my_decorator=decorator(some)  # Pass 'some' to decorator
my_decorator()   # Call the wrapper