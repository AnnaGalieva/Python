# по двум заданным числам проверить является ли первое квадратом второго

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
if(a == b * b) or (b == a * a):
    print(f'True')
else:
    print(f'False')