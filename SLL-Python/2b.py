def farenheittocelcius():
	temp=int(input("Please enter the farenheit temperature"))
	celcius= ((temp-32)*5)/9
	print (celcius)
	exit ()
    

def farenheittokelvin():
	temp=int(input("Please enter the farenheit temperature"))
	celcius= ((temp-32)*5)/9+273
	print (celcius)
	return

def celciustokelvin():
	temp=int(input("Please enter the celcius temperature"))
	celcius= temp+273
	print (celcius)
	return

def celciustofarenheit():
	temp=int(input("Please enter the celcius temperature"))
	celcius= (temp*9)/5+32
	print (celcius)
	return

def kelvintofarenheit():
	temp=int(input("Please enter the kelvin temperature"))
	celcius= ((temp-273)*9)/5+32
	print (celcius)
	return

def kelvintocelcius():
	temp=int(input("Please enter the kelvin temperature"))
	celcius= ((temp-32)*(5/9))+273
	print (celcius)
	return

print ("1.farenheit to celcius")
print ("2.farenheit to kelvin")
print ("3.celcius to kelvin")
print ("4.celcius to farenheit ")
print ("5.kelvin to farenheit")
print ("6.kelvin to celcius")

choice = int(input("choose from the following options:"))

m=1
while(m==1):
 if (choice==1):
  farenheittocelcius()
 if (choice==2):
  farenheittokelvin()
 if (choice==3):
  celciustokelvin()
 if (choice==4):
  celciustofarenheit()
 if (choice==5):
  kelvintofarenheit()
 if (choice==6):
  kelvintocelcius()
