# Даны два числа. Показать большее и меньшее число
a = int(input('Введите число: '))
b = int(input('Введите число: '))
if a > b:
    print(f'{a} больше {b}')
elif a == b:
    print(f'{a} равно {b}')
else:
    print(f'{b} больше {a}')

    