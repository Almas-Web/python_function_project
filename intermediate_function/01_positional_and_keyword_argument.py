def some(a,b,c):
    print(a,b,c)
#positional argument # not necessary to main serial 
some(1,2,3)
#keyword argument
some(a=1,b=2,c=3)

#positional ,keyword 
some(1,b=2,c=5)
some(1,2,c=5)
some(1,c=6,b=2)
#some(a=1,b=2,3) # error because always first positional argument 

# function increasing when parameters are also increasing 
#approach-1 
def my_sum(a,b):
    return a+b 
print(my_sum(1,2))
print(my_sum(a=1,b=1))

def my_sum(a,b,c):
    return a+b+c
print(my_sum(2,3,4))
print(my_sum(a=1,b=3,c=5))

#approach -2 
def my_sum(a,b,c=None,d=None):
    return a+b+c+d
#print(my_sum(1,2))   unsupported int +Nonetype 

def my_sum(a,b,c=0,d=0):
    return a+b+c+d
print(my_sum(1,3)) # but will be continued infinite 
