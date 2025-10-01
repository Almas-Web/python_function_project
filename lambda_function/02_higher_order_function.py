def some():
    print("Hello")
some()
# function assign to another variable 
another_variable=some 
# function call as a variable 
another_variable()

# function as an argument 
def square(number):
    return number**2
def cube (number):
    return number**3
def quard (number):
    return number**4
def helper(function_name,number): # here function_name ,number is function as an argument 
    return(function_name(number))
result1=helper(function_name=cube,number=87)
result2=helper(function_name=quard,number=9999)
print(result1)
print(result2)