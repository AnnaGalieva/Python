# Подсчитать сумму цифр в вещественном числе
# import random
# n = random.randint(1, 100)
# num = int(input('Введите число: '))
# sum = 0
# while num != 0:
#     sum = sum + num % 10
#     num = num // 10
# print(f'сумма цифр числа равна:', sum) 


import random
num = random.randint(300, 9999)
print(num)
result = 0

while num != 0:
    result += num % 10
    num //= 10

print(result)
