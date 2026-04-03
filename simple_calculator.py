print('''Enter An Operation 
          1. ADDITION
          2. SUBTRACTION
          3. MULTIPLICATION
          4. DIVISON
          ''')

history = []

while True:
    try:
        num1 = float(input('Input your first number: '))
        num2 = float(input('Input your second number: '))
        user_choice = int(input('Enter An Operation: '))

        if user_choice == 1:
            result = num1 + num2
            print(result)
            history.append(f'{num1} + {num2} = {result}')

        elif user_choice == 2:
            result = num1 - num2
            print(result)
            history.append(f'{num1} - {num2} = {result}')

        elif user_choice == 3:
            result = num1 * num2
            print(result)
            history.append(f'{num1} * {num2} = {result}')

        elif user_choice == 4:
            result = num1 / num2
            print(result)
            history.append(f'{num1} / {num2} = {result}')

        print('===History===')
        for item in history:
            print(item)
    except ZeroDivisionError:
        print('Cant Be Divisible By 0')

    except ValueError:
        print('Please enter a valid number')

    ask_user = input('Calculate again? (Yes/No):').lower()
    if ask_user == 'no':
        break
