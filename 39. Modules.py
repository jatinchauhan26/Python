# module = a file containing code you want to include in your program 
#          use 'import' to include a module (built_in or your own)
#          useful to break up a large program reusable separate files

#--------Example 1
# print(help("modules"))
# print(help("math"))

# import math 
# print(math.pi)

# import math as m
# print(m.pi)

# from math import pi 
# print(pi)

#----------Example 2
# import math
# from math import e 
# a,b,c,d = 1,2,3,4
# a,b,c,d,e = 1,2,3,4,5
#
# print(a,b,c)
# print(e**a)
# print(math.e**a)
# print(e**b)

#_--------->example 3
pi = 3.14159
def square(x):
    return x**2

def cube(x):
    return x**3

def circumference(radius):
    return 2*pi*radius

def area(radius):
    return pi*radius**2

print(cube(2))


# #run it to new file \
# import Modules # make the filename 39. Modules to Modules
# result = Modules.pi
# result = Modules.square(3)
# # result = Modules.circumference(3)
# print(result)








