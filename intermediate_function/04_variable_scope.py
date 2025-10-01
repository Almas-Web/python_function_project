# global scope and function scope 
user_name="almas" # global scope 

def greet(user_name):  # function scope 
    print(user_name)
greet(user_name="sakib")
print(user_name)
print("____________________")

user_name="abc"   # global scope 
def greet():   # function scope
    print(user_name)
greet()
print("______________")

user_name="eeeefffg"
def greet(user_name):
    print(user_name)
greet(user_name="def")
print(f"out of function", user_name)
print("_____________________")

user_name="tanim"
def greet(user_name):
    global x
    x=10
    y=7
    print(user_name)
greet(user_name="sakib")
print(f"out of function",user_name)
print(x)
#print(y) # error 
print("___________________")

user_name="tanim"
def greet(user_name):
    global x,y
    x=10
    y=7
    print(user_name)
greet(user_name="sakib")
print(f"out of function",user_name)
print(x)
print(y)