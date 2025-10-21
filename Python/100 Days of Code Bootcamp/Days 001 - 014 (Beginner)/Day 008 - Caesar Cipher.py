import os

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to encode the message
def encode_message(message, chr_shift, alphabet):
    encrpyted_list = []

    for character in message:
        if character not in alphabet:
            encrpyted_list.append(character)
        elif character in alphabet:
            i = alphabet.index(character)
            new_letter = alphabet[i + chr_shift]
            encrpyted_list.append(new_letter)

    encrpyted_message = "".join(str(i) for i in encrpyted_list)
    return encrpyted_message

# function to decode the message
def decode_message(encrypted_message, chr_shift, alphabet):
    decrpyted_list = []

    for character in encrypted_message:
        if character not in alphabet:
            decrpyted_list.append(character)
        elif character in alphabet:
            i = alphabet.index(character)
            new_letter = alphabet[i - chr_shift]
            decrpyted_list.append(new_letter)
    
    decrpyted_message = "".join(str(i) for i in decrpyted_list)
    return decrpyted_message
    
logo=(r""""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88          
""")

# the alhpabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# will hold the character shift
chr_shift = 0
# will hold the initial message
message = ""
# will hold the encrypted message
encrpyted_message = ""
# will hold the decrypted message... which should be the initial message
decrpyted_message = ""
# will determine if we want to encode or decode or to exit the program
direction = ""

# START
while direction.lower() != "exit":
    clear()
    print(logo)
    direction = input("Type 'encode' to encrpyt, or 'decode' to decrypt. Type 'exit' to exit:\n").lower()

    # Checking to ensure that the message if in our listen
    if direction not in ["exit", "encode", "decode"]:
        clear()

    # If the user wants to encode
    elif direction == "encode":
        clear()
        print(logo)
        message = input("Type your message:\n").lower()
        chr_shift = int(input("Type the shift number:\n"))
        encrpyted_message = encode_message(message = message, chr_shift = chr_shift, alphabet = alphabet)
        print(f"Here is your encoded message: {encrpyted_message}")
        input("Press any key to continue...")

    # If the user wants to decode
    elif direction == "decode":
        clear()
        print(logo)
        if message == "" or chr_shift == 0:
            print("You have no prior message or character shift in the message.")
            input("Press any key to continue...")
        elif message != "" and chr_shift != 0:
            decrpyted_message = decode_message(encrypted_message = encrpyted_message, chr_shift = chr_shift, alphabet = alphabet)
            print(f"Here is your decoded message: {decrpyted_message}")
            input("Press any key to continue...")

# Exit screen
clear()
print(logo)
print("Thanks!")