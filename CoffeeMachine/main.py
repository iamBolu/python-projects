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
    "money": 0.0,
}

def report():
    for item in resources:
        print(f"{item.title()}: {resources[item]}")

def check(value):
     r_water = resources['water']
     r_milk = resources['milk']
     r_coffee = resources['coffee']


     drink = MENU[value]["ingredients"]

     if drink.get("water", 0) > r_water:
         print("Sorry there is not enough water")
     elif drink.get("milk", 0) > r_milk:
        print("Sorry there is not enough milk")
     elif  drink.get("coffee", 0) > r_coffee:
         print("Sorry there is not enough ")
     else:
         print("Please insert coins")
         quarters = int(input("How many quarters?: "))
         dimes = int(input("How many dimes?: "))
         nickels = int(input("How many nickels?: "))
         pennies = int(input("How many pennies?: "))
         total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
         if MENU[value]["cost"] > total:
             print(" Sorry that's not enough money. Money refunded.")
         else:
             change = total - MENU[value]["cost"]
             resources["money"] += MENU[value]["cost"]
             resources["water"] -= drink.get("water", 0)
             resources["milk"] -= drink.get("milk", 0)
             resources["coffee"] -= drink.get("coffee", 0)
             print(f"Here is ${round(change, 2)} in change")
             print(f"Here is your {value}. Enjoy!")







machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        check(choice)


