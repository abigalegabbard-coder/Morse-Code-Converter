import os

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
    """Asks the user for the text being encoded"""
    userText = input(prompt).upper().strip()
    user_words = userText.split(" ")

def decoding(prompt):
    """Asks the user for the Morse code being encoded"""
    userMorse = input(prompt)
    userMorseWords = userMorse.split("   ")


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