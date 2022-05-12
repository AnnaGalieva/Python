# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 1 до 100, можно создать свой генератор случайных 
# чисел или использовать готовый) многочлена и записать в файл многочлен 
# степени k.
#Пример: k=2 => 2*x² + 4*x + 5 = 0
# def Polynomial(k):
#     str = []    
#     import random
#     k = random.randint(1, 4)
#     for i in range(0, k + 1):
#         if i >= 2:
#             str.append(f'{k}*x^{i} + ')
#         elif i == 1:
#             str.append(f'{k}*x + ')
#         elif i == 0:
#             str.append(f'{k} = 0')
#     stroka = str[::-1]                
#     result = ''.join(stroka)
#     with open("test2.txt", "a") as data:
#         data.write(result + '\n')
# Polynomial(2)


# def Polynomial(k):
#     str = []    

#     k = 2
#     str.append(f"{2}*x^{k} + {4}*x+{5} = {0}")
        
#     stroka = str[::-1]                
#     result = ''.join(stroka)
#     with open("test2.txt", "a") as data:
#         data.write(result + '\n')
# Polynomial(5)


#import random

## from useFulFutires.IsNumber import isNumber

# k = isNumber()
# count = k
# randomKoef = [random.randint(0, 100) for i in range(k+1)]

# resultT = ""
# for i in range(k):
#     if i == k-1:
#         resultT += str(randomKoef[i]) + '*x + '
#         resultT += str(randomKoef[i+1])
#         break
#     else:
#         resultT += str(randomKoef[i]) + f'*x**{count} + '
#     count -= 1

# resultT += ' = 0'
# print(resultT)
# path = 'randomCoefPolynom.txt'

# with open(path, 'w') as d:
#     d.write(resultT)




# import random

# k = 9
# file_name = 'res_dz2_4.txt'
# with open(file_name, 'w') as data:
# for i in range(k, 0, -1):
# x = random.randint(1,100)
# if i > 1:
# data.write(f'{x}*x**{i} + ')
# else:
# data.write(f'{x}*x + {random.randint(1,100)} = 0')


from sympy import parse_expr, symbols
path1 = 'Polynom1.txt'
path2 = 'Polynom2.txt'
with open(path1, 'r') as file:
   mNumber = file.read()
with open(path2, 'r') as file:
   mNumber2 = file.read()
print(f'({mNumber}) + ({mNumber2})')
x = symbols('x')
mNumber = parse_expr(mNumber.replace('^', '**'), local_dict={'x': x})
mNumber2 = parse_expr(mNumber2.replace('^', '**'), local_dict={'x': x})
sumMNumbers = mNumber + mNumber2
print(f'({mNumber}) + ({mNumber2})')
print(f'{mNumber} + {mNumber2}')
print(sumMNumbers)



# path1 = 'Polynom1.txt'
# path2 = 'Polynom2.txt'
# with open(path1, 'r') as file:
# mNumber = file.read()
# with open(path2, 'r') as file:
# mNumber2 = file.read()
# print(f'({mNumber}) + ({mNumber2})')
# x = symbols('x')
# mNumber = parse_expr(mNumber.replace('^', '**'), local_dict={'x': x})
# mNumber2 = parse_expr(mNumber2.replace('^', '**'), local_dict={'x': x})
# sumMNumbers = mNumber + mNumber2
# print(f'({mNumber}) + ({mNumber2})')
# print(f'{mNumber} + {mNumber2}')
# print(sumMNumbers)







