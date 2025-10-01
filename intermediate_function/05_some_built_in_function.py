ls=[1,2,3,55,7,100,1200,300]
# sorting a list /ascending 
print(ls)
print(sorted(ls))
print("_______________")
ls=[2,1,5,3,4,7,6,8,9,11,15,12,17,13]

print(reversed(ls)) # <list_reverseiterator object at 0x00000123456789>

ite=reversed(ls)
rev_ls=list(ite)
print(rev_ls)

# direct 
print(list(reversed(ls)))
print("___________________")

# sort a list (descending order)
ls=[11111,9999,11,22,44,311,111,211,4,55]
#way-1
print(list(reversed(ls))) # just reverse 
print(list(reversed(sorted(ls)))) # reverse with descending order 
print("__________________")

#way-2
ls=[11111,9999,11,22,44,311,111,211,4,55]
new_ls=sorted(ls,reverse=True)
print(new_ls)
print("______________________")

ls=[
    ("Almas",23),
    ("Tanim",24),
    ("Sakib",22)

]

print(sorted(ls)) # nothin to change 
# sort based on age (sort key-1)
ls=[
    ("Almas",23),
    ("Tanim",24),
    ("Sakib",22)

]
sort_key=1
for item in ls:
    print(item[sort_key])
print("_______________________________")

def get_sort_key_value(ls,key):
    for item in ls :
        print(item[key])
ls=[
    ("Almas",23),
    ("Tanim",24),
    ("Sakib",22)
]
get_sort_key_value(ls=ls,key=0)
print("_________________________")

def get_sort_key_value(ls,key):
    for item in ls:
        print(item[key])
new_ls=[
    ("Computer",500000,"India"),
    ("Mobile",30000,"China"),
    ("Dress",500,"Bangladesh")

]
get_sort_key_value(ls=new_ls,key=0)
get_sort_key_value(ls=new_ls,key=1)
get_sort_key_value(ls=new_ls,key=2)