import random
from termcolor import cprint

quiz = [
    {
        'question': 'What are odin\'s ravens called?',
        'options': ['A. Sad and Lonely', 'B. Huginn and Muninn', 'C. Rip and Tear', 'D. Geri and Freki'],
        'anwser': 'B'
    },
    {
        'question': 'Who is the mother of Sleipnir?',
        'options': ['A. Does not have a mother', 'B. No one knows', 'C. Frigg', 'D. Loki'],
        'anwser': 'D'
    },
    {
        'question': 'What is the end of days called in Norse mythology?',
        'options': ['A. Armageddon', 'B. Al-Qiyamah', 'C. Kali Yuga', 'D. Ragnarok'],
        'anwser': 'D'
    },
]

random.shuffle(quiz)
score = 0

for index, item in enumerate(quiz, 1):
    print(f'Question {index}: {item['question']}')
    for option in item['options']:
        print(option)
    
    choice = input('Your anwser:  ').upper().strip()

    if choice == item['anwser']:
        cprint('Correct!', 'green')
        score += 1
    else:
        cprint(f'Nope! It was {item["anwser"]}', 'red')
    
    print()

print(f'Quize is over! you got {score} out of {len(quiz)} correct')