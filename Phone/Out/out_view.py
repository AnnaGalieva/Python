def look_phone_book():
    data = open(r'telephon_book.txt', 'r')
    for line in data:
        print(line)
    data.close()