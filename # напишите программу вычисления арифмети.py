# напишите программу вычисления арифметического выражения заданого строкой.
# используйте операции + - / *   2*2=4  1+2*3=7  1-2*3=-5



str = input('введите пример: ')
list = [ ]
for i in str:
       list.append(i)
print(list)
for j in range(2):
    for i in range(len(list)):
        if i < len(list):
          if list[i] == '*':
            list[i]= int(list[i-1]) * int(list[i+1])
            list.pop(i-1)
            list.pop(i)
        
          elif list[i] == '/':
                list[i]= int(list[i-1]) / int(list[i+1])
                list.pop(i-1)
                list.pop(i)

        else:
            break    

    print(list) 
for j in range(2):    
    for i in range(len(list)):
        if i < len(list):
         if list[i] == '+':
            list[i]= int(list[i-1]) + int(list[i+1])
            list.pop(i-1)
            list.pop(i)
        
         elif list[i] == '-':
                list[i]= int(list[i-1]) - int(list[i+1])
                list.pop(i-1)
                list.pop(i)

        else:
            break    
    print(list)        





# expression = '23+2*12/6-9'
# print(eval(expression))

# expression = '23+2*12/6-9'
# print(eval(expression))


# my_list = '23+2*12/6-9'
# print(int(eval(my_list)))

# my_list2 = '2+22-5'
# print(int(eval(my_list2)))