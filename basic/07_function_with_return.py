# return is the last line of a function 
def get_percentage(amount,percentage):
    result=(amount*percentage)/100
    return result # without return output will be None
percentage_amount=get_percentage(amount=5123,percentage=35)
print(percentage_amount)
print("--------------------------")

def get_percentage(amount,percentage):
    if not isinstance(amount,int):
        if not isinstance(amount,float):
            return "Invalid amount"
    if not isinstance(percentage,int):
        if not isinstance(percentage,float):
            return "Invalid percentage"
    result=(amount*percentage)/100
    return result  # without return output will be None
percentage_amount=get_percentage(amount=1234567654,percentage=19)
print(percentage_amount)

percentage_amount=get_percentage(amount=12244.44,percentage="21")
print(percentage_amount)