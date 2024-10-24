import random
# generate a random number
# loop
#   ask the user to make a guess
#   if not a valid number
#       print an error
#   if number < guess
#        print too low
#   if number > guess
#       print too high
#   else
#       print well done
#       end loop

right_number = random.randint(1, 100)

while True:
    try:
        guess = int(input('what do you think the number is between (1-100)?: '))

        if guess < right_number:
            print('too low')
        elif guess > right_number:
            print('too high')
        else:
            print(f'well done correct number was {right_number}')
            break
    except ValueError:
        print('please enter a valid number')
