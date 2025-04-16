#Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle<=0:
       principle = float(input("enter the principle value"))
       if principle<0:
        print("principle amount cant be zero")
       

while rate<=0:
    
    rate = float(input("enter the interest rate"))
    if rate<=0:
        print("rate amount cant be zero")
   #automatically break because value is greater than zero     

while True:
    time = int(input("enter the time value"))
    if time<=0:
        print("time amount cant be zero")
    else:
        break
#we need to break because it remains true so run infinnite for value greater than 0

total = principle*pow((1+rate/100),time)
print(f"balance after {time} year/s: ${total:.2f}")
