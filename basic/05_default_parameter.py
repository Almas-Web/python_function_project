def greet (name,email,age=None):
    """a function that greet a person with their name , email and age"""
    print(f"Hello, {name}! Your email is {email}.")
    print(f"Hello {name}.Your age is {age}.your email is {email}")

# Call the function with multiple arguments
greet(name="Almas",email="almashossen@gmail.com")
greet(name="Joy",email="joy@gmail.com",age=22) 
print("-----------------------------------------------")

def greet(name, email, age=None):
    """A function that greets a person with their name, email, and optional age"""
    
    if age is not None:
        print(f"Hello {name}! Your email is {email} and your age is {age}.")
    else:
        print(f"Hello {name}! Your email is {email}. (Age not provided)")


greet(name="Almas", email="almashossen@gmail.com")      
greet(name="Joy", email="joy@gmail.com", age=22)      
greet("Rafi", "rafi123@gmail.com", 30)    # positional arguments             
greet("Sadia", "sadia456@gmail.com")                
