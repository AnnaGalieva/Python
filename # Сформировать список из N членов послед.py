# Сформировать список из N членов последовательности.
#  Список записать в файл "number_list.txt"(в одну строку- одно число)
n = int(input('Введите число: '))
def get_degree(n):
    return [((-3)**i) for i in range(n)]
print (get_degree(n))
    