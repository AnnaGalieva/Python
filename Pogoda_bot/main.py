import requests
import datetime
from config import open_weather_token
from pprint import pprint

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)
        city = data["name"]
        cure_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"***{datetime.datetime.now().strftime('%y-%m-%d %H:%M')}***\n"
            f"погода в городе: {city}\nТемпература: {cure_weather}C\n"
              f"влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nВетер: {wind}м/с\n"
              f"восход солнца: {sunrise_timestamp}\nзакат солнца: {sunset_timestamp}"
        )
        
        
    except Exception as ex:
        print(ex)
        print('проверьте название города')
def main():
    city = input('введите город: ')
    get_weather(city, open_weather_token)
    

if __name__=='__main__':
    main()
