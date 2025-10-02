def some(n):
    sum=0
    for i in range(1,n+1):
        sum +=i
    print(f"{n}->{sum}")
def greet():
    print("Hello World")
def add(a,b):
    print(a+b)

def  decorator(func):
    def wrapper(*args,**kwargs):
        print("HI")
        func(*args,**kwargs)
        print("Finish")
        print("___________________")
    return wrapper
my_decorator=decorator(some)
my_decorator(5)
my_decorator(11)

my_decorator_2=decorator(add)
my_decorator_2(10,111)

my_decorator_3=decorator(greet)
my_decorator_3()