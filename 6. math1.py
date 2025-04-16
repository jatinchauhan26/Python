import math
# print(math.pi)
# print(math.e)#in physics
#result = math.sqrt(9)
# result = math.ceil(9.1) (always give upper value like 10)
# result = math.floor(9.9) (always give lower value like 9)


# #circumference of circle
# radius = float(input("enter the radius of the circle"))
# circumference = 2*math.pi*radius
# print(f" the circumference is:{ round(circumference,2)}cm") #2 defines here the decimal point to give like 65.34 example


# # area of circle
# radius = float(input("enter the radius:"))
# area = math.pi*pow(radius,2)
# print(f"area of circle is :{round(area,2)}cm²) #alt+0178

#hypotenuse of a right angled triangle
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))

c = math.sqrt(pow(a,2)+pow(b,2))
print(f"Side c is: {round(c,2)}")