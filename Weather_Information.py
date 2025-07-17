import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=f370a9c985d442ff953114109252806&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(f"The current temperature is: {w}")

engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()




