# import requests

# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# print(data['Valute']['USD']['Name'], data['Valute']['USD']['Value'])


from tkinter import *
 # Создать окно с графическим интерфейсом
root = Tk() 
# создать глобальные переменные
variable1 = StringVar(root)
variable2 = StringVar(root) 
# инициализировать переменные
variable1.set("currency")
variable2.set("currency")    
# Функция для выполнения преобразования в реальном времени
# из одной валюты в другую валюту
def RealTimeCurrencyConversion(): 
    import requests, json
    # код валюты
    from_currency = variable1.get()
    to_currency = variable2.get()
 
    # введите здесь свой API-ключ
    api_key = "GY6I9B2JM9AGWCJE"
     
    # Базовый URL-адрес хранения переменной base_url
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
 
    # Переменная main_url хранит полный URL
    #main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key 
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
    req_ob = requests.get(main_url) 
    # получить метод модуля запросов вернуть объект ответа
    req_ob = requests.get(main_url)
 
    # метод json возвращает формат json данные в тип данных словаря Python.     
    # результат содержит список вложенных словарей
    result = req_ob.json()
 
    # разбор необходимой информации
    Exchange_Rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
 
    #получить метод виджета Entry
    # возвращает текущий текст в виде строки из поля ввода текста.
    amount = float(Amount1_field.get())
 
    # расчет на конвертацию
    new_amount = round(amount * Exchange_Rate, 3)
 
    # Метод вставки значения в поле ввода текста.
    Amount2_field.insert(0, str(new_amount))
  
# Функция очистки поля ввода
def clear_all() :
     Amount1_field.delete(0, END)
     Amount2_field.delete(0, END) 
    #Код драйвера
if __name__ == "__main__" :
 
    # Установите цвет фона окна GUI
     root.configure(background = 'light green')
   
    # Установите конфигурацию окна
     root.geometry("500x300")
   
    # Создайте метку приветствия конвертера валют в реальном времени
     headlabel = Label(root, text = 'Добро пожаловать в конвертер валют в реальном времени',
                      fg = 'black', bg = "red")
 
    # Создайте метку «Сумма:»
     label1 = Label(root, text = "Сумма :",
                 fg = 'black', bg = 'white')
     
    # Создайте метку «Из валюты:»
     label2 = Label(root, text = "Из валюты:",
                   fg = 'black', bg = 'white')
   
    # Создайте метку «В валюту:»
     label3 = Label(root, text = "В валюту:",
                   fg = 'black', bg = 'white')
 
    # Создайте метку «Сумма конвертации:»
     label4 = Label(root, text = "Сумма конвертации:",
                   fg = 'black', bg = 'white')
 
    # метод сетки используется для размещения
    # виджеты на соответствующих позициях
    # в табличной структуре.
     headlabel.grid(row = 0, column = 1)
     label1.grid(row = 1, column = 0)
     label2.grid(row = 2, column = 0)
     label3.grid(row = 3, column = 0)
     label4.grid(row = 5, column = 0)
     
    # Создайте поле для ввода текста
    # для заполнения или ввода информации.
     Amount1_field = Entry(root)
     Amount2_field = Entry(root)
      
    # Аргумент ключевого слова ipadx задает ширину поля ввода.
     Amount1_field.grid(row = 1, column = 1, ipadx ="25")
     Amount2_field.grid(row = 5, column = 1, ipadx ="25")
 
    # список кодов валют
     CurrenyCode_list = ["USD", "RUB", "EUR"]
 
    # создать выпадающее меню с помощью функции OptionMenu
    # который принимает имя окна, переменную и варианты выбора как
    # Аргумент. используйте * перед названием списка,
    # для распаковки значений
     FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
     ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)
     
     FromCurrency_option.grid(row = 2, column = 1, ipadx = 10)
     ToCurrency_option.grid(row = 3, column = 1, ipadx = 10)
     
    # Создайте кнопку преобразования и прикрепите
    # с функцией RealTimeCurrencyExchangeRate
     button1 = Button(root, text = "Convert", bg = "red", fg = "black",
                                command = RealTimeCurrencyConversion)
     
     button1.grid(row = 4, column = 1)
 
    # Создайте кнопку «Очистить» и прикрепите
    # с функцией удаления
     button2 = Button(root, text = "Clear", bg = "red",
                     fg = "black", command = clear_all)
     button2.grid(row = 6, column = 1)
   
    # Запустите графический интерфейс
     root.mainloop()






