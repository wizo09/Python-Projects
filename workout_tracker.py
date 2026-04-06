from datetime import date
import json
workouts = []

try:
    with open('workouts.json', 'r') as f:
        workouts = json.load(f)
except FileNotFoundError:
    pass

def add_workout():
    name = input('Enter Name Of Exercise: ')
    num_sets = int(input('Enter Number Of Sets: '))
    num_reps = int(input('Enter Number Of Reps: '))
    today = str(date.today())
    workouts.append({'name': name, 'sets': num_sets, 'reps': num_reps, 'date': today})

def view_workouts():
    if not workouts:
        print('No Workouts Yet!')
        return
    for index, workout in enumerate(workouts, 1):
        print(f"{index}. {workout['date']} - {workout['name']}"
              f" - Sets: {workout['sets']} - Reps: {workout['reps']}")

def search_exercise():
    found = False
    exercise_name = input('What is Exercise Name: ').lower()
    for workout in workouts:
        if workout['name'].lower() == exercise_name:
            print(f"{workout['date']} - {workout['name']}"
                  f" - Sets: {workout['sets']} - Reps: {workout['reps']}")
            found = True

    if not found:
        print('Exercise Not Found!')

def show_statistics():
    if not workouts:
        print('No Workout Yet!')
        return
    total_workouts = len(workouts)
    all_sets = [workout['sets'] for workout in workouts]
    total_sets = sum(all_sets)
    exercise_count = {}
    for workout in workouts:
        name = workout['name']
        if name not in exercise_count:
            exercise_count[name] = 0
        exercise_count[name] += 1
    most_trained = max(exercise_count, key=lambda e: exercise_count[e])
    print(f"Total Workouts: {total_workouts}")
    print(f"Total Sets : {total_sets}")
    print(f"Most Trained Exercise: {most_trained}")

while True:
    print('''
            1. Add Workout
            2. View Workouts
            3. Search By Exercise
            4. Show Statistics
            5. Quit
        ''')

    user_choice = input('Enter A Menu: ')

    if user_choice == '1':
        add_workout()

    elif user_choice == '2':
        view_workouts()

    elif user_choice == '3':
        search_exercise()

    elif user_choice == '4':
        show_statistics()

    elif user_choice == '5':
        with open('workouts.json', 'w') as f:
            json.dump(workouts, f)
        print('Goodbye!')
        break

    else:
        print('Invalid Choice!')