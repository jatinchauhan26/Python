menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "candy" :2.00,
        "tofee":4.23,
        "burger":9.2}
print("----------------")
cart = []
total = 0 
for key,value in menu.items():
    print(f"{key:10}:{value:.2f}")
print("----------------") 
while True :
    food = input("select food(q to exit:)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER-------")
for food in cart:
    total += menu.get(food) #this is used to get the price 
    print(food, end = " ")

print()
print(f"Total is :${total:.2f}")
