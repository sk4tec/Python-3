import requests
import json

Apikey = "062487fc4b8c1f4cf2c6e584511b54ef"
url = f"https://api.openweathermap.org/data/2.5/weather?lat=51.4562&lon=-0.97113&appid={Apikey}"
response = requests.get(url)

if response.ok:
	data = response.json()
	print(json.dumps(data, indent=2)) # converts to a nicely formatted string
else:
	print(f"Request failed: {response.status_code}")
	
print(f"Weather in {data['name'] }:")
print(f"Description: {data['weather'][0]['description']}")
print(f"Temperature (C): {round(data['main']['temp'] - 273.15, 2)}")