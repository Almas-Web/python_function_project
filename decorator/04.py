# The easiest way of using decorator

def decorator(func):
    def wrapper(*args,**kwargs):
        print("HI")
        func(*args,**kwargs)
        print("Finish")
        print("_______________")
    return wrapper 
@decorator
def some(n):
    sum=0 
    for i in range(1,n+1):
        sum+=i
    print(f"{n}->{sum}")
@decorator
def greet():
    print("Hello World")
    
"""
def add(a,b,*args):
    print(a+b+args)  can't add integer+ tuple 
    """
@decorator
def add(a, b, *args):
    total = a + b + sum(args)  # sum works on tuple
    print(total)

# call the function
some(5)
some(11)
greet()
add(1,12)
add(1,2,3,55,66,90)
