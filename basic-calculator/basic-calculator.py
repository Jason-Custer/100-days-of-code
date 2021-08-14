# Calculator Program

# Variables:

x = 1
y = 1

# Functions:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    from art import logo
    print(logo)

# Input the first number in the calculator:

    x = float(input("What is the first number? "))

# Choose the type of operator:

    another_calculation = True

    while another_calculation == True:
        for symbol in functions:
            print(symbol)
        operator = input("Select the operator:\n")
        y = float(input("What is the next number? "))
    
        calculation = functions[operator]
        result = calculation(x, y)

        print(f"{x} {operator} {y} = {result}")
    
        response = input(f"Type 'y' to continue with {result} or 'n' to calculate something else: ")
        if response == "y":
            another_calculation = True
            x = result
        else:
            another_calculation = False
            calculator()

calculator()
    
