"""
**kwargs collects extra keyword arguments into a dictionary.

You can combine *args and **kwargs in a function:
"""
def greet(**kwargs):
    print(kwargs)
    print(kwargs,type(kwargs))
greet()
greet(user_name="Almas")
greet(user_name="sakib",is_loggedin=True)
greet(user_name="tanim",is_loggedin=True,is_subscribed=False)
print("________________-")

def greet(**kwargs):
    print(kwargs.get("user_name"))
    print(kwargs.get("is_loggedin"))
    print(kwargs.get("is_subscribed"))
greet(user_name="Almas")
greet(user_name="Sakib",is_loggedin=True)
greet(user_name="Tanim",is_loggedin=True,is_subscribed=False)
print("____________________")

def greet(**kwargs):
    if (kwargs.get("user_name") is not None):
        print(kwargs.get("user_name"))
    if (kwargs.get("is_loggedin") is not None):
        print(kwargs.get("is_loggedin"))
    if(kwargs.get("is_subscribed") is not None):
        print(kwargs.get("is_subscribed"))
greet(user_name="Almas")
greet(user_name="Sakib",is_loggedin=True)
greet(user_name="Tanim",is_loggedin=True,is_subscribed=False)
print("____________________")

def greet(**kwargs):
    user_name=kwargs.get("user_name")
    is_loggedin=kwargs.get("is_loggedin")
    is_subscribed=kwargs.get("is_subscribed")
    
    if user_name is not None:
        print(user_name)
    if is_loggedin is not None:
        print(is_loggedin)
    if is_subscribed is not None:
        print(is_subscribed)
greet(user_name="Almas")
greet(user_name="Sakib",is_loggedin=True)
greet(user_name="Tanim",is_loggedin=True,is_subscribed=False)
print("____________________")

def some(*args,**kwargs):
    print(args)  # *args → tuple -> (1, 2, 3)
    print(kwargs)  #**kwargs → dictionary ->{'user_name': 'Almas', 'email': 'almas@gmail.com'}
some(1,2,3, user_name="Almas",email="almas@gmail.com")
print("__________________________")

def some(a,b,*args,**kwargs):
    print(args)  # *args → tuple -> (3,)
    print(kwargs)  #**kwargs → dictionary ->{'user_name': 'Almas', 'email': 'almas@gmail.com'}
some(1,2,3, user_name="Almas",email="almas@gmail.com")
print("_________________")

def student_info(id, name, *marks, **details):
    print(f"ID: {id}")
    print(f"Name: {name}")
    
    if marks:
        print("Marks:", marks)  
    
    if details:
        print("Other Details:", details)  


# Function call
student_info(
    101, "Almas",
    85, 90, 78,                
    age=21, city="Dhaka", dept="CSE"   # **kwargs → details dictionary
)
