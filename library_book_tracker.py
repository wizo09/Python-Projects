import json

books = []

try:
     # Loading
    with open('books.json', 'r') as f:
        books = json.load(f)
except FileNotFoundError:
    pass

def add_book():
    book_title = input('Enter A Book: ')
    author_name = input("Enter Author's Name: ")
    year_published = int(input('Enter Year Published: '))
    books.append({'title': book_title, 'name': author_name, 'year': year_published, 'read': False})


def view_books():
    if not books:
        print('No Books Yet!')
        return
    for index, book in enumerate(books, 1):
        status = '✅' if book['read'] else '❌'
        print(f"{index}. {book['title']} - {book['name']} - {book['year']} - {status}")

def mark_as_read():
    if not books:
        print('No Books Yet!')
        return
    view_books()
    try:
        read_num = int(input('Enter A Book To Mark As Read: '))
        books[read_num -1]['read'] = True
        print('Marked Book As Read')
    except IndexError:
        print('Not Enough Books!')


def search_author():
    found = False
    search_name = input("What Is Author's Name: ").lower()
    for book in books:
        if book['name'].lower() == search_name:
            print(f"{book['title']} - {book['name']} - {book['year']} ")
            found =  True
    if not found:
        print('Author Not Found ')

def show_statistics():
    if not books:
        print('No Books Yet!')
        return
    total_books = len(books)
    books_read = [book for book in books if book['read'] == True]
    books_unread = [book for book in books if book['read'] == False]
    percentage_read = round(len(books_read) / total_books * 100, 1)
    print(f"Total Books: {total_books}")
    print(f"Books Read: {len(books_read)}")
    print(f"Books Unread: {len(books_unread)}")
    print(f"Percentage Read: {percentage_read}%")


while True:
    print('''
        1. Add Book
        2. View Books
        3. Mark As Read
        4. Search By Author
        5. Show Statistics
        6. Quit
    ''')

    user_choice = input('Choose A Menu: ')

    if user_choice == '1':
        add_book()

    elif user_choice == '2':
        view_books()

    elif user_choice == '3':
        mark_as_read()

    elif user_choice == '4':
        search_author()

    elif user_choice == '5':
        show_statistics()

    elif user_choice == '6':
        with open('books.json', 'w') as f:
            json.dump(books, f)
        print('Goodbye..')
        break

    else:
        print('Invalid Choice')