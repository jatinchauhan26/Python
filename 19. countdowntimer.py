import time #importing time module

my_time =int(input("enter the time in seconds"))

for x in reversed(range(0,my_time)): #or we can use  for x in range(my_time, 0, -1):
 seconds = x % 60
 minutes = int(x/60) % 60 #we dont want to go above 60 
 hours = int(x/3600) #we dont add %24 because we dont  have days in f string

 print(f"{hours:02}:{minutes:02}:{seconds:02}")
 time.sleep(1)

print("Time'S UP!")
