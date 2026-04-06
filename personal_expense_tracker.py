import json

expenses = []

try:
    with open('expenses.json', 'r') as f:
        expenses = json.load(f)

except FileNotFoundError:
    pass

def add_expense():
    expense_name = input("What's The Expense Name?: ")
    expense_amount = float(input("What's The Amount?: "))
    expense_category = input("What's The Category?: ")
    expenses.append({'name': expense_name, 'amount': expense_amount,
                     'category': expense_category})
    print('Your Item Has Been Succesfully Added!')

def view_expense():
    if not expenses:
        print('No Expenses Yet!')
        return

    for index, expense in enumerate(expenses, 1):
        print(f"{index}. {expense['name']} - {expense['category']}"
              f" - ${expense['amount']:.2f}")

def view_summary():
    if not expenses:
        print('No Expenses Yet!')
        return
    amounts = [expense['amount'] for expense in expenses]
    total = sum(amounts)
    most_expensive = max(expenses, key=lambda e: e['amount'])
    cheapest = min(expenses, key=lambda e: e['amount'])

    print(f"Most Expensive: {most_expensive['name']} - {most_expensive['amount']:.2f}")
    print(f"Cheapest: {cheapest['name']} - {cheapest['amount']:.2f}")
    print(f"Total Spent: ${total:.2f}")

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense['amount']

    top_category = max(category_totals, key=lambda c: category_totals[c])
    print(f"Most Spent Category: {top_category} - ${category_totals[top_category]:.2f}")

while True:
    print('''
    1. Add Expense
    2. View Expenses
    3. View Summary
    4. Quit
''')
    user_choice = input('Choose A Menu: ')

    if user_choice == '1':
        add_expense()

    elif user_choice == '2':
        view_expense()

    elif user_choice == '3':
        view_summary()

    elif user_choice == '4':
        with open('expenses.json', 'w') as f:
            json.dump(expenses, f)
        print('Goodbye!')
        break

    else:
        print('Invalid Choice!')