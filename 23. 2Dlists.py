
# 2D LISTS

# fruits =     ["apple","orange","banana","coconut"]
# vegetables = ["celery","carrots","potatoes"]
# meats =      ["chicken","fish","turkey"]

# groceries = [fruits,vegetables,meats]
# print(groceries)
# print(groceries[0]) #return entire list of fruits

#  print(groceries[0][2]) #print banana bcz on 0 index we have fruits and the second element is banana
# print(groceries[0][0]) #it will print apple
# print(groceries[2][2])


#---------------->>>>ASSIGN DIRECT WITHOUT USING ITEMS

groceries = [["apple","orange","banana","coconut"],
             ["celery","carrots","potato0es"],
             ["chicken","fish","turkey"]]

# ---WORK ON TUPLE TOO
# groceries = (("apple","orange","banana","coconut"),
#              ("celery","carrots","potato0es"),
#              ("chicken","fish","turkey"))

# print(groceries[0][3])
# print(groceries[0][0])
# print(groceries[2][2]) 

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()





    #2d tuple numpad tuple

# num_pad = ((1,2,3),(4,5,6),
#            (7,8,9),
#            ("*",0,"#"))

# for row in num_pad:
#     for num in row:
#         print(num,end = " ")
#     print()    
