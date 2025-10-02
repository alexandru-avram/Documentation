print("Welcome to Treasure Island",
"\nYour mission is to find the treasure")

print("\n\n")

game_on = True
victory = False


while game_on:
    print("You are at a cross road. Where do you want to go?",
        "\n\t",
        "Left or Right")
    choice_1 = input().strip().lower()

    if choice_1 == "right":
        game_on = False
        break
    elif choice_1 == "left":
        pass
    else:
        print("Choose left or right")
        continue
       
    print("You have arrived at a lake. What do you want to do?",
          "\n\t",
          "Swim or Wait for a boat")
    choice_2 = input().strip().lower()
    
    if choice_2 == "swim":
        game_on = False
        break
    elif choice_2 == "wait":
        pass
    else:
        print("Choose to either swim or wait!")
        continue


    print("You have arrived at the castle. You enter it to find three doors. Which one do you choose?",
          "\n\t",
          "Door 1, Door 2 or Door 3?")
    choice_3 = int(input().strip())
    if choice_3 == 2:
        victory = True
        game_on = False
    else:
        game_on = False



if victory == True:
    print("You have found the treasure!")
else:
    print("You are dead!")
print("Gave over!")


