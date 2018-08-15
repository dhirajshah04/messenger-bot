import os
import sys
from weather import *
from google import *

welcome=(["hi", "hey", "hello"])
def classify(msg):
	msg=msg.lower().strip()

	if(msg=="help"):
		return "commonly used commands: \n1.Greeting: Hi\n2.weather city_name "
	if(msg in welcome):
		return "Hello! Whats up?"
	# if (msg.find("google")==0):
	# 	query = msg.split()[1]
	# 	return search(query, num=10)
	if (msg.find("weather")==0):
		try:
			city=msg.split()[1]
			return weather(city)
		except:
			return "please enter a valid city name"
	return "Sorry! I didn't get that"

if __name__ == '__main__':
	while (1):
		msg=raw_input("Enter Something:")
		print(classify(msg))