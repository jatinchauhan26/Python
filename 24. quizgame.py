questions = ("HOw many elements are in the periodic  table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in the atmosphere?",
             "How many bones in the human body?",
             "Which planet in the solar system is the hottest? ")

options = (("A.116 ","B.117 ","C.118 ","D.119 "),
           ("A.whale ","B.crocodile ","C.elephant ","D.ostrich "),
           ("A.nitrogen ","B.oxygen ","C.carbon-dioxide ","D.hydrogen"),
           ("A.205 ","B.206 ","C.208 ","D.209 "),
           ("A.mercury ","B.venus ","C.earth ","D.mars "))

answers = ("C","D","A","A","B")
guesses = [] #we will append the guesses to list so we are using list
score = 0
question_num = 0

for question in questions:
    print("------------------------------------------")
    print(question) 
    for option in options[question_num]:
      print(option)
   
    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess ==  answers[question_num]:
       score +=1
       print("CORRECT!")
    else:
      print("INCORRECT!")         
      print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("------------------------------------------")
print("RESULTS")
print("------------------------------------------")

print("answers:", end="")
for answer in answers:
   print(answer,end=" ")
print()


print("guesses:", end="")
for guess in guesses:
   print(guess,end=" ")
print()
  
score = int(score/len(questions)*100) 
print(f"your score is : {score}")