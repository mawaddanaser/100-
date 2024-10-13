MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarters_value = 0.25
dimes_value = 0.10
nickles_value = 0.05
pennies_value = 0.01


# TODO: 2 check if resources sufficient
def is_resources_sufficient(order_ingredients):
    """it checks if order ingredients sufficient so return True
      Or if not return False."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry the {order_ingredients} is not sufficient")
            return False

    return True


# TODO: 3 coin process
def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * quarters_value) + (dimes * dimes_value) + (nickles * nickles_value) + (pennies * pennies_value)
    return total


# TODO: 4 check if transaction successful
def is_transaction_successful(money_received, drink_cost):
    """return true if the payment is accepted Or False if is not sufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True

    print("Sorry that's not enough money. Money refunded.")
    return False


# TODO: 5 make a coffe and  deducted report
def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO: 1 Prompt user by asking
def coffe_machine():
    profit = 0
    is_coffe_machine_on = True
    while is_coffe_machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            is_coffe_machine_on = False
        elif user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[user_choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coin()
                if is_transaction_successful(payment, drink["cost"]):
                    profit += drink["cost"]
                    make_coffe(user_choice, drink["ingredients"])


coffe_machine()
