def calculate(number):
    square=number**2  # number*2 ==10x2
    cube=number**3    # number*3 == 10x3
    return square,cube
result=calculate(number=10)
print(result) # output will be a tuple 
print("__________________")
result_square,result_cube=calculate(number=21)
print(result_square)
print(result_cube)
print("______________________________________")
# shortcut method 
def calculate(number):
    return number**2,number**3,number**4
result=calculate(number=111111)
print(result)