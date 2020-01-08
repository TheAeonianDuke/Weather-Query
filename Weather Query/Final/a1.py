# Roll No.: 2018211
# Name: Abhishek Pratap Singh
# Section: B
# Group: 4

import urllib.request
import urllib.parse
import datetime
import string
import requests

#location_1 = input("Enter City: ")
#location = location_1.title()
#API_key = input("Enter API: ")
#n= int(input('Enter day from the the current day: '))
#t= input("Enter time: ")

def weather_response(location, API_key):
	main_url= 'http://api.openweathermap.org/data/2.5/forecast?'
	fin_url = main_url + urllib.parse.urlencode({'q':location , 'APPID' : '5037fc7fbdffa8b55a9ea3820f12bf43'})
	#print(fin_url)
	response = urllib.request.urlopen(fin_url)
	finresp = response.read()
	json=str(finresp)
	#print(json) 
	return json
	

def has_error(location,json):
	erro_str ='"name":"' + str(location) + '"'
	if (erro_str not in json):	
		#print('Wrong City!')
		return True
	else:
		return None	

#has_error(location,json)


def get_temperature (json, n=0, t="03:00:00"):
	#n= int(input('Enter day from the the current day: '))
	n=int(n)
	now = datetime.datetime.today()
	now = now + datetime.timedelta(days=n)
	new_date = now.strftime('%Y-%m-%d')
	#t= input("Enter time: ")

	timestamp= str(new_date) + " " + str (t) 

	#print(timestamp)
	
	#print(type(json))
	dt_txt= json.find('"dt_txt"')

	first_date=json[dt_txt+10:dt_txt+20]
	
	'''if new_date!=first_date:	

		print("System Current Time and City Current Time does not match! ")
		confirm= str(input("Do you want to append 'n'?"))

		if confirm=="yes" or confirm=="Yes" or confirm=="y" or confirm=="Y":
			n= int(input('Enter day from the the current day: '))
		now = now + datetime.timedelta(days=n) - datetime.timedelta(days=1)		
		new_date = now.strftime('%Y-%m-%d')	
		first_time=json[dt_txt+21:dt_txt+29]'''
	

	global fin_time
	fin_time=(json.index(timestamp))
	x=json.rfind('"temp":', 0, int(fin_time))
	finder=json[x+7:x+18]
	comma=json.find(",", int(x)+7, int(x)+18)

	new_finder=float(json[x+7:comma])
		
	#print("Temperature: ", new_finder)
	return new_finder


#get_temperature(json, n=0)	

def get_humidity(json, n=0, t="03:00:00"):
	n=int(n)
	now = datetime.datetime.today()
	now = now + datetime.timedelta(days=n)
	new_date = now.strftime('%Y-%m-%d')
	#t= input("Enter time: ")

	timestamp= str(new_date) + " " + str (t) 
	fin_time=(json.index(timestamp))
	x=json.rfind('"humidity":', 0, int(fin_time))
	finder=json[x+11:x+17]
	comma=json.find(",", int(x)+11, int(x)+17)
	new_finder=float(json[x+11:comma])		
	#print("Humidity: ", new_finder)
	return new_finder

#get_humidity(json, n=0)	

def get_pressure(json, n=0, t="03:00:00"):
	n=int(n)
	now = datetime.datetime.today()
	now = now + datetime.timedelta(days=n)
	new_date = now.strftime('%Y-%m-%d')
	#t= input("Enter time: ")

	timestamp= str(new_date) + " " + str (t) 
	fin_time=(json.index(timestamp))
	x=json.rfind('"pressure":', 0, int(fin_time))
	finder=json[x+11:x+21]
	comma=json.find(",", int(x)+11, int(x)+21)
	new_finder=float(json[x+11:comma])
	#print("Pressure: ", new_finder)
	return new_finder
#get_pressure(json, n=0)	

def get_wind(json, n=0, t="03:00:00"):
	n=int(n)
	now = datetime.datetime.today()
	now = now + datetime.timedelta(days=n)
	new_date = now.strftime('%Y-%m-%d')
	#t= input("Enter time: ")

	timestamp= str(new_date) + " " + str (t) 
	fin_time=(json.index(timestamp))
	x=json.rfind('"speed":', 0, int(fin_time))
	finder=json[x+8:x+16]
	comma=json.find(",", int(x)+8, int(x)+16)
	new_finder=float(json[x+8:comma])
	#print("Wind Speed: ", new_finder)
	return new_finder

#get_wind(json, n=0)	

def get_sealevel(json, n=0, t="03:00:00"):
	n=int(n)
	now = datetime.datetime.today()
	now = now + datetime.timedelta(days=n)
	new_date = now.strftime('%Y-%m-%d')
	#t= input("Enter time: ")

	timestamp= str(new_date) + " " + str (t) 
	fin_time=(json.index(timestamp))
	x=json.rfind('"sea_level":', 0, int(fin_time))
	finder=json[x+12:x+22]
	comma=json.find(",", int(x)+12, int(x)+22)
	new_finder=float(json[x+12:comma])	
	#print("Sea Level ", new_finder)
	return new_finder

#get_sealevel(json, n=0)
