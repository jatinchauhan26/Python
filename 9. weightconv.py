#python weight convertor
weight = float(input("enter the weight:"))
unit = input("kilograms or pounds? (K OR L)")

if unit == "K":
    weight = weight * 2.205
    print (f"Your weight is {weight} pounds")
elif unit == "L":
    weight = weight / 2.205
    print (f"Your weight is:{weight} kgs")
else:
    print("unit is not valid")