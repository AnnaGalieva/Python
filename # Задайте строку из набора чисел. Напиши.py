# Задайте строку из набора чисел. Напишите программу, которая покажет
#  большее и меньшее число. В качестве символа-разделителя использовать пробел.
#file_name = 'task1.txt'

# path = 'task1.txt'
# with open(path, 'r') as data:       
#      list = data.read()
# print(list)                     # считали строку
file_name = r'C:\Users\User\Desktop\Phyton seminar\task1.txt'
data = open(file_name, 'r')
dataRead = data.read().split(' ')
data.close()
for i in range(0, len(dataRead)):
    dataRead[i] = int(dataRead[i])
print(dataRead)
print(f'минимальное: {min(dataRead)}, максимальное: {max(dataRead)}')
