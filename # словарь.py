# СЛОВАРЬ
# Структурировать: id, name, date
# Что делать с данными: посмотреть (по id), добавить, удалить

program = True
dictionary = {
    1:{'name1','date1'},
    2:{'name2','date2'},
    3:{'name3','date3'},
    4:{'name4','date4'},
    5:{'name5','date5'}
    }

while(program == True):
    print('1. View\n2. Add\n3. Remove\n4. Exit')

    choice = input('\n')

    if choice == '4':
        program = False
        continue

    if choice == '1':
        id = int(input('Input id: '))
        print(f'\n{dictionary[id]}\n')

    if choice == '2':
        id = int(input('\nInput id: '))
        name = input('\nInput name: ')
        date = input('\nInput date: ')
        dictionary[id] = {name, date}

    if choice == '3':
        id = int(input('Input id: '))
        del dictionary[id]


# program = True
# dictionary = {
#     1:{ 'name':'name1',
#         'date':'date1'},

#     2:{ 'name':'name2',
#         'date':'date2'},

#     3:{ 'name':'name3',
#         'date':'date3'},

#     4:{ 'name':'name4',
#         'date':'date4'},

#     5:{ 'name':'name5',
#         'date':'date5'}
#     }
# # Пока переменная program = True - программа выполняется
# while(program == True):
#     print('1. View\n2. Add\n3. Remove\n4. Exit')

#     choice = input('\n')

#     # Условие закрытия программы
#     if choice == '4':
#         program = False
#         continue

#     # Условие для просмотра товара по id
#     if choice == '1':
#         id = int(input('Input id: '))
#         print(f'\n{dictionary[id]["name"]}\n{dictionary[id]["date"]}\n')
#         continue

#     # Условие для добавления нового товара
#     if choice == '2':
#         id = int(input('\nInput id: '))
#         name = input('\nInput name: ')
#         date = input('\nInput date: ')
#         dictionary[id] = {name, date}
#     # Условие для удаления нового товара    
#     if choice == '3':
#         id = int(input('Input id: '))
#         del dictionary[id]    
