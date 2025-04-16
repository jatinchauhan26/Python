# dictionary = a collection of {key:value} pairs
#             ordered and changeable . No dublicates

capitals = {"USA": ("Wahington D.C."),
            "India" : "Delhi ",
            "China" : "Beijing",
            "Russia":"Moscow"}

# print (dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

# print(capitals.get("japan")) #give null value bcz japan is not in the dictionary

# if capitals.get("Russia"):
#  print ("that capital exists")
# else:
#     print("the capital doesnt exist")

# capitals.update({"Germany":"Berlin"}) #you can update or add the new value to dictionary
# capitals.update({"India":"Mumbai"}) 
# print(capitals)



# capitals.pop("China") #to remove an key
# capitals.popitem() #it will remove the latest key value pairs
# print(capitals)

# capitals.clear() #clear the dictionary
# print(capitals)

# keys = capitals.keys()
# print(keys)
# or
#for key in capitals.keys():
# print(key)
# or
# print(capitals.keys())
# print(capitals.values()
#or
# values = capitals.values()
# for value in values:
#  print(value)
