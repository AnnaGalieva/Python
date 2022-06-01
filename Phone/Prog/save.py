def add_phone_number(book):
    path=r'Python-task\Phone\Prog\telephon_book.txt'
    with open(path, 'a') as data:
        data.write(f"{book[0]} : {book[1]} \n")