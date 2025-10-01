#syntax
"""lambda(parameter):returning_value"""
def my_square(n):
    return n**2
print(my_square(3))
def  my_sum(a,b):
    return a+b
print(my_sum(2,3))

# using lambda_function 
my_lambda_square_function=lambda n: n**3 # n= parameter and n**3 = returning value
print(my_lambda_square_function(5))

def get_value(any_list,key):
    for item in any_list:
        print(item[key])
list=[
    ("Almas",23),
    ("Tanim",24),
    ("Sakib",22)
]
get_value(any_list=list,key=0)
print("_____________________________")
list=[
    ("Almas",23),
    ("Tanim",24),
    ("Sakib",22)
]
# sorted based on age 
ls=sorted(list, key=lambda list: list[1])
print(ls)

ls=sorted(list,key=lambda list :list[0],reverse=True)
print(ls)

ls=sorted(list,key=lambda list :list[0],reverse=False)
print(ls)