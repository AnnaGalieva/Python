# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# n = int(input('Введите число n: '))
# list = []
# d = 2
# m = n # Запомним исходное число
# while d * d <= n:
#         if n % d == 0:
#             list.append(d)
#             n//=d
#         else:
#             d += 1
# list.append(n) # Добавим последнеё простое число
# print('{} = {}' .format(m, list)) # Выводим исходное число и все простые множители.
n = int(input('Введите число n: '))
list_simple = []
simple = 2
while n > 1:
    if n % simple == 0:
        list_simple.append(simple)
        n = n/simple
    else:
        simple += 1
print(list_simple)

# n = int(input())
# lst = []
# for i in range(2,int(n**0.5)+1):
# while n%i == 0:
# lst.append(i)
# n /= i
# if n == 1:
# break
# print(lst)


