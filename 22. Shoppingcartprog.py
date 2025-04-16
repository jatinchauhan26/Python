#SHOPPING CART PROGRAM

foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of a {food}:$ "))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")        
        
for food in foods:
    print(food, end =" ")

for price in prices:
    total = total+price
#this print statement is taken outside because we need to make total complete value first so it print after every food value  get add to total  
print()
print(f"your total is :${round(total,2)}")
