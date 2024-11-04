import string
import random


def generate_password(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError(
            'Password length is too short to include all the required characters')

    password = ''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    charaters = string.ascii_lowercase
    if include_uppercase:
        charaters += string.ascii_uppercase
    if include_numbers:
        charaters += string.digits
    if include_special:
        charaters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(charaters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    length = int(input('Enter password length: '))
    include_uppercase = input(
        'Include uppercase letters? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
    include_special = input(
        'Include special characters? (y/n): ').lower() == 'y'
    try:
        print(generate_password(length, include_uppercase,
                            include_numbers, include_special))
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
