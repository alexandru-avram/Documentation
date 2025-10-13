print("Welcome to the tip calculator!")
print("\n \n")

bill = int(input("What is your total bill? $"))
tip = int(input("How much tip would you like to give? %: ").rstrip("%"))
split = int(input("How many people to split the bill? "))

split_cost = bill * (1+ tip/100) / split

print(f"Each person should pay ${split_cost}")
