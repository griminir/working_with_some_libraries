import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANWSER = 'anwser'


def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)

    return input('Your anwser: ').upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)

    score = 0

    for index, item in enumerate(quiz, 1):
        choice = ask_question(index, item[QUESTION], item[OPTIONS])

        if choice == item[ANWSER]:
            cprint('Correct!', 'green')
            score += 1
        else:
            cprint(f'Nope! It was {item[ANWSER]}', 'red')

        print()

    print(f'Quize is over! you got {score} out of {len(quiz)} correct')


def main():
    quiz = [
        {
            QUESTION: 'What are odin\'s ravens called?',
            OPTIONS: ['A. Sad and Lonely', 'B. Huginn and Muninn', 'C. Rip and Tear', 'D. Geri and Freki'],
            ANWSER: 'B'
        },
        {
            QUESTION: 'Who is the mother of Sleipnir?',
            OPTIONS: ['A. Does not have a mother', 'B. No one knows', 'C. Frigg', 'D. Loki'],
            ANWSER: 'D'
        },
        {
            QUESTION: 'What is the end of days called in Norse mythology?',
            OPTIONS: ['A. Armageddon', 'B. Al-Qiyamah', 'C. Kali Yuga', 'D. Ragnarok'],
            ANWSER: 'D'
        },
    ]
    run_quiz(quiz)


if __name__ == '__main__':
    main()
