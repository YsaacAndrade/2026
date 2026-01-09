import requests
import sys
import os

### GET THE API_KEY ON https://openweathermap.org ###

class Weather:
    def __init__(self, city):
        self.city = city

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city.strip()


def main():
    print(correct_value(confirm_request(get_request(get_url(get_clean_input())))))


def get_clean_input():
    while True:
        
        know = Weather(input("What's the city name? "))
        if len(know.city) <= 0 or len(know.city) > 58 or know.city.isnumeric():
            continue

        else:
            break
    return know.city


def get_url(city_name):
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.environ.get('API_KEY')}"


def get_request(url):
    return requests.get(url)


def confirm_request(request):
    if request.status_code == 200:
        return request.json()

    else:
        return sys.exit("Something wrong happened. Please, verify if your API_KEY is valid and try again.")

def correct_value(confirmed_request):
    request = confirmed_request


    country = request["sys"]["country"]
    city = request["name"]


    climate_main = request["weather"][0]["main"]
    climate_description = request["weather"][0]["description"]


    temperature = request["main"]["temp"]
    temperature = float(temperature)


    calculate_for_celsius = temperature - 273.15
    calculate_for_fahrenheit = calculate_for_celsius * 1.8 + 32


    climate = f"Country: {country}\nCity: {city}\nClimate: {climate_main}\nDescription: {climate_description}\n°C {calculate_for_celsius:,.1f} | °F {calculate_for_fahrenheit:,.1f}"

    return climate


if __name__ == "__main__":

    main()
