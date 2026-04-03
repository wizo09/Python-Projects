import random

high_score = None

while True:
    attempt = 0
    print("""Pick A Difficulty
        Easy → 1 to 50
        Medium → 1 to 100
        Hard → 1 to 200:
    """)
    difficulty = input('Enter a difficulty level: ').lower()

    if difficulty == 'easy':
        computer_choice = random.randint(1, 50)
        upper = 50
    elif difficulty == 'medium':
        computer_choice = random.randint(1, 100)
        upper = 100
    elif difficulty == 'hard':
        computer_choice = random.randint(1, 200)
        upper = 200
    else:
        print('Invalid difficulty, defaulting to Medium')
        computer_choice = random.randint(1, 100)
        upper = 100


    while True:
        try:
            user_guess = int(input(f'Guess a number between 1-{upper}: '))
        except ValueError:
            print('Please enter a valid number')
            continue
        attempt += 1

        if user_guess > computer_choice:
            print('Too High')
        elif user_guess < computer_choice:
            print('Too Low')
        else:
            print('Correct!')
            print(f'You did {attempt} attempts')
            break

    if high_score is None or attempt < high_score:
        high_score = attempt
        print(f'New high score: {high_score} attempts!')
    else:
        print(f'High score is still: {high_score} attempts')

    play_again = input('Play Again? yes/no: ')
    if play_again == 'no':
        break




