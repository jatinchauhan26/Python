#Default arguments = A default value for certain parameters 
# default is used when that argument is omitted
# a=make your functions more flexible , reduces no. of arguments
# 1. positional 2. DEFAULT 3. keyword 4. arbitrary

# def net_price(list_price,discount=0,tax=0.05):
    #we set default values in upper functions 
#     return list_price*(1- discount)*(1+tax)

# print(net_price(500,0,0.05))
# print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,0))



#------------> COUNT UP TIMER

import time 

# def count(start, end):
def count(end, start = 0):
    for x in reversed(range(start , end+1)): # we used end+1 because second one is exclusive like when we want to go 1,10 we write 1,11
        print(x)
        time.sleep(1)
    print("Done!")
count(20,10)     



