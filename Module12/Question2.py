import requests

city_name = input("Enter your municipality name: ")
app_key = '592a0b9b96a27876f06138b5043f410d'
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={app_key}&units=metric"

try:
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        desc = str(data['weather'][0]['description'])
        print(f"weather: ", desc)
        print("Temperature: ", str(data['main']['temp']) + "Celsius")

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")