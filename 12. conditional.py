#conditional expression = A one line shortcut for the if else statement 
#Print or assign one of two values based on a condtion
# X if conditon else Y

# num=int(input("enter the number"))
# # print("Positive" if num >0 else "negative")
# result = "EVEN" if num%2==0 else "odd"
# print(result)

# a=4
# b=6
# max_num = a if a>b else b
# min_num = a if a<b else b
# print(max_num)
# print(min_num)

# age = int(input("enter the age:"))
# if age>=18:
#  print("adult")
# elif 0<age<18:
#  print("not adult")
# else:
#  print("enter valid age")

##here we did with conditional statements
# result= "adult" if age>=18 else "not adult"
# print(result)

# if age<0:
#       print("enter a valid age")

user_role = "guest"
access_level ="Full access" if user_role =="admin" else "limited access"

print(access_level)

