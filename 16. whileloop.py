#while loop = execute some code WHILE some condition remains true 
#run infinite loop if  didnt give any condition to make it eventually false 

#-------- example1
# name = input("enter the name ")

# # if name== "":
# #  print("you did not enter your name")
# # else:
# #  print(f"helllo {name}")
# #we can use else with while


# while name== "":
#  print("you did not enter your name")

# print(f"helllo {name}")

#-------- example2
# age = int(input("enter the age:"))
# while age < 0:
#   print("age cant be zero")
#   age = int(input("enter the age:"))
# print(f"your age is {age}")


#--------  example 3

# food = input("enter any food you like ( q to quit)")

# while not food == "q":
#  print(f"You like {food}")
#  food = input("enter another food name(q to exit) ")
# print("bye")

#-------- example 4
num = int(input("enter any number"))
while num < 1 or num > 10:
    print(f"{num} num is not valid")
    num = int(input("enter a number between 1-10"))
    
print(f"your number is {num}")