import string
import random


def generate_password(length, include_uppercase, include_numbers, include_special):
    charaters = string.ascii_lowercase
    if include_uppercase:
        charaters += string.ascii_uppercase
    if include_numbers:
        charaters += string.digits
    if include_special:
        charaters += string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(charaters)

    return password


def main():
    length = int(input('Enter password length: '))
    include_uppercase = input(
        'Include uppercase letters? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
    include_special = input(
        'Include special characters? (y/n): ').lower() == 'y'
    print(generate_password(length, include_uppercase, include_numbers, include_special))


if __name__ == '__main__':
    main()
