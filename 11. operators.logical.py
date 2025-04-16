#---------------- NORMAL OPERATORS

# friends = 5
# # friends = friends + 1
# # friends +=1
# # friends -= 1
# # friends *= 1
# # # friends /= 1
# # friends **= 1
# rem=friends%3
# print(rem)

x=3.7
y=-4
z=5
# result = round(x) (round value which is closest, can give float too like 9.77777 so if we mention round(x,2) it will give 9.77)
# result = abs(z)(whole value always positive means give distance)
# result = pow(4,3) #power
# result = max(x,y,z)
result = min(x,y,z)
print(result)


#------------------LOGICAL OPERATORS
#logical operators = evaluate multiple conditions(or,and,not)
#or = at least one condition must be true 
#and = both conditions must be true 
#not = inverts the condition (not False,not True)

temp = 25
is_raining =  False
# is_sunning =  True
is_sunning =  not True
if  (is_raining and is_sunning) or temp<24:
 print("event is cancelled")
else:
 print (" event not cancelled ") 