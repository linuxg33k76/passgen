#!/bin/env python3

'''
CLI Password Generator
By Ben Calvert 
Date: 6/1/2021
'''

import random


# Get user input on length 

def get_input():
    while True: 
        x = input('Please enter length of password: ')
        try:
            if int(x) and int(x) > 0:
                return int(x)
        except:
            print('Invalid Input; Try again!')


def main():

    # Set Constants 
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdeefghijklmnopqrstuvwxyz'
    NUMBER = '0123456789'
    SYMBOLS = '!@#$%&*.?'

    # Combine all Constants
    all_values = UPPER + LOWER + NUMBER + SYMBOLS

    # Get password length from the user; pass length of all available characters
    password_length = get_input()

    # Find a random sample and generate password of specified length - values can repeat
    password_array = []
    for i in range(password_length):
        # Creates an array of one value
        value = random.sample(all_values,1)
        # Add value of array above to a new array
        password_array.append(value[0])

    # make the array a string
    password = ''.join([str(character) for character in password_array])

    # Print generated password
    print('\n\t' + password + '\n')


if __name__ == '__main__':

    main()
