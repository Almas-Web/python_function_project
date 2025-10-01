"""*args allows a function to accept a variable number of positional arguments.

The * collects all extra positional arguments into a tuple."""
# syntax
def my_function(*args):
    print(args)

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice")
greet("Bob", "Charlie", "David")
print("__________________")
def add_numbers(a, b, *args):
    total = a + b
    for num in args:
        total += num
    return total

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3, 4, 5))
print("__________________")

def my_sum(*args):
    print(args)
my_sum(3,5)
my_sum(1,2,3)
my_sum(1,2,3,4,5)
print("_____________")

def my_sum(*args):
    sum=0
    for digit in args:
        sum=sum+digit
    return sum
print(my_sum(1,2,3,4))
print(my_sum(1,2,3,4,5,6))
print(my_sum(1,2,3,4,5,6,7,8))

print("___________")

def my_sum(*args):
    total = 0
    for digit in args:
        if isinstance(digit, (int, float)):  # Only add numbers
            total += digit
        else:
            print(f"Skipping non-numeric value: {digit}")
    return total

print(my_sum(1, 2, 3, 4, "a",5,6))
print("_______________")

def greet(user_name,is_loggedin=None):
    if is_loggedin:
        print(f"Hello {user_name}")
    else:
        print("please loggin")
greet(user_name="Almas",is_loggedin=True)
greet(user_name="sakib")
# if parameter is increasing the code will be showing error 
