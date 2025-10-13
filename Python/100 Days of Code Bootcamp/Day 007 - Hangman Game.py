
import os
import random
from wordfreq import top_n_list, zipf_frequency

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_word(min_len=7, max_len=20, lang="en", min_zipf=3.5, max_zipf=6.5):
    # get the top ~50k words as a positional arg
    vocab = top_n_list(lang, 50_000)
    candidates = [
        w for w in vocab
        if w.isalpha()
        and min_len <= len(w) <= max_len
        and min_zipf <= zipf_frequency(w, lang) <= max_zipf
    ]
    if not candidates:
        raise RuntimeError("No candidates found with current filters.")
    return random.choice(candidates).lower()

# Graphics

logo = (r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

full_lives = (r"""
    +---+
    |   |
        |
        |
        |
        |
  ===========
""")



lives5_6 = (r"""
    +---+
    |   |
    O   |
        |
        |
        |
  ===========
""")

lives4_6 = (r""""
    +---+
    |   |
    O   |
    |   |
        |
        |
  ===========
""")

lives3_6 = (r""""
    +---+
    |   |
    O   |
   /|   |
        |
        |
  ===========
""")

lives2_6 = (r""""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  ===========
""")

lives1_6 = (r""""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  ===========
""")

no_lives = (r""""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ===========
""")


# List of hangman graphics

lives = [full_lives, lives5_6, lives4_6, lives3_6, lives2_6, lives1_6, no_lives]

# Chosen word for the challenge
chosen_word = random_word()
chosen_length = len(chosen_word)

# Create a placeholder and replace words in chosen_words with _
placeholder = ""
for pos in range(1, chosen_length+1):
    placeholder += "_"

# Create a display that puts the letter in the right position of the placeholder
# display will be what will be printed out for the user
display = ""

correct_letters = []
guessed_letters = []

# Lives
nr_lives = 6
display_lives = 0

# game_on variable
game_on = True

clear()
print(logo)
print(lives[0])
print(f"Word to guess: {placeholder}")
print(f"The word has {chosen_length} letters.")
print("Good luck!")

# START

while game_on:    
    print("\n")
    guess = input("Guess a letter: ").lower()
    guess = guess[0]

    if guess not in guessed_letters:
        guessed_letters.append(guess)
        guessed_letters.sort()

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
                clear()
                print(logo)

        if guess in chosen_word:
            print(f"You guessed '{guess}. That was correct.")
        else:
            nr_lives -= 1
            display_lives += 1
            print(f"You guessed '{guess}'. That's not in the word. You lose a life.")

    elif guess in guessed_letters:
        clear()
        print(logo)
        print("You already tried that letter.")


    print(lives[display_lives])

    if "_" not in display:
        print("You have guessed the word!")
        print(f"You had {nr_lives}/6 lives remaining.")
        game_on = False
    else:
        if nr_lives == 0:
            print("You are dead!")
            print(f"The correct word was: {chosen_word}.")
            game_on = False
        else:
            print(f"You have {nr_lives}/6 remaining")
            print(f"Word to guess: {display}")
            print(f"The word has {chosen_length} letters.")
            print(f"Currently, you have tried: {guessed_letters}")
