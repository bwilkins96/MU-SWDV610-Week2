# SWDV 610: Data Structures and Algorithms
# A text-based game of rock, paper, scissors against a random choice

from random import choice

def compare(c1, c2):
    choices = [c1[0], c2[0]]
    
    if c1 == c2:
        print('Tie game!')
    elif choices == ['r', 'p'] or choices == ['p', 'r']:
        print('Paper covers rock!')
    elif choices == ['r', 's'] or choices == ['s', 'r']:
        print('Rock breaks scissors')
    elif choices == ['s', 'p'] or choices == ['p', 's']:
        print('Scissors cuts paper!')

def main():
    possible = ('r', 'p', 's')

    while True:
        user_choice = input('Would you like to play rock, paper, or scissors? ').strip().lower() or 'n'
        if user_choice[0] in possible: break
        print('Invalid choice!')

    computer_choice = choice(possible)
    print(f'\nYour choice: {user_choice} | Computer choice: {computer_choice}')
    compare(user_choice, computer_choice)

if __name__ == '__main__': main()
