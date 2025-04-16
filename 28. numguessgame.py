#Python number guessing game 

import random 

lowest_num = 10
highest_num =  100

answer = random.randint(lowest_num,highest_num)
guesses =0
is_running = True

print("-------------------------------------------------------------")
print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
# while True:
 print("-------------------------------------------------------------")
 guess = (input("Enter your guess:"))
 print("-------------------------------------------------------------")
 if guess.isdigit():
      
     
      guess = int(guess)
      guesses +=1 
      
      if guess<lowest_num or guess>highest_num:
        print("guess is out of range")
      elif guess<answer:
        print("Try Again! number is too low ")  
      elif guess>answer:
        print("Try Again! number is too high ")  
      else:
        print("Correct Number! Well Done")
        print(f"Number of guesses: {guesses}")
        print("-------------------------------------------------------------")
        is_running = False
 else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")
        print("-------------------------------------------------------------")
          









