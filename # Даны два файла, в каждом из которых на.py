# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (нет нулевых кофициентов)


# from fileinput import close


# file_1 = r'C:\Users\User\Desktop\Phyton seminar\task_5.1.txt'
# file_2 = r'C:\Users\User\Desktop\Phyton seminar\task_5.2.txt'


# first = ''
# data = open(file_1, 'r')
# for i in data: first += i
# first = first.replace(' = 0', '')
# first = first.split(' ')

# print(f'first = {first}')

# second = ''
# data = open(file_2, 'r')
# for i in data: second += i
# second = second.replace(' = 0', '')
# second = second.split(' ')
# print(f'second = {second}')
# sum = []
# for i in range(3):
#     sum.append(first[i]+second[i])
# file_3 = r'C:\Users\User\Desktop\Phyton seminar\task_5.3.txt'    
# for i in range(1,3):
#     if sum[i] > 0:
#         sum[i] = '+' + str(sum[i])
# file_3.writelines(f'{sum [0]}x*2 {sum[1]}x {sum[2]}')            
# file_3.close()

