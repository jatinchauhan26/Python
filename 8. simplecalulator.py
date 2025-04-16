operator = input("Enter any operator (+,-,*,/)")
num1 = float(input("enter the num 1:"))
num2 = float(input("enter the num2:"))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "/":
    if num2 == 0:
      print("not divisible by zero")
    else:
     result= num1/num2
     print(result)
else: 
    print(f"the operator {operator} is invalid") 