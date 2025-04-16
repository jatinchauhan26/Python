#Functions = A block of reusable code 
#            Place () after the function name to invoke it 

# i=0
# while i<3 :
#  print("Happy birthday to you!")
#  print("You are old!")
#  print("Happy birthday to you!")
#  i =i +1
#  print()
# print()

# def happy_birthday():
#  print(f\"Happy birthday to you !")
#  print("You are old!")
#  print("Happy birthday to you!")  
#  print()


# happy_birthday()
# # happy_birthday()
# # happy_birthday()



# def happy_birthday(name):
#  print(f"Happy birthday to {name} !")
#  print("You are old!")
#  print("Happy birthday to you!")  
#  print()


# happy_birthday("bro")
# happy_birthday("bhai")


# def happy_birthday(x,y,country):
#  print(f"Happy birthday to {x} !")
#  print(f"You are {y} old!")
#  print(f"Happy birthday to you!")  
#  print()


# # happy_birthday("bro",16)  #this line will show error it is compulsory to give every argument value)
# happy_birthday("bro",16,"india")
# happy_birthday("bhai",16,"india")


# simple calculator  by function 
# def add(x,y):
#     z = x+y
#     return z

# def substract(x,y):
#     z = x-y
#     return z

# def multiply(x,y):
#     return x*y

# def divide(x,y):
#    z = x/y 
#    return z 

# x = int(input( "enter the value of x:"))

# y = int(input ("enter the value of y:"))

# print(add(x,y))  , print(multiply(x,y))
# print(divide(x,y)) , print(substract(3,5)) ,print(substract(x,y)) 


#------------>

def create_name(first,last):
 first = first.upper() #Capitalize all the characters 
 last = last.capitalize() #Capitalize only the first character
 return first + " " + last 

# full_name = create_name("jatin","chauhan")
# print(full_name)

print(create_name("jatin","c"))