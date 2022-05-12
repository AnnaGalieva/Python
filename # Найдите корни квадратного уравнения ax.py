# Найдите корни квадратного уравнения ax2+bx+c=0 двумя способами:
# 1) c помощью математических формул нахождения корней квадратного уравнения
# 2) c помощью дополнительных библиотек пайтон
# пользователь вводит a,b,c


#d = b**2-4*a*c
from re import X


a = int(input('Введите числа a='))
b = int(input('Введите числа b='))
c = int(input('Введите числа c='))

def diskr(a, b, c):             # функц ищет дискриминант
   d = b ** 2 - 4 * a * c
   return d
def sqrt_(a, b, c):               #функц ищет корни
    d = diskr(a, b, c)
    if d > 0:
        x1 = (-b + d**0,5)/(2*a) 
        x2 = (-b - d**0,5)/(2*a)
        return x1, x2
    elif d == 0:
        x = -b/2*a
        return x
    else:
        return False  
print(sqrt_(a, b, c))                