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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources_sufficient(ingredients):
    '''Checks if the amount of resources are sufficient to make the desired drink.'''

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f" Sorry, there is not enough {item}.")
            return "insufficient"
    return "sufficient"
# End of check_resources_sufficient function.

def process_coins():
    '''Prompts user to enter coins, processes them, and stores them in one variable (coins).'''

    coins = 0.0
    print("Please insert coins.")

    quarters = float(input("How many quarters?: "))
    coins += quarters * 0.25

    dimes = float(input("How many dimes?: "))
    coins += dimes * 0.10

    nickels = float(input("How many nickels?: "))
    coins += nickels * 0.05

    pennies = float(input("How many pennies?: "))
    coins += pennies * 0.01

    return coins
# End of process_coins function.

def check_transaction_successful(drink, coins, menu):
    '''Checks if transaction was successful, refunds change, and stores the coins in the machine.'''

    cost_of_drink = menu[drink]["cost"]

    if coins < cost_of_drink:
        print("Sorry, that's not enough money. Money refunded.")
        return "unsuccessful"
    if coins == cost_of_drink:
        resources["money"] += cost_of_drink
        return "successful"
    if coins > cost_of_drink:
        resources["money"] += cost_of_drink
        change = coins - cost_of_drink
        print(f"Here is ${round(change, 2)} in change.")
        return "successful"  
# End of check_transaction_successful function

def deduct_resources(ingredients):
    '''Deducts resources from the machine after the transaction has went through (makes drink).'''

    for item in ingredients:
        resources[item] -= ingredients[item]
# End of deduct_resources function.

MACHINE_RUNNING = True
while MACHINE_RUNNING:
    # Prompt user to select a drink.
    selection = input(" What drink would you like? espresso($1.50) ~ latte($2.50) ~ cappuccino($3.00): ")

    # Add ability for the coffee machine to be turned off; via user input that ends the program.
    if selection == "off":
        MACHINE_RUNNING = False

    # Print a report that shows the current resources in the coffee machine.
    elif selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        # Check if current resources are sufficient to make the desired drink.
        if check_resources_sufficient(MENU[selection]["ingredients"]) == "sufficient":
            # Prompt user to enter coins and process them.
            input_coins = process_coins()

            # Check if the transaction was successful.
            transaction = check_transaction_successful(selection, input_coins, MENU)

            # Make the drink.
            if transaction == "successful":
                deduct_resources(MENU[selection]["ingredients"])
                print(f"Here is your {selection} ☕. Enjoy!")
