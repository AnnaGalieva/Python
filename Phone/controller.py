import In
import Out
import Prog


def start():
    while True:
        print('список команд: \n1- добавить контакт \n2- удалить контакт \n3- посмотреть список контактов \n4- найти номер по имени \n5- выход \n')
        command = int(input('введите номер команды: '))
        if command == 1:
            a = In.get_name()
            b = In.get_number()
            In.phone_number(a, b)
            book = In.get_data()
            Prog.add_phone_number(book)
            print('данные успешно сохранены \n')
        elif command == 2:
            x = In.search_kontakt()
            Prog.del_phone_number(x)
            print('данные успешно сохранены \n')
        elif command == 3:
            print('телефонная книга: \n')
            Out.look_phone_book()
        elif command == 4:
            x = In.search_kontakt()
            print('данные по вашему запросу: \n')
            Out.search_view_number(x)
        elif command == 5: 
            print('выход')
            break
        else:
            print('введите коректную команду') 



