# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open(r'C:\Users\User\Desktop\Phyton seminar\rle1.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(my_text)
print(str_code)

# with open(r'C:\Users\User\Desktop\Phyton seminar\rle2.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)

# with open('C:\Users\User\Desktop\Phyton seminar\rle1.txt', 'r') as data:
#  text = data.read()
text = 'qwwweeqrrtyyyy'
text2 = ''
text3 = ''
count = 1
for i in range(0, len(text)-1):
    if text[i] == text[i+1]:
        count +=1
        text2 = str(count) + text[i] 
    else: 
        text2 = str(count) + text[i] 
        count = 1
        text3 += text2
text3 += text2

print(text3)    