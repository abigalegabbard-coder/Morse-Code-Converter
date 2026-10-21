import utilities as ut
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
options = ["Encode text to Morse code", "Decode Morse code to text", "Exit"]

def main():
    print("----- Main Menu -----")
    ut.startChoices(options)
    while True:
        startScreen = ut.userStart("Enter one of the choices above (1-3): ", min=1, max=3)
        if startScreen == 1:
            ut.clearScreen()
            ut.encoding("Enter the text being converted into Morse code: ")
        elif startScreen == 2:
            ut.clearScreen()
            ut.decoding("Enter the Morse code being converted into text: ")
        else:
            break


if __name__ == "__main__":
    main()