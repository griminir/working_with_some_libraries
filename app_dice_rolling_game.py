import random

while True:
    choice = input('would you like to roll the dice? (y/n): ').lower()

    match choice:
        case 'y':
            dic1 = random.randint(1, 6)
            dic2 = random.randint(1, 6)
            print(f'[{dic1}],[{dic2}]')
        case 'n':
            print('thanks for playing!')
            break
        case _:
            print('invalid choice')
print('it was fun while it lasted')