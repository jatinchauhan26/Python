#Match-case statement(switch) : An alternative to using any 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable


# -------------> BY ELIF

# def day_of_week(day):
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else :
#         return "Not a Valid day"
# try:
#    day = int(input("enter the value"))  
#    print(day_of_week(day))
# except ValueError:
#    print("Please enter a valid number")   
           

# -------------> BY SWITCHCASE


# def day_of_week(day):

#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _ :
#             return "Not a Valid day"
        
# print(day_of_week(1))        
        
#             #  OR

# while True:
#  try:
#    day = int(input("enter the value"))  
#    result = (day_of_week(day))
#    print(result)
#    if result == "Not a Valid day":
#     break
#  except ValueError:
#     print("Please enter a valid number")   
           


# -------------EXAMPLE2


# def is_weekend(day):
#     match day:
#        case "Sunday":
#         return True
#        case "Monday":
#         return False
#        case "Tuesday":
#         return False
#        case "Wednesday":
#         return False
#        case "Friday":
#         return False
#        case "Saturday":
#         return False
#        case _:
#         return False
      
# print(is_weekend("Sunday"))
   
#    OR


def is_weekend(day):
   
    match day :
      case "Saturday" | "Sunday":
         return True
      case "Monday"| "Tuesday" | "Wednesday"| "Thursday"|"Friday":
         return False
      case _:
         return False

print(is_weekend("Sunday"))
