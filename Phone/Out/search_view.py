def search_view_number(kont):
    f = open(r'telephon_book.txt', 'r')
    Line_new = f.readlines()
    f.close()
    for line in Line_new: 
        if line.find(kont) == 0:
            print(line)