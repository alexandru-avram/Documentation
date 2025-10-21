# Imports
import random

# Lists of values
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Password storage variable
password_storage = []
password_generated = ''

# Star screen
print("Welcome to the PyPassword Generator!")
print("\n\n")

# Program: getting number of elements in your passowrd
print("How many letters would you like in your passowrd?")
nr_letters = int(input())

print("How many numbers would you like?")
nr_numbers = int(input())

print("How many special characters would you like?")
nr_symbols = int(input())

# password_storage will be populated with random letters, numbers and symbols
for letters in range(1, nr_letters+1):
    password_storage.append(random.choice(letters_list))

for numbers in range(1, nr_numbers+1):
    password_storage.append(random.choice(numbers_list))

for symbol in range (1, nr_symbols+1):
    password_storage.append(random.choice(symbols_list))

# Shuffle the password_storage list
random.shuffle(password_storage)

# Transfer the list to a string by using join
password_generated = "".join(str(i) for i in password_storage)

# Print password
print(f"Your password is: {password_generated}")