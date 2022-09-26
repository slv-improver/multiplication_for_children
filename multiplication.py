import random
from threading import Timer
import pyautogui


def exit():
    print('Temps dépassé')
    # autopress enter key
    pyautogui.hotkey('enter')

# define variables for the game
time_limit = int(input('Combien de temps pour répondre ? '))
table = int(input('Quel table ? '))
errors = 0
points = 0
nb_of_question = 0

while errors < 10:
    first_number = table or random.randrange(2, 11)
    second_number = random.randrange(2, 11)
    multiplication = first_number * second_number
    # start timer
    t = Timer(time_limit, exit)
    t.start()
    answer = input(f'{first_number} x {second_number} = ...')
    answer = int(answer or 0)
    # timer call callback (exit())
    t.cancel()
    nb_of_question += 1
    if answer == multiplication:
        print('Super ! Bonne réponse\n')
        points += 1
    else:
        print(f'—— Dommage ! La bonne réponse était : {multiplication}')
        errors += 1
    print(f'{errors} erreurs\n{points} bonnes réponses\n')

print(f'Le partie est terminée.\n{points}/{nb_of_question}')
