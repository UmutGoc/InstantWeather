import requests

# Instant Weather App
# Weather Data https://openweathermap.org
# Create your account on site to take your apikey

cityName = "Istanbul"
APIkey = "YourApiKey"

def get_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    return data

data = get_weather_data()

def create_weather_report(data):
    k = data["main"]["temp"] #temperature as Kelvin
    c = int(k-273.15) #type conversion -- Kelvin to °C
    felTemperatureAsKelvin = data["main"]["feels_like"]
    felTemperature = int(felTemperatureAsKelvin-273.15) #type conversion -- Kelvin to °C

    report = "Weather Report:\n"
    city = f"{cityName}"
    report += f"City:{city}\n"
    temperature = c
    report += f"Temperature: {temperature}°C\n"
    humidity = data["main"]["humidity"]
    report += f"Humidity: {humidity}%\n"
    wind_speed = data["wind"]["speed"]
    report += f"Wind Speed: {wind_speed} m/s\n"
    report += f"Felt Temperature: {felTemperature}°C\n"
    description = data["weather"][0]["description"]
    description = description.upper()
    report += f"Weather: {description}\n"
    return report




report = create_weather_report(data)
print(report)
#print(data) to see all data about city











