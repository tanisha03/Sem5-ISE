def farenheittocelcius():
    temp = int(input("Please enter the farenheit temperature"))
    ans = ((temp - 32) * 5) / 9
    conv.append((temp, ans))
    print(ans)


def farenheittokelvin():
    temp = int(input("Please enter the farenheit temperature"))
    ans = ((temp - 32) * 5) / 9 + 273
    conv.append((temp, ans))
    print(ans)


def celciustokelvin():
    temp = int(input("Please enter the celcius temperature"))
    ans = temp + 273
    conv.append((temp, ans))
    print(ans)


def celciustofarenheit():
    temp = int(input("Please enter the celcius temperature"))
    ans = (temp * 9) / 5 + 32
    conv.append((temp, ans))
    print(ans)


def kelvintofarenheit():
    temp = int(input("Please enter the kelvin temperature"))
    ans = ((temp - 273) * 9) / 5 + 32
    conv.append((temp, ans))
    print(ans)


def kelvintocelcius():
    temp = int(input("Please enter the kelvin temperature"))
    ans = ((temp - 32) * (5 / 9)) + 273
    conv.append((temp, ans))
    print(ans)


c = "y"
tup = (
    (1, "farenheit", "celcius"),
    (2, "farenheit", "kelvin"),
    (3, "celcius", "kelvin"),
    (4, "celcius", "farenheit"),
    (5, "kelvin", "farenheit"),
    (6, "kelvin", "celcius"),
    (7, "show tuple"),
)
conv = []

while True:
    print(tup)
    ch = int(input("Enter choice: "))
    if ch == 1:
        farenheittocelcius()
    elif ch == 2:
        farenheittokelvin()
    elif ch == 3:
        celciustokelvin()
    elif ch == 4:
        celciustofarenheit()
    elif ch == 5:
        kelvintofarenheit()
    elif ch == 6:
        kelvintocelcius()
    elif ch == 7:
        print(conv)
    else:
        print("wrong option")

    c = input("Continue? (y/n)")
    if c == "n":
        break
