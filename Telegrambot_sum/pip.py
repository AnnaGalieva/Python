# import telebot

# # Создаем экземпляр бота
# bot = telebot.TeleBot('5522933104:AAFGHQKez5rXdVLvyH08ZaeWv0shqfbBiaE')
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#   bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)    



import telebot
from telebot import types
import re #Эта библиотека с текстом работать. 

bot = telebot.TeleBot("5522933104:AAFGHQKez5rXdVLvyH08ZaeWv0shqfbBiaE") 

@bot.message_handler(content_types=['text']) #Срабатывание на text
def start(message): #Начало
  if message.text.lower() == 'вычисли сумму чисел' or message.text.lower() == '/sum':#Команда для начала. message.text - получаемый текст. lower(), значит не учитывается регистр, т.е. и /SUM и /SuM будет считаться за один и тот же текст
    bot.send_message(message.from_user.id, 'Хорошо. Введи два числа которые ты хочешь суммировать. К примеру "1 и 5".')
    bot.register_next_step_handler(message, sumcalc)#"Перенаправляет" на след.функцию
  else:
    bot.send_message(message.from_user.id, 'Введи /sum, или напиши "Вычисли сумму чисел", чтобы продолжить.')

def sumcalc(message):#После "перенаправления" функция сработает, лишь после получения message
  try: #проверки каких-то действий. И в случае ошибки, программа выполнит заданные в except действие.
    number1, number2 = re.split(' и ', message.text, maxsplit = 1)#Разделяет полученный текст по слову " и "
    try:
      number1 = int(number1) #Проверка "числа ли?" 
      try:
        number2 = int(number2)
        bot.send_message(message.from_user.id, 'Сумма двух введённых чисел равна:  ' + str(number1 + number2))
      except Exception:
        bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\nВы ввели не число. /sum - Чтоб повторить сначала.')
    except Exception:
      bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\nВы ввели не число. /sum - Чтоб повторить сначала.')
  except Exception:
    bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число *и* число*"*. /sum - Чтоб повторить сначала.', parse_mode= 'Markdown')

bot.polling( none_stop = True, interval=0 )#Чтоб программа не закрывалась никогда

