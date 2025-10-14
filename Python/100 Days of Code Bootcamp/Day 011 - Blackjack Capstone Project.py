
import random

# Clear screen and print the logo
import os
def clear_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""          
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/
""")
    print("\n\n")

# Cards dictionary
def new_card_pack():
   cards ={"1":[1,1,1,1],
                    "2":[2,2,2,2],
                    "3":[3,3,3,3],
                    "4":[4,4,4,4],
                    "5":[5,5,5,5],
                    "6":[6,6,6,6],
                    "7":[7,7,7,7],
                    "8":[8,8,8,8],
                    "9":[9,9,9,9],
                    "10":[10,10,10,10],
                    "J":[11,11,11,11],
                    "Q":[12,12,12,12],
                    "K":[13,13,13,13],
                    "A":[14,14,14,14]
                }
   
   return cards

# Deal cards
def deal_card(cards):
    new_card = ""
    new_card = random.choice(list(cards.keys()))
    cards[new_card].pop()

    return new_card

# CPU Logic
def cpu_logic(sum_my_cards, sum_cpu_cards, cards, my_choice, cpu_cards):
    if my_choice == "y":
        if (sum_cpu_cards < sum_my_cards or sum_cpu_cards < 17) and sum_cpu_cards != 21:
            cpu_cards.append(deal_card(cards))
    elif my_choice == "n":
        if sum_cpu_cards < sum_my_cards and sum_cpu_cards != 21:
            cpu_cards.append(deal_card(cards))          

# START

game_on = True
round = True
cards = {}

while game_on:
    my_cards = []
    cpu_cards = []
    cards = new_card_pack()

    sum_my_cards = 0
    sum_cpu_cards = 0
    my_cards.append(deal_card(cards))
    my_cards.append(deal_card(cards))

    cpu_cards.append(deal_card(cards))
    cpu_cards.append(deal_card(cards))

    while round:
        clear_logo()
        choice = ""
        sum_my_cards = 0
        sum_cpu_cards = 0
        for i in my_cards:
            sum_my_cards += cards[i][0]

        for i in cpu_cards:
            sum_cpu_cards += cards[i][0]
        print(f"Your cards are: {my_cards}\nYour total score is: {sum_my_cards}")
        print("\n")
        print(f"CPU cards are: {cpu_cards}\nCPU total score is: {sum_cpu_cards}")
        print("\n")
        
        if sum_cpu_cards > 21 or sum_my_cards > 21:
            round = False
            break
        elif sum_my_cards == 21:
            round = False
            break
        elif sum_cpu_cards == 21:
            round = False
            break
        
        while choice not in ("y","n"):
            choice = input("Do you want another hit? y/n \n").lower()

        if choice == "y": 
            my_cards.append(deal_card(cards))
            cpu_logic(sum_my_cards, sum_cpu_cards, cards, choice, cpu_cards)
        if choice == "n":
            cpu_logic(sum_my_cards, sum_cpu_cards, cards, choice, cpu_cards)
            round = False
        

    clear_logo()
    print(f"Your cards are: {my_cards}\nYour total score is: {sum_my_cards}")    
    print(f"CPU cards are: {cpu_cards}\nCPU total score is: {sum_cpu_cards}")   

    if sum_my_cards > 21 and sum_cpu_cards > 21:
        print("Both loose.")
    elif sum_my_cards > 21 and sum_cpu_cards <= 21:
        print("CPU wins!")
    elif sum_my_cards <= 21 and sum_cpu_cards > 21:
        print("You win!")
    elif sum_cpu_cards > sum_my_cards:
        print("CPU wins!")
    elif sum_my_cards > sum_cpu_cards:
        print("You win!")
    elif sum_my_cards == sum_cpu_cards:
        print("Equality.")

    choice = input("Go again?\n").lower()
    if choice == "y":
        round = True
    else:
        game_on = False


    

