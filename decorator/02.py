# decorator with parameter

def some(n):
    sum=0
    for i in range (1,n+1):
        sum +=i
    return sum 
def decorator (func):
    def wrapper(n):
        print("Hi")
        func(n)
        print("finish")
    return wrapper
my_decorator=decorator(some)
my_decorator(10)
my_decorator(5)
my_decorator(20)
print("_______________________________")

def some(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def decorator(func):
    def wrapper(n):
        print("Hi")
        result = func(n)      
        print(result)         # return value 
        print("Finish")
    return wrapper

my_decorator = decorator(some)

my_decorator(10)
my_decorator(5)
my_decorator(20)

print("____________________")

def some(n):
    sum=0
    for i in range (1,n+1):
        sum +=i
    print(f"{n}->{sum}")
def decorator (func):
    def wrapper(n):
        print("Hi")
        func(n)
        print("finish")
    return wrapper
my_decorator=decorator(some)
my_decorator(10)
my_decorator(5)
my_decorator(20)
