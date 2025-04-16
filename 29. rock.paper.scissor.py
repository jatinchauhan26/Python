import random

options = ("rock","paper","scissor")
running = True 

while running:
    player = None
    computer = random.choice(options)




    while player not in options:
        player =input("Enter a choice: (rock,paper,scissor)")


    print(f"Player : {player}")
    print(f"Computer: {computer}")



    if player == computer :
        print("-----> It's a tie")
    elif (player == "rock" and computer == "scissor"):
        print("-----> Player won")
    elif (player == "paper" and computer == "rock"):
        print("-----> Player Won")
    elif (player == "scissor" and computer == "paper"): 
        print("-----> Player Won")  

    
    else:
        print("Computer Won")    
       
    if not input ("Play again? (y/n): ").lower() == "y":
    # if not play_again == "y":
        running = False

print("Thanks for Playing!")      #Second loop is optional  