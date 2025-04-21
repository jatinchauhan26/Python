# List comprehension = A concise way to create a list in python 
#                      Compact and easier to read traditional loops 
#                      [expression for value in iterable if condition]


# ----------> BY NORMAL APPEND METHOD

# doubles = []
# for x in range (1,11):
#     doubles.append(x*2)
# print(doubles)

# # ------> BY LIST COMPREHENSION METHOD

# doubles =  [ x*2 for x in range(1,11)]
# print(doubles)

# -----> EXAMPLE 3

# doubles =  [ x*2 for x in range(1,11)]
# triples =  [ y*3 for y in range(1,11)]
# squares =  [ z*z for z in range(1,11)]
# print(doubles)
# print(triples)
# print(squares)

#------------>EXAMPLE 4 
# fruits = ["apple","orange","banana","coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

#                 OR

 
# fruits = [fruit.upper() for fruit in ["apple","orange","banana","coconut"] ] 
# print(fruits)


#---------->EXAMPLE 5

# fruits = ["apple","orange","banana","coconut"]
# fruit_char= [fruit[0] for fruit in fruits[0]]
# fruit_char = [fruit[0] for fruit in fruits]
# print(fruit_char)


#--------> EXAMPLE 6

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_nums = [num for num in numbers if num>=0]
# negative_nums = [num for num in numbers if num<0]
# even_nums = [num for num in numbers if num%2 ==0]
# odd_nums = [num for num in numbers if num%2 !=0]

# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)



#-------> EXAMPLE 7

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)

#---------->EXAMPLE I MAKE 

students = ["jatin","ravi","sahil","sudhanshu","love","akshay"]
friends = [friend for friend in students if friend[0] == "s"]
print(friends)