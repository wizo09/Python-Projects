import json

students = []

try:
     # Loading
    with open('students.json', 'r') as f:
        students = json.load(f)
except FileNotFoundError:
    pass

def add_student():
    name = input('Enter Student Name: ')
    grades = []

    for i in range(3):
        grade = float(input(f'Enter grade {i+1}: '))
        grades.append(grade)

    average = sum(grades) / len(grades)
    if average >= 90:
        letter = 'A'
    elif average >= 80 and average <= 89:
        letter = 'B'
    elif average >= 70 and average <= 79:
        letter = 'C'
    elif average >= 60 and average <= 69:
        letter = 'D'
    else:
        letter = 'F'
        
    students.append({'name': name, 'grades': grades, 'average': average, 'letter': letter })
    print(f'{name} added!')

def view_students ():
    for student in students:
        print(f"{student['name']} - Average: {student['average'] :.1f} - Letter: {student['letter']}")


def search_student():
    found = False
    search_name  = input('What Is Student Name: ').lower()
    for student in students:
        if student['name'].lower() == search_name:
            print(f"{student['name']} - Average: {student['average']:.1f} - Letter: {student['letter']}")
            found = True
    if not found:
        print('Student Not Found')

def show_statistics():
    if not students:
        print('No Students Yet')
        return
    averages = [student['average'] for student in students]
    class_average = sum(averages) / len(averages)
    highest = max(students, key=lambda s: s['average'])
    lowest = min(students, key=lambda s: s['average'])
    print(f"Highest: {highest['name']} - {highest['average']:.1f}")
    print(f"Lowest: {lowest['name']} - {lowest['average']:.1f}")
    print(f"Class Average: {class_average:.1f}")




while True:
    print('''
            1. Add Student
            2. View Students
            3. Search Student
            4. Show Statistics
            5. Quit
    ''')

    user_choice = input('Choose A Menu: ')

    if user_choice == '1':
        add_student()

    elif user_choice == '2':
        view_students()

    elif user_choice == '3':
        search_student()

    elif user_choice == '4':
        show_statistics()

    elif user_choice == '5':
        # Saving
        with open('students.json', 'w') as f:
            json.dump(students, f)
        print('Goodbye..')
        break

    else:
        print('Invalid Choice')


