a=10
b=10.2222
c="Hello"
d=True
e=None
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,bool))
print(isinstance(e,type(None)))   

print("-----------------------------------------------")
def greet(name, email, age=None):
    if (age is  not None and isinstance(age,int) and  age>=18):
        print("You are eligible for voting.")
    else:
        print("You are not eligible for voting.")
    print(f"Hello {name} ! Your email is {email}.")
# call the function
greet(name="Almas",email="almas@gmail.com")
greet(name="joy",email="joy@gmmail.com",age=20)
greet(name="sadi",email="sadi@gmail.com",age="20")
greet(name="rafi",email="rafi@gmail.com",age=12)
