import os

"""
This is a docstring
Remember this
or not
"""


# Clear screen and print the logo
def clear_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""          
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
    print("\n\n")

# Calculator functions
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Variables
n1 = 0
n2 = 0
result = 0

# Boolean variables to keep the calculation going
program_on = True
running_calc = True

# Operations dictionary
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# START

# We will be using recursion instead of a while loop
# Create a function and call it at the end to keep it working
def calculator():
    clear_logo()    
    result = 0
    running_calc = True
    n1 = float(input("What is the first number?: "))

    while running_calc:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        n2 = float(input("What is the next number?: "))

        result = operations[operation_symbol](n1,n2)
        
        print(f"{n1} {operation_symbol} {n2} = {result}")
        choice = input("Do you want to continue this calclations, start a new calculation... or exit? Type 'y', 'n': ").lower()

        while choice not in ["y", "n"]:
                choice = input("Do you want to continue this calclations, start a new calculation... or exit? Type 'y', 'n': ").lower()
        
        if choice == "y":
            n1 = result
        elif choice == "n":
            running_calc = False
            calculator()


calculator()
clear_logo()
input("Thank you for using me. Press enter to continue...")