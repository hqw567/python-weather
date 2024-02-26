import requests


def get_weather(city):
    res = requests.get(f"https://api.oioweb.cn/api/weather/weather?city_name={city}")
    return res.json()
