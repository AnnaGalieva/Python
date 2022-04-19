# найти максимальное из трех
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if a > b and a > c:
    print(f'max: {a}')
elif b > a and b > c:
    print(f'max: {b}')
else:
    print(f'max: {c}')
