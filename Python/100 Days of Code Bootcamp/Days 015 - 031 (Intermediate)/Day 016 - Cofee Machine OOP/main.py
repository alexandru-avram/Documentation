from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


""" First we are going to create 3 Class objects.
1. Object to hold the money machine to process payments
2. Object to hold the coffee maker to process orders
3. Object to hold the menu items
"""
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# While loop start
is_on = True
while is_on:
    options = menu.get_items() # Will get the objects on the menu... latte/espresso/cappuccino

    # Have the user make a choice 
    choice = input(f"What would you like? {options}: ")

    if choice == "off": # turn off the machine
        is_on = False

    elif choice == "report": # print report to see available resources
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice) # it will find the drink and save it based on user input
        
        """ 
        It will check first to see if the coffee machine has enough ingredients
        It will then process the payments
        If all is successfull, it will make the coffee
        """
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
