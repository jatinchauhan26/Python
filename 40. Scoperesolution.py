#variable scope = where a variable is visble and accessible 
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
#                     

#-------------->local 
# def func1():
#  a = 1
#  print(a)

# def func2():
#  b = 2 
#  print(b)

# func1()
# func2()


# def func1():
    

#     def func2():
#         x=2           #local scope  
#         print(x)
#     func2()

# func1()   
     
# --------------- >enclosed 
# def func1():
    #   x=1

#     def func2():
           
#         print(x)
#     func2()

# func1()        

#--------------> global

# from math import e

# def func1():
    
#     print(e)

# e = 3
# func1()

#---------------> 

from math import e 

def func1():
    print(e)
func1()

