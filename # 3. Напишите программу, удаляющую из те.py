# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_str = 'Напишите прогабврамму, удабваляющую из текста все слова, содержащие'
# my_str = my_str.split(' ')
# res = ' '
# for word in my_str:
#     if word.find('абв') == -1:
#        res += word + ' '
# print(res)

my_str = 'Напишите прогабврамму, удабваляющую из текста все слова, содержащие'

def del_some_words(my_str):
    my_str = list(filter(lambda x: 'абв' not in x, my_str.split()))
    return " ".join(my_str)

my_str = del_some_words(my_str)
print(my_str)
