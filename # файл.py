# файл записать файл и считать
from importlib.resources import path
from unittest.mock import patch


file_name = 'test.txt'
my_dict = {
    1: 'One',
    2: 'Two'
}
# data = open('test.txt', 'w') # открывает файл для использования
# for i in my_dict:            # получаем ключи        
#     data.write(my_dict[i])   # запишет значение в файл
#     data.write(' ')          # через пробел 
# data.close()       
# path = 'test.txt'           # путь к файлу через переменную
# with open(patch, 'r') as data: # режим чтения
#     for line in data:
#         print(line, end='')    




# file = open('test.txt', 'w')
# for i in my_dict:
#     file.write(my_dict[i])
#     file.write(' ')
# file.close()
# file = open('test.txt','r')
# for i in file:
#     print(i)
# file.close() 


# file = open('test.txt','r')
# all_info = file.read(5)   # считали 5 символов
# print(all_info)
# file.close()       


file = open('test.txt','a')
file.write('New')     # new добавили в конец строки, #(new\n)
file.close()
