# Вычислить число Пи c заданной точностью d
# Пример:при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
import numbers


# d = '0.001'
# def Number(number2):
#     count = len(d) - 2
#     result = float(number2)
#     return round(result, count)
# print(Number(3.141))


import math

d = int(input('введите точность(кол=во знаков после запятой)числа Пи:'  ))
ress = round(math.pi,d)
print(ress)

# k = 1
# x = 0
# for k in range(1, 1000000):
#     x = x+4*((-1)**(k+1))/(2*k-1)
# #print(x)
# print(round(x, 4))

