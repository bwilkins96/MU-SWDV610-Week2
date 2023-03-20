# SWDV 610: Data Structures and Algorithms
# Function that generates a password with a passed-in length 

from random import choice
from string import ascii_letters, digits, punctuation

def generate_password(pass_len=8, chars=ascii_letters+digits+punctuation):
    return ''.join(choice(chars) for i in range(pass_len))

if __name__ == '__main__':
    length = int(input('How long would you like your password? '))
    print(generate_password(length))