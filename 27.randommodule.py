import random 

low = 1
high =100
options = ("rock","paper","scissor")
cards = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"}
# number = random.randint(low,high)      #---this wil give random number bwtween 1 to 100
# number = random.random()               #---this will give random floating point number between 0 and 1
# print(number)
# option = random.choice(options)         #---choice is a function of import module                  
# print(option)                           #---choice method will work in list and tuple both

#---------------ONLY WORK IN LIST AND RANDOM MODULE 
# random.shuffle(options) 
# print(options)

# card = random.shuffle(cards) this will not work 
# print(card)

random.shuffle(cards) 
print(cards) #this will shuffle the cards