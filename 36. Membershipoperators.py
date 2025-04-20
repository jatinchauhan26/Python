#Membership operators = used to test whether a value or variable is found in asequence 
# (string, list , tuple , set , or dictionary)
# 1. in
# 2. not in



# word = "APPLE"
# letter = input("Guess a letter in the secret word:").upper()
#----------> 1. in example

# if letter in word :
#     print(f"There is a {letter}")
# else:
#     print("letter not found")    

#-----------> 2. not in example

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

#------------------>

# students = {"jatin","ravi","sudhanshu","love","akshay"}

# student = input("enter the name of the student:")


# if student in students:
#     print(f"{student} is  a student")
# else:
#    print(f"{student} is not a student")


#------------->


# grades = {"Sandy": "A",
#           "Sidhu":"B",
#           "Sahil":"C",
#           "Siddharth":"D"}

# student = input("enter the name of a student:").capitalize()

# if student in grades:
#     print(f"{student}'s grade is {grades[student]} ")
# else:
#     print(f"{student} is not found")


# email = input("ENTER YOUR EMAIL HERE:")

# if "@" in email and "." in email :
#     print("Valid email")
# else:
#     print("Invalid email")