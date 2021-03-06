import requests
from datetime import datetime
import pytz
import os, sys, stat

IST = pytz.timezone('Asia/Kolkata')

api_key = 'ff1ea325d9615c351e65ddabbd6e3757'
loc = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+"{}".format(loc.lower())+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temperature = ((api_data['main']['temp']) - 273.15)
weather_description = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now(IST).strftime("%d %b %Y | %I:%M:%S %p")

print ("\n"+"Weather informtion for {} | {}".format(loc.title(), date_time)+"\n")

print ("Current temperature : {:.2f} degree C".format(temperature)) 
print ("Weather description :",weather_description)
print ("Humidity            :",humidity, '%')
print ("Wind speed          :",wind_speed ,'kmph')

str1 = "Current temperature : " + str("{:.2f}".format(temperature)) + " degree C"
str2 = "\nWeather description : " + str(weather_description)
str3 = "\nHumidity            : " + str(humidity) + '%'
str4 = "\nWind speed          : " + str(wind_speed) + 'kmph'

with open('weatherinformation.txt','w') as f:
    f.writelines(str1+str2+str3+str4)
