import os

MORSE_CODE_DICT = {"A":". -", "B":"- . . .", "C": "- . - .", "D":"- . .", "E":".",
                   "F":". . - .", "G":"- - .", "H":". . . .", "I":". .", "J":". - - -",
                   "K":"- . -", "L":". - . .", "M":"- -", "N":"- .", "O":"- - -",
                   "P":". - - .", "Q":"- - . -", "R":". - .", "S":". . .",
                   "T":"-", "U":". . -", "V":". . . -", "W":". - -",
                   "X":"- . . -", "Y":"- . - -", "Z":"- - . .", "1":". - - - -",
                   "2":". . - - -", "3":". . . - -", "4":". . . . -", "5":". . . . .",
                   "6":"- . . . .", "7":"- - . . .", "8":"- - - . .",
                   "9":"- - - - .", "0":"- - - - -"
                   }

def startChoices(items):
    """Prints the choices for the user to pick from"""
    if len(items) == 0:
        print("No items to display.")
    else:
        number = 1
        for item in items:
            print(f"{number}. {item}")
            number += 1
def userStart(prompt, min=1, max=3):
    """Asks the user for a number 1-3 based off of startChoices"""
    while True:
        userStartChoice = input(prompt)
        if not userStartChoice.isnumeric() or not min <= int(userStartChoice) <= max:
            print("Enter something from above")
        else:
            return int(userStartChoice)

def encoding(prompt):
    """Converts the user's text to Morse code"""
    userText = input(prompt).upper().strip()
    morse_words = []
    for words in userText.split():
        morse_letters = []
        for character in words:
            if character in MORSE_CODE_DICT:
                code = MORSE_CODE_DICT[character].replace(" ", "")
                morse_letters.append(code)
            else:
                print(f"Warning! Character '{character}' not reconized. Skipped.")
        morse_words.append(" ".join(morse_letters))
    print("Encoded string:", "   ".join(morse_words))
def decoding(prompt):
    """Converts the user's Morse code to text"""
    morse_to_text = {value.replace(" ", ""): key for key, value in MORSE_CODE_DICT.items()}
    userMorse = input(prompt).strip()
    decoded_words = []
    for word in userMorse.split("   "):
        decoded_letters = []
        for code in word.split():
            if code in morse_to_text:
                decoded_letters.append(morse_to_text[code])
            else:
                print(f"Warning! Unknown sequence reconinzed! Skipped.")
        decoded_words.append("".join(decoded_letters))
    print("Decoded text:", " ".join(decoded_words))
    
def clearScreen():
    """Clear the window's console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    startChoices([])
    userStart("Enter one of the choices above (1-3): ", min=1, max=3)
    clearScreen()
    encoding("Enter the text being converted into Morse code: ")
    decoding("Enter the Morse code being converted into text: ")

if __name__ == "__main__":
    main()