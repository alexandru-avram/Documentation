import random

# Clear screen and print the logo
import os
def clear_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
          """)
    print("Welcome to the Number Guessing Game!")
    print("\n\n")

def number_check():
    global number_to_guess
    global my_guess
    global attempts

    if number_to_guess == my_guess:
        print(f"You got it! The answer was {number_to_guess}.")
    elif number_to_guess > my_guess:
        print("Too low")
        attempts -= 1
    elif number_to_guess < my_guess:
        print("Too high.")
        attempts -= 1
    
    if attempts == 0:
        print(f"You failed. The answer was {number_to_guess}.")

# Difficulty - how many guesses
def chose_difficulty():
    global attempts
    difficulty = {"easy": 10,
              "hard": 5}

    dif_chosen = ""

    # Choose a difficulty
    while dif_chosen not in ["easy", "hard"]:
        dif_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ")

    attempts = difficulty[dif_chosen]
    return attempts


# Number to guess
number_to_guess = random.randint(0,100)
my_guess = 101
attempts = 0

# INTRO HERE
clear_logo()
print("I'm thinking of a number between 1 and 100. Can you guess it?")

chose_difficulty()


while my_guess != number_to_guess and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    my_guess = int(input("Make a guess: "))

    number_check()


input("Thank you for playing. Press 'ENTER' to continue...")