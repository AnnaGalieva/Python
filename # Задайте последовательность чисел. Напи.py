# Задайте последовательность чисел. Напишите программу, которая выведет список
#  неповторяющихся 
# элементов исходной последовательности.
# from random import randint
# lst = [1, 1, 2, 3, 3, 4, 5, 5]
# def UniqueNumbers():
#     result = list(map(int, set(lst)))
#     return result
# print(UniqueNumbers())

# numbers = [3, 5, 3, 8, 8, 2, 5]
# print ('Исходная последовательность чисел')
# print (numbers)
# new_numbers = []
# for i in numbers:
#     if i not in new_numbers:
#      new_numbers.append(i)
# print ('Последовательность неповторяющихся элементов')
# print (new_numbers)

mass = [int(i) for i in input('Введите числа массива через пробел ').split()]
print(mass)

def unique_mass_num(mass):
    unique = []

    for i in mass:
        if mass.count(i) == 1:
            unique.append(i)
    return unique

print(unique_mass_num(mass))