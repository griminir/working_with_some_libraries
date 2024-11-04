import random
HEADS = 'heads'
TAILS = 'tails'

def pick_choice():
    while True:
        choice = input(f'Pick {HEADS} or {TAILS} (h/t): ').lower()
        if choice == 'h':
            return HEADS
        elif choice == 't':
            return TAILS
        else:
            print('please pick one of the options presented')

def cosmic_wheel(choice):
    count_heads = 0
    count_tails = 0
    while True:
        fate = random.randint(1,10)
        if fate <= 5:
            count_heads += 1
        elif fate >=6:
            count_tails += 1

        if count_heads != 0 and count_tails != 0:
            break
    return print(f'you picked {choice} and {HEADS} came up {count_heads} times and {TAILS} came up {count_tails} times')


def main():
    choice = pick_choice()
    cosmic_wheel(choice)

if __name__ == '__main__':
    main()