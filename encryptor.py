# Author: Kevin Liu
# Date: 2021-01-28
# File Name: encryptor.py
# Description: A program that will encrypt a word with a selection of encryption methods.


def determine_choice(selection):    # Determines which encryption method is selected and runs it.
    if selection == 'A':
        input_sub()
    elif selection == 'B':
        input_caesar()
    elif selection == 'C':
        input_caesar_advanced()
    elif selection == 'D':
        input_own_alphabet()
    elif selection == 'H':    # Prints out a description of each cipher if H is inputted.
        print('')
        print('The Substitution Cipher is the most simple form of encryptor. It will simply replace all instances')
        print('of a specific letter in your word with a new letter of your choice. For example, if you were to input')
        print('the word "APPLE," and ask to replace the letter P with K, the word you get is "AKKLE."')
        print('')
        print('The Caesar Cipher is a more complicated form of the Substitution Cipher. Each letter in the word')
        print('that you encrypt will be replaced by a different letter that is a fixed number of positions down')
        print('the alphabet. You will be able to choose how many positions you want to shift by. For example,')
        print('the letter A would become D if you choose a shift of 3. Thus, if you were to input the word "APPLE"')
        print('with a shift amount of 3, the word you would get is "DSSOH."')
        print('')
        print('The Advanced Caesar Cipher follows almost the same rules as the Caesar Cipher, but the shifting')
        print('mechanism works a little different. Here, you can input a number between 1 and 5, and that will')
        print('serve as the initial shift (n) of the first letter. The second letter will be shifted down the')
        print('alphabet by n+1 positions, the third by n+2, and so on until n+5. At this point, the next letter ')
        print('will be shifted by the initial shift and the increase in shifts will start again.. So for example,')
        print('"AAAAA" with an initial shift of 3 will return "DEFGH." So, if you were to input "APPLE" with an ')
        print('initial shift of 3, the encrypted word will be "DTURL."')
        print('')
        print('THe Personal Alphabet Cipher is a completely customizable cipher. With this option, you can enter')
        print('your own unique alphabet (26 letters), and every letter in your word will be replaced by the new')
        print('letter dictated by your alphabet. For example, if your own alphabet is something like: "DJIWQD...."')
        print('then every A letter in your word will be replaced with D, B with J, C with I, etc. So, if my alphabet')
        print('is "ZXCVBNMASDFGHJKLQWERTYUIOP" and my word is "APPLE, the encrypted word would be "ZLLGB."')


def input_sub():    # Asks for the appropriate input for the Substitution Cipher.
    print('')   # Prints a message showing what cipher the user chose.
    print('==========================================')
    print('You have selected the Substitution Cipher.')
    print('==========================================')
    print('')

    text = input('Please enter the word you want to encrypt: ').lower()     # Receives word and turns it lowercase.

    while True:     # Asks for a valid single letter to be replaced until one is inputted.
        replace = input('Please enter the letter you want to replace: ').lower()
        if len(replace) == 1:
            break
        else:   # Prints an error message if an invalid letter was inputted.
            print('You did not enter a valid letter. Please enter a SINGLE letter to be replaced.')

    while True:     # Asks for a valid single letter to be replace with until one is inputted.
        new_letter = input('Please enter the replacement letter: ')
        if len(new_letter) == 1:
            break
        else:   # Prints an error message if an invalid letter was inputted.
            print('You did not enter a valid letter. Please enter a SINGLE letter to replace.')

    sub_cipher(text, replace, new_letter)   # Runs the encryption function.


def input_caesar():     # Asks for the appropriate input for the Caesar Cipher.
    print('')   # Prints a message showing what cipher the user chose.
    print('====================================')
    print('You have selected the Caesar Cipher.')
    print('====================================')
    print('')

    text = input('Please enter the word you want to encrypt: ').lower()
    shift_by = int(input('Please enter the amount of letters you want to shift by: '))

    caesar(text, shift_by)     # Runs the encryption function.


def input_caesar_advanced():    # Asks for the appropriate input for the Advanced Caesar Cipher.
    print('')   # Prints a message showing what cipher the user chose.
    print('=============================================')
    print('You have selected the Advanced Caesar Cipher.')
    print('=============================================')
    print('')

    text = input('Please enter the word you want to encrypt: ').lower()

    while True:     # Asks for a valid shift value until one is inputted.
        initial_shift = int(input('Please enter the initial amount of shifts (between 1 and 5): '))
        if 1 <= initial_shift <= 5:
            break
        else:   # Prints an error message if an invalid value was inputted.
            print('You did not enter a valid value. Please try again.')

    caesar_advanced(text, initial_shift)    # Runs the encryption function.


def input_own_alphabet():   # Asks for the appropriate input for the Personal Alphabet Cipher.
    print('')   # Prints a message showing what cipher the user chose.
    print('==============================================')
    print('You have selected the Personal Alphabet Cipher.')
    print('==============================================')
    print('')

    text = input('Please enter the word you want to encrypt: ').lower()

    while True:     # Asks for a valid alphabet until one is inputted.
        new_alphabet = input('Please enter your personal alphabet (26 letters): ').lower()
        if len(new_alphabet) == 26:
            break
        else:   # Prints an error message if an invalid alphabet was inputted.
            print('You did not enter a valid alphabet. Please try again.')

    own_alphabet(text, new_alphabet)    # Runs the encryption function.


def sub_cipher(text, replace, new_letter):  # Encrypts the word using the Substitution Cipher and prints the encrypted word.
    encrypt_text = text     # Declares variables.

    for i in range(len(text)):  # Replaces every instance of the letter to be replaced with the new letter.
        character = text[i:i+1]

        if character == replace:    # If a character in the word is the letter to be replaced, replaces that letter.
            encrypt_text = encrypt_text[0:i] + new_letter + encrypt_text[i+1:len(text)]

    print('Your encrypted word is: ' + encrypt_text)    # Prints the encrypted word.


def caesar(text, shift_by):  # Encrypts the word using the Caesar Cipher and prints the encrypted word.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'     # Declares variables.
    encrypt_text = ''

    for i in range(len(text)):  # For every letter in the word, replace with a new letter in the alphabet according to the shift.
        char_pos = alphabet.index(text[i])
        key_val = (shift_by + char_pos) % 26
        replace_with = alphabet[key_val]
        encrypt_text += replace_with

    print('Your encrypted word is: ' + encrypt_text)    # Prints the encrypted word.


def caesar_advanced(text, initial_shift):   # Encrypts the word using the Advanced Caesar Cipher and prints the encrypted word.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'     # Declares variables.
    encrypt_text = ''
    shift_by = initial_shift

    for i in range(len(text)):  # For every letter in the word, replace with a new letter in the alphabet according to the initial shift.
        char_pos = alphabet.index(text[i])
        key_val = (shift_by + char_pos) % 26
        replace_with = alphabet[key_val]
        encrypt_text += replace_with
        shift_by += 1

        if shift_by == (initial_shift + 5):  # When the shift value exceeds n+5, reset back to the original shift amount.
            shift_by = initial_shift

    print('Your encrypted word is: ' + encrypt_text)    # Prints the encrypted word.


def own_alphabet(text, new_alphabet):   # Encrypts the word using the Personal Alphabet Cipher and prints the encrypted word.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'     # Declares variables.
    encrypt_text = ''

    for i in range(len(text)):  # Replaces every letter in the word with the numerically corresponding letter in their chosen alphabet.
        char_pos = alphabet.index(text[i])
        encrypt_text += new_alphabet[char_pos]

    print('Your encrypted word is: ' + encrypt_text)    # Prints the encrypted word.


def welcome():  # Prints a welcome message and prompts a cipher selection.
    print('')
    print('Welcome to The Ultimate Encryptor! Please select the type of encryptor by typing in the letter it corresponds to.')
    print('')
    print('A) Substitution Cipher')
    print('B) Caesar Cipher')
    print('C) Advanced Caesar Cipher')
    print('D) Personal Alphabet Cipher')
    print('')
    print('If you want more info on how each cipher works, please enter "H" to receive explanations.')
    print('')

    while True:     # Asks for a valid selection until one is inputted.
        selection = input('Enter your choice here: ').upper()
        if selection == 'A' or selection == 'B' or selection == 'C' or selection == 'D' or selection == 'H':
            break
        else:   # Prints an error message if an invalid selection was inputted.
            print('You did not enter a valid selection. Please try again.')

    determine_choice(selection)     # Runs the function that determines which option was selected.


welcome()   # Starts the program by running the welcome function.
