# City, Time, Temprature, Condition
import requests

def get_weather(city, units='metric', api_key='1bfcf32e767d80e127e0bd0e80530537'):
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units={units}'

  r = requests.get(url)
  content = r.json()
  with open(f'weather_{city}.txt', 'a') as file:
    for dicty in content['list']:
      file.write(f"{city} | {dicty['dt_txt']} | {dicty['main']['temp']} | {dicty['weather'][0]['description']}\n")

get_weather(city='Rehovot')