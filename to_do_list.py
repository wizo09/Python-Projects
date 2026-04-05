tasks = []

try:
    with open('tasks.txt', 'r') as f:
        for line in f:
            name, done = line.strip().split(',')
            tasks.append({'name': name, 'done': done == 'True'})
except FileNotFoundError:
    pass

while True:
    print('''
            1. Add Task
            2. View Task
            3. Mark Task As Done 
            4. Delete Task
            5. Quit
        ''')

    user_choice = input('Choose A Menu: ')

    if user_choice == '1':
        task = input('Enter A Task: ')
        tasks.append({'name': task, 'done': False})
        print('Task Added!')

    elif user_choice == '2':
        for index, task in enumerate(tasks, 1):
            status = '✅' if task['done'] else '❌'
            print(f'{index}. {task["name"]} {status}')
        print('Viewing Task')

    elif user_choice == '3':
        try:
            task_num = int(input('Enter task number to mark as done: '))
            tasks[task_num -1]['done'] = True
            print('Marked Task As Done')
        except IndexError:
            print('Not enough tasks')
    elif user_choice == '4':
        task_num = int(input('Enter task number to delete: '))
        tasks.pop(task_num -1)
        print('Tasks Deleted!')

    else:
        with open('tasks.txt', 'w') as f:
            for task in tasks:
                f.write(f"{task['name']},{task['done']}\n")
        print('Goodbye!')
        break
