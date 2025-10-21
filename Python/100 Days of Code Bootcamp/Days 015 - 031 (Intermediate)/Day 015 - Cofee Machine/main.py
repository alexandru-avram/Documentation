MENU = {
    "esspresso": {
        "ingredients": {
        "water": 50,
        "coffee": 18},
    "cost": 1.5
    },

    "lattee": {
        "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24},
    "cost": 2.5
    },

    "cappuccino": {
        "ingredients": {
        "water": 250,
        "milk": 100,
        "coffee": 24},
    "cost": 3.0
    }}

ressources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money = 0

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_resourece_sufficient(order_ingredients):
    """ Returns true if total can be made or false if we need more ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= ressources[item]:
            print(f"Sorry, thre is not enough {item}.")
            return False
        return True

def process_coins():
    """ Returns the total talculated from the coins inserted """
    print("Please insert coins.")
    total = int(input("Quarters $0.25: ")) * 0.25
    total += int(input("Dimes $0.10: ")) * 0.1
    total += int(input("Nickles $0.05: ")) * 0.05
    total += int(input("Pennies $0.01: ")) * 0.01

    return total


def is_transaction_succsessful(money_received, drink_cost):
    """ Returns True when the payment is accepted, False if the money is insufficient """
    global money
    
    if money_received >= drink_cost:
        money += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: {change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """ Deduct ingredients required from the resources """
    for item in order_ingredients:
        ressources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


clear()
is_on = True
while is_on:
    choice = input("What would you like to? (espresso, lattee, cappuccino)")

    if choice == "off":
        clear()
        is_on = False
    elif choice == "report":
        print(f"Water {ressources["water"]}ml")
        print(f"Milk {ressources["milk"]}ml")
        print(f"Coffee {ressources["coffee"]}ml")
        print(f"Money {money}")
    else:
        drink = MENU[choice]
        if is_resourece_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succsessful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
