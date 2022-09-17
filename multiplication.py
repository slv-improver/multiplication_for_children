import random

errors = 0
while errors < 10:
    first_number = random.randrange(1, 11)
    second_number = random.randrange(1, 11)
    multiplication = first_number * second_number

    answer = input(f'{first_number} x {second_number} = ...')
    answer = int(answer)
    if answer == multiplication:
        print('Super ! Bonne réponse\n')
    else:
        print(f'—— Dommage ! La bonne réponse était : {multiplication}')
        errors += 1
    print(f'{errors} erreurs\n')

print('Le partie est terminée.')