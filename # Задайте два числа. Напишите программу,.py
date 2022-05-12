# Задайте два числа. Напишите программу, которая найдет
#  НОК(наименьшее общее кратное) этих двух чисел

a = int(input('a= '))
b = int(input('b= '))
c = max(a, b)

#while (c % b != 0) and (c % a != 0) or (c % b == 0) and (c % a != 0) or (c % b != 0) and (c % a == 0) :
k=1
while  True:
    if ((c * k)% a ==0 and (c*k)%b==0):
        print(c*k)
        break
    k+=1

# c += 1
#print(c)    
