import random


ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', 's': '✂️', 'p': '📃'}
# made into tuple so it can not be changed as basing it on the dictonary keys so if emojis key changes so does the choices
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input(f'Rock, paper or scissors? ({ROCK}/{PAPER}/{SCISSORS}): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print(f'please pick {ROCK}, {PAPER} or {SCISSORS}')

def display_choices(user_choice, computer_choice):
    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')

def determin_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print('You win!')
    else:
        print('You lose!')

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determin_winner(user_choice, computer_choice)

        should_continue = input('do you wanna continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()
