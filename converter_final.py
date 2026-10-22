import utilities as ut

options = ["Encode text to Morse code", "Decode Morse code to text", "Exit"]

def main():
    print("----- Main Menu -----")
    ut.startChoices(options)
    while True:
        startScreen = ut.userStart("Enter one of the choices above (1-3): ", min=1, max=3)
        if startScreen == 1:
            ut.clearScreen()
            ut.encoding("Enter the text being converted into Morse code: ")
            break
        elif startScreen == 2:
            ut.clearScreen()
            ut.decoding("Enter the Morse code being converted into text: ")
            break
        else:
            break

def play_again_choice(propmt):
    ut.clearScreen()
    while True:
        player_choice = input(propmt).lower().strip()
        if player_choice == "y":
            main()
        elif player_choice == "n":
            print("Goodbye!")
            break
        else:
            print("Enter a choice from above")

if __name__ == "__main__":
    main()
    play_again_choice("Enter a 'y' to play again, or a 'n' to quit: ")