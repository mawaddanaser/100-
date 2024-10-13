# calculator
# from art import logo

# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# division
def division(n1, n2):
    return n1 / n2


# create dictionary
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": division
              }


# function = operations["+"]
# function(3, 2)
def calculator():
    # print(logo)
    num1 = float(input("What is the first number?: "))
    # loop through operation to ask user which one wanted
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            # recursion
            calculator()


calculator()
