# a function returning a function 
def outer():
    def inner():
        print("Hello Almas")
    return inner
outer_part=outer()
outer_part()
outer()()
print("___________________________")

def outer():
    def inner():
        print("Hello")
    return 100
outer_part=outer()
val=outer_part
print(val)
print("___________________")

def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum 
print("Calling the function")
sum(n=5)
print("function called finished")
print("Calling the function")
sum(n=10)
print("function called finished")