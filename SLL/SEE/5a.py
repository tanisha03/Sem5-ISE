def farenheittocelcius():
	temp=int(input("Please enter the farenheit temperature"))
	print(((temp-32)*5)/9)

def farenheittokelvin():
	temp=int(input("Please enter the farenheit temperature"))
	print(((temp-32)*5)/9+273)

def celciustokelvin():
	temp=int(input("Please enter the celcius temperature"))
	print(temp+273)

def celciustofarenheit():
	temp=int(input("Please enter the celcius temperature"))
	print((temp*9)/5+32)

def kelvintofarenheit():
	temp=int(input("Please enter the kelvin temperature"))
	print(((temp-273)*9)/5+32)

def kelvintocelcius():
	temp=int(input("Please enter the kelvin temperature"))
	print(((temp-32)*(5/9))+273)

c='y'
tup = ((1,'farenheit','celcius'),(2,'farenheit','kelvin'),(3,'celcius','kelvin'),(4,'celcius','farenheit'),(5,'kelvin','farenheit'),(6,'kelvin','celcius'))

while(True):
    print(tup)
    ch=int(input("Enter choice: "))
    if ch==1:
        farenheittocelcius()
    elif ch==2:
        farenheittokelvin()
    elif ch==3:
        celciustokelvin()
    elif ch==4:
        celciustofarenheit()
    elif ch==5:
        kelvintofarenheit()
    else:
        kelvintocelcius()

    c=input("Continue? (y/n)")
    if c=='n':
        break