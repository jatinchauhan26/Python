unit = input("Is this temp in celsius or farenheit(C/F): ")
temp = float(input("enter the temperature"))
if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"the temp in fahrenhiet is: {temp}°F") #alt+0176 (°)
elif unit == "F":
    temp = round((temp-32)*5/9,1)
    print(f"the temp in celsius  is :{temp}°C") 
else:
    print("the given unit is invalid")
