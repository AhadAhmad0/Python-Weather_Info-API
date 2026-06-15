import os
import requests
import json
import pyttsx3

engine = pyttsx3.init()

API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable not set.")

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(f"The current temperature is: {w}")

engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()

