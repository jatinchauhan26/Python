#*args = allows you to pass multiple non = key arguments ------POSTIONAL ARGUMENTS
#**kargs = allows you to pass multiple keyword - argume=ments --------KEYWORD ARGUMENTS
#  *unpacking operator 
#   1. positional 2. default 3. keyword 4. ARBITRARY 

#---------->
# def add (a,b):
#     return a+b

# print(add(1,2))

#-------------->
# def add(*args):     ---------#def add(*num)
#     # print(type(args))
#     # return a+b
#  total = 0
#  for arg in args:
#    total += arg 
#  return total 
 
# print(add(1,2,3,4,6,9))

#------------>
# def display_name(*args):
#     for arg in args :
#       print(arg, end = " ")

# display_name ("Dr.","Spongebob","Harold","Squarepants","III")

#---------->
#----------------->HERE KWARGS FOR KEYS AND VALUES PAIRS TYPE DICTIONARY

# def print_address(**kwargs):
# #  print(type(kwargs)) ----------we packed into dictionary
# #   for value in kwargs.values():
# #     print(value)
# #   for key in kwargs.keys():
# #     print(key)
#   for key,value in kwargs.items():
#     print(f"{key}:{value}")

# print_address(street = "123 Fake St.",
#               city = "aMROHA",
#               state = "UP",
#               zip = "244221")


#----------------EXAMPLE:

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # for key,value in kwargs.items():
    #  print(f"{key}: {value},", end =" ")
    # print()

    if "street" in kwargs : 
     print(kwargs.get("street"))
    else:
     print( "kdl")
shipping_label("Dr.","Spongebob","Squarepants","III",
               apt = "100",city="detroit",state ="mi",zip="244221")            
    