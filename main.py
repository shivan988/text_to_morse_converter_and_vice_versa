import time

import morse_code
morse_code = morse_code.morse_code_dict


def text_to_morse(letter):
        word = letter.upper()
        for letter in word:
            if letter in morse_code:
                value = morse_code[letter]
                print(value, end=" ")
            elif letter == " ":
                print("/",end=" ")
            elif letter not in morse_code:
                print(f"\nletter [{letter}] is invalid, enter valid elements")

def morse_to_text(value):
    a = value
    b = a.split(' ')
    reverse_dict = {value: key for key, value in morse_code.items()}
    for i in b:
        if i in reverse_dict:
            decoded = reverse_dict[i]
            print(decoded, end="")


run = True
while run:

    option = input('what do you want to convert\n * click 1 for text to morse code converter\n '
                   '* click 2 for morse code to text converter\n')
    if option != "x":
        if option == "1":
            text = input("Enter the text ('/' represents space):\n")
            if text != 'x':
                text_to_morse(text)
                print('\n')
            else:
                run = False

        elif option == "2":
            code = input("Enter the morse code for converting (the code should be contain space):\n")
            if code != "x":
                morse_to_text(code)
                print('\n')
            else:
                run = False
    else:
        run=False





