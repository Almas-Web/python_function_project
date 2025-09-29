def greet(name,email):
    """a function that greet a person with their name and email"""
    print(f"Hello, {name}! Your email is {email}.")
# Call the function with multiple arguments
greet(name="Almas", email="almashossen@gmail.com") # keyword arguments

greet("Joy" , "joy@gmail.com") 

greet(email="almashossen@gmail.com",name="Almas") # here we don't need to maintain sequence

greet("joy@gmail,.com", "Joy") # here we need to maintain sequence # positional arguments
