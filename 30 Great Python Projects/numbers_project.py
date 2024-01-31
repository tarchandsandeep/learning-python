
def subtract(num1, num2): 
    sub = num1 - num2 
    print(sub)
    return sub

x = subtract(8,5)

def multiply(num1, num2):
    mult = num1 * num2
    print(mult)
    return mult

y = multiply(3,4)

print(y)

def divide(num1, num2):
    div = num1 / num2
    print(div)
    return div

z = divide(50,5)
# We are resuisng the code. 
# In this use case what are we resusing
randy = multiply(3,4) # 3 ** 4
sashank = multiply(6,4) # 6 ** 4

print('randy', randy)
print('sashank', sashank)

# Task: How to do all the operations(divide, multiple, subtract add) in one function

def perform_operation(num1, num2, operation_name):
    if(operation_name == "add"):
        add = num1 + num2 
        return add 
    elif(operation_name == "subtract"):
        subtract = num1 - num2 
        return subtract
    elif (operation_name == "multiply"):
        multiply = num1 ** num2
        return multiply
    elif(operation_name == "divide"):
        divide = num1 / num2
        return divide
    



zzz = perform_operation(1,2,"multiply")

zzz = perform_operation(1,2,"add")

print(zzz)


