import requests

city =  input(" enter the name of the city ")
url  = f"http://api.weatherapi.com/v1/current.json?key=4c08583d0ba447baa87180625251507&q=city"
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    print(f"The current temperature in {city} is {temperature}°C with {condition}.")
else:
    print(f"Error: Unable to retrieve weather data for {city}. Please check the city name or try again later.")
# This code retrieves the current weather data for a specified city using the WeatherAPI.
# It uses the requests library to make an HTTP GET request to the WeatherAPI endpoint,