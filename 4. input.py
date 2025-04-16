# input() = A function that prompts the user to enter data returns the entired data as a string
# age = int(input("enter your age:"))
# # age= int(age)
# age = age + 1
# print(f"your age is {age}")
# print("happppy bday")

# example to print area of rectangle
# length = float(input("enter value of length"))
# breadth =float(input("enter value of breadth"))
# area = length*breadth
# print(f"the area is {area}cm^2")


#example shopping cart program
item = input("enter the item:")
price = float(input("enter the price of item:"))
quantity = int(input("enter the quantity:"))
total = price*quantity
print(f"you bought {quantity}x {item}/s")
print(f"your total is: {total}inr")



#validate user input exercise 
#1. username is no more than 12 characters 
#2. username must not contain spaces
#3. username must not contain digits
# username = input("Enter a username:")

# if len(username)>12:
#     print("your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#  print("your username can't contain spaces")
# else:
# #     print(f"welcome{username}"
# print(8)
# print(13,end=" ")
# print(21)