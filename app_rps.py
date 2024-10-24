import random


# made into tuple so it can not be changed
choices = ('r', 'p', 's')
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}


def get_user_choice():
    while True:
        user_choice = input('Rock, paper or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('please pick r, p or s')

def display_choices(user_choice, computer_choice):
    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')

def determin_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
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
