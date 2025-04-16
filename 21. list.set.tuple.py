# collection = single "variable" used to store multiple values
#List = [] ordered and changeable. Dublicates Ok
#Set = {} unordered and immutable, but Add/Remove OK. No dublicates
#Tuple = () ordered and unchangeable. Dublicates OK. faster

####==================>>>LIST

# fruits = ["apple","orange","banana","coconut"]

#-----> INDEXING AND SOME COMMANDS

# print(fruits[3]) #+index
# print(fruits[0:3])
# print(fruits[::-1]) #reverse 

# for fruit in fruits: #we can use fruit here in place of x
#     print(fruit)

# print(dir(fruits)) #give the list builtin functions
# print(help(fruits)) #give the detail of list builtin functions

# print(len(fruits))
# print("apple" in fruits) #return true check whether element is present in list or not
# print("pineapple" in fruits) #return False

#------>  BUILT IN FUNCTIONS:

# fruits[0] = "pineapple"       #{reassign the values and we can say replace the values}
# fruits.append("pineapple")    #{add an element at the end of the list}
# fruits.remove("apple")        #{remove an element from the list}
# fruits.insert(1,"pineapple")  #{insert an element at any particular index}
# fruits.sort()                 #{sort the list arrange in alphabetically or if numbers then in incresing order}  
# fruits.reverse()              #{reverse the list and we can use both sort and reverse to reverse in alphabetically order}
# fruits.clear()                #{to clear the all elements of list this will print the empty list}

#----> ITERABLE
# for fruit in fruits:
#  print(fruit)

# print(fruits)

# print(fruits.index("apple"))  #{this will give the index of given value and works only under print statements}
# print(fruits.count("banana")) #{count the number of time the given value comes}




###=================>>> SET ---- no indexing in set and it is unordered

# fruits = {"apple","orange","banana","coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits) #give false

# fruits.add("pineapple")    #{add at any place bcz set is unordered}
# fruits.remove("apple")     #{remove an element}
# fruits.pop()               #{it will pop the first element but remove random because  set is unordered}
# fruits.clear()               #{provides an empyty list}

# ------> NO DUBLICATES ARE ALLOWED
# fruits = {"apple","orange","banana","coconut","banana"}
#it will print banana only one time

# print(fruits) 

#------->ITERABLE
# for fruit in fruits:
#     print(fruit)



###================>>> TUPLE --FAST

# fruits = ("apple","orange","banana","coconut","coconut","coconut")


# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))         #this will give the index of given value
# print(fruits.count("coconut"))       #this will return the no. of times any value comes

# ------> ITERABLE
# for fruit in fruits:
#     print(fruit)









