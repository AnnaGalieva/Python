# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. Найдите это число.

# a = [2, 3, 4, 5, 6, 8, 9]

# for i in range(1, len(a)):
#   if a[i] - 1 != a[i - 1]:
#    print (a[i]-1)



# my_list = [x for x in range(1, 101) if (x % 10 == 3) or (x % 10 == 6)]

# print(my_list)
#какой элемент взять,где взять,при каком условии  

# txt = '1 2 4 5 '
# path = 'task_1.txt'
# with open(path, 'w') as f:
#   f.write(txt)
# with open(path, 'r') as f:
#   txt = f.read().split()
# numbers = [int(txt[i]) - 1 for i in range(len(txt)) if (int(txt[i]) - 1) != int(txt[i-1])]
# print(numbers)


a = [2, 3, 4, 5, 6, 8, 9]
result = [(a[i] - 1) for i in range(1, len(a)) if (a[i] - 1 != a[i - 1])]
print(result)

