def add_finction(x, y=100):
    return x + y


def subtract_function(x, y):
    return x - y


def multiply_function(x, y):
    return x * y


def division_function(x, y):
    if y == 0:
        print("divisin by zero is not allowed")
    return x / y

def main_function():
    x = float(input("enter X: "))
    y = float(input("enter y: "))
    # add_result = add_finction(x, y)
    # subtract_result = subtract_function(x, y)
    # multiply_result = multiply_function(x, y)
    # division_result = division_function(x, y)
    print(f"""
        add result: {add_finction(x, y)}
        subtract result: {subtract_function(x, y)}
        multiply result: {multiply_function(x, y)}
        division result:  {division_function(x, y)}
    """)


main_function()