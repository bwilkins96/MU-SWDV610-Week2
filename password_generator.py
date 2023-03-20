# SWDV 610: Data Structures and Algorithms
# Function that generates a password with a passed-in length 

from random import sample

def generate_password(pass_len=8):
    choices = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    return ''.join(sample(choices, pass_len))

if __name__ == '__main__':
    p1 = generate_password()
    p2 = generate_password(12)
    
    print(p1)
    print(p2)