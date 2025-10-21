# Randomization and Python Lists
# Create a "Rock, Paper, Scissors game"

import random
rps_choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock, Paper, Scissors" \
"\nThe game is simple. I select rock, paper, or scissors... you select rock, paper, or scissors.")


game_on = True

while game_on:

    cpu_choice = random.choice([1,2,3])
    print("\nPaper beats rock. Scissors beat paper. Paper beats rock.\n" \
        "\nSelect (1-3):" \
        "\n\t1. Rock" \
        "\n\t2. Paper" \
        "\n\t3. Scissors")
    
    player_choice = int(input("\nYour choice: "))

    


    if cpu_choice == player_choice:
        print(f"{rps_choices[cpu_choice-1]} equals {rps_choices[player_choice-1]}. No one wins.")
    elif (cpu_choice == 2 and player_choice == 1) or (cpu_choice == 3 and player_choice == 2) or (cpu_choice == 1 and player_choice == 3):
        print(f"{rps_choices[cpu_choice-1]} beats {rps_choices[player_choice-1]}. I win.")
    else:
        print(f"{rps_choices[cpu_choice-1]} looses to {rps_choices[player_choice-1]}. You win.")
    
    replay_game = input("Play again? Y or N: ")

    if replay_game.lower() == "y":
        game_on = True
    else:
        game_on = False
        break