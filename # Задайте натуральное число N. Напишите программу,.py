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
# print('{} = {}' .format(m, list)) # Выводим исходное число и все простые 
# множители.


# n = int(input('Введите число n: '))
# list_simple = []
# simple = 2
# while n > 1:
#     if n % simple == 0:
#         list_simple.append(simple)
#         n = n/simple
#     else:
#         simple += 1
# print(list_simple)

# n = int(input())
# lst = []
# for i in range(2,int(n**0.5)+1):
# while n%i == 0:
# lst.append(i)
# n /= i
# if n == 1:
# break
# print(lst)

# list = []
# number = int(input('введите число n: '))
# for n in range(2, number):
#     if number % n == 0:
#         list.append(n)
# print(list)  
# 
#       
n = int(input('Задайте натуральное число N: '))
n1 = n
res = []
# numbers = []
# for i in range (2, int(math.sqrt(n))+1):
# while (n1 % i == 0):
# numbers.append(i)
# n1 //= i
# if (n1 != 1):
# numbers.append(n1)
# print(f'Простые множители числа {n}: ', numbers)


def func(i):
  global n1
  global res
  a = []
  while (n1 % i == 0):
      n1 //= i
      res.append(i)
list(map(func, [i for i in range(2, int(n**0.5)+1)]))
if (n1 != 1):
   res.append(n1)

print(res)


    