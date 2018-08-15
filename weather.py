import requests
import pyowm


def weather(city):
	city=str(city)
	site='http://api.openweathermap.org/data/2.5/weather?APPID=[GET YOUR OPEN WEATHER API KEY]&q='+str(city)
	r = requests.get(site)
	p=r.json()
	text=""

	text+=str("City: "+str(p['name'])+str(" \nCountry: ")+str(p['sys']['country'])+"\n");
	text+=("Temp: "+str(float(p['main']['temp'])-273.15)+ chr(176)+"C"+"\n");
	text+=("Humidity: "+str(p['main']['humidity'])+"\n");
	
	return (text)