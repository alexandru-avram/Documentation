import random

# Clear screen and print the logo
import os
def clear_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/       
          """)
    print("\n\n")

# Check if my guess is equal to the random number

def provide_choices():
    global instagram_accounts
    global choice_a
    global choice_b

    choice_a = random.choice(list(instagram_accounts))
    choice_b = random.choice(list(instagram_accounts))

    # This is created to ensure that there will be no 2 choices having the same account
    while choice_a == choice_b:
        choice_b = random.choice(list(instagram_accounts))

    print(f"Choice A: {choice_a} - {instagram_accounts[choice_a][1]} from {instagram_accounts[choice_a][2]}")
    
    print(r"""
_    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
    """)


    print(f"Choice B: {choice_b} - {instagram_accounts[choice_b][1]} from {instagram_accounts[choice_b][2]}")

def more_followers():
    global instagram_accounts
    global choice_a
    global choice_b
    global my_choice
    global has_more_followers

    if instagram_accounts[choice_a][0] > instagram_accounts[choice_b][0]:
        has_more_followers = "a"
    elif instagram_accounts[choice_b][0] > instagram_accounts[choice_a][0]:
        has_more_followers = "b"



# Dictionary to hold top 100 Instagram accounts as of 16.10.2025
instagram_accounts ={"Instagram": [676700000, "social network", "United States"],
    "Cristiano Ronaldo": [639900000, "football player", "Portugal"],
    "Leo Messi": [504000000, "football player", "Argentina"],
    "Selena Gomez": [424300000, "singer and actress", "United States"],
    "Kylie Jenner": [396700000, "businesswoman and media personality", "United States"],
    "Dwayne Johnson": [395300000, "actor and wrestler", "United States"],
    "Ariana Grande": [376800000, "singer", "United States"],
    "Kim Kardashian": [364200000, "media personality", "United States"],
    "Beyoncé": [318900000, "singer", "United States"],
    "Khloé Kardashian": [311700000, "media personality", "United States"],
    "Nike": [304400000, "sportswear brand", "United States"],
    "Justin Bieber": [294500000, "singer", "Canada"],
    "Kendall Jenner": [294300000, "model", "United States"],
    "Taylor Swift": [284000000, "singer-songwriter", "United States"],
    "National Geographic": [281300000, "magazine and media", "United States"],
    "Virat Kohli": [264400000, "cricketer", "India"],
    "Jennifer Lopez": [253000000, "singer and actress", "United States"],
    "Nicki Minaj": [228300000, "rapper", "Trinidad and Tobago"],
    "Kourtney Kardashian": [224800000, "media personality", "United States"],
    "Neymar Jr": [216800000, "football player", "Brazil"],
    "Miley Cyrus": [215700000, "singer and actress", "United States"],
    "Katy Perry": [205800000, "singer", "United States"],
    "Zendaya": [185100000, "actress and singer", "United States"],
    "Kevin Hart": [179500000, "comedian and actor", "United States"],
    "Cardi B": [169100000, "rapper", "United States"],
    "LeBron James": [159000000, "basketball player", "United States"],
    "Demi Lovato": [157600000, "singer and actress", "United States"],
    "Rihanna": [152700000, "singer and entrepreneur", "Barbados"],
    "Real Madrid": [149300000, "football club", "Spain"],
    "Chris Brown": [144800000, "singer", "United States"],
    "Drake": [144400000, "rapper", "Canada"],
    "Ellen DeGeneres": [139800000, "TV host and comedian", "United States"],
    "FC Barcelona": [124900000, "football club", "Spain"],
    "UEFA Champions League": [111700000, "football competition", "Switzerland"],
    "Billie Eilish": [110200000, "singer", "United States"],
    "Kylian Mbappé": [110100000, "football player", "France"],
    "Gal Gadot": [109500000, "actress", "Israel"],
    "Vin Diesel": [101900000, "actor", "United States"],
    "LISA": [99300000, "singer", "Thailand"],
    "NASA": [97300000, "space agency", "United States"],
    "Shakira": [90000000, "singer", "Colombia"],
    "Priyanka Chopra Jonas": [89900000, "actress", "India"],
    "Dua Lipa": [88500000, "singer", "United Kingdom"],
    "David Beckham": [86100000, "football player", "United Kingdom"],
    "Shraddha Kapoor": [84600000, "actress", "India"],
    "NBA": [84100000, "sports league", "United States"],
    "Snoop Dogg": [83000000, "rapper", "United States"],
    "Narendra Modi": [81400000, "politician", "India"],
    "Khaby Lame": [81400000, "content creator", "Italy"],
    "Alia Bhatt": [80900000, "actress", "India"],
    "Gigi Hadid": [79000000, "model", "United States"],
    "Deepika Padukone": [77600000, "actress", "India"],
    "Victoria's Secret": [76300000, "fashion brand", "United States"],
    "Karim Benzema": [76200000, "football player", "France"],
    "The Weeknd": [75300000, "singer", "Canada"],
    "Emma Watson": [75100000, "actress", "United Kingdom"],
    "Ronaldinho": [74800000, "football player", "Brazil"],
    "ROSÉ": [74600000, "singer", "South Korea"],
    "BTS": [74000000, "music group", "South Korea"],
    "Raffi & Nagita": [73800000, "TV personalities", "Indonesia"],
    "Shawn Mendes": [73600000, "singer", "Canada"],
    "Justin Timberlake": [72000000, "singer and actor", "United States"],
    "Premier League": [71400000, "sports league", "United Kingdom"],
    "433": [69500000, "sports media", "Netherlands"],
    "Marvel": [67700000, "entertainment studio", "United States"],
    "Salman Khan": [67400000, "actor", "India"],
    "Camila Cabello": [67100000, "singer", "United States"],
    "Karol G": [67000000, "singer", "Colombia"],
    "Akshay Kumar": [66700000, "actor", "India"],
    "Tom Holland": [66500000, "actor", "United Kingdom"],
    "Anushka Sharma": [66300000, "actress", "India"],
    "Marcelo Vieira": [66100000, "football player", "Brazil"],
    "Paris Saint-Germain": [65700000, "football club", "France"],
    "Anitta": [64800000, "singer", "Brazil"],
    "Will Smith": [64700000, "actor", "United States"],
    "Zlatan Ibrahimović": [63900000, "football player", "Sweden"],
    "Maluma": [63800000, "singer", "Colombia"],
    "Manchester United": [63100000, "football club", "United Kingdom"],
    "Mohamed Salah": [63000000, "football player", "Egypt"],
    "V (Kim Taehyung)": [62500000, "singer", "South Korea"],
    "Sergio Ramos": [62200000, "football player", "Spain"],
    "Leonardo DiCaprio": [62000000, "actor", "United States"],
    "Zac Efron": [61900000, "actor", "United States"],
    "ZARA": [61900000, "fashion brand", "Spain"],
    "Paul Pogba": [61500000, "football player", "France"],
    "Bella Hadid": [61100000, "model", "United States"],
    "MrBeast": [60600000, "content creator", "United States"],
    "Disha Patani": [60200000, "actress", "India"],
    "Juventus": [59900000, "football club", "Italy"],
    "Whindersson Nunes": [59700000, "comedian and YouTuber", "Brazil"],
    "CHANEL": [59200000, "fashion brand", "France"],
    "Stephen Curry": [58100000, "basketball player", "United States"],
    "Chris Hemsworth": [58000000, "actor", "Australia"],
    "Paulo Dybala": [57900000, "football player", "Argentina"],
    "BLACKPINK": [57600000, "music group", "South Korea"],
    "Adele": [57400000, "singer", "United Kingdom"],
    "Robert Downey Jr.": [57200000, "actor", "United States"],
    "Michelle Obama": [57200000, "public figure and author", "United States"],
    "Tatá Werneck": [57000000, "comedian and actress", "Brazil"],
    "Joko Widodo": [56500000, "politician", "Indonesia"]
}

# Save Choice A and Choice B
choice_a = ""
choice_b = ""
my_choice = ""
has_more_followers = ""
score = 0
game_on = True
session_on = True

# START

while game_on:
    while session_on:
        clear_logo()
        my_choice = ""
        if score > 0:
            print(f"Your score is: {score}\n")

        provide_choices()
        more_followers()

        while my_choice not in ["a","b"]:
            my_choice = input("Who has more follower? Type 'A' or 'B': ").lower()
        
        print(my_choice)
        print(has_more_followers)

        if my_choice == has_more_followers:
            score += 1
            session_on = True
        else:
            session_on = False

    clear_logo()
    print(f"Your final score is: {score}")
    
    while my_choice not in ["y", "n"]:
        my_choice = input("Do you want to play again? Type 'y' or 'n': ")
    
    if my_choice == "y":
        session_on = True
        score = 0
    elif my_choice == "n":
        game_on = False

clear_logo()
input(f"Thank you for playing. Your final score was {score}. Press ENTER to continue...")
    