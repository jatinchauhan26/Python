# format specifiers = {value:flags} format a value based on what flags are inserted 
price1 = 3.1459
price2 = -987.658
price3 = 12.344
# print(f"price 1 is ${price1:.2f}")
# print(f"price 2 is ${price2:.1f}") #(will display one decimal pla)
# print(f"price 3 is ${price3:.3f}")

# print(f"price 1 is ${price1:12}")
# print(f"price 2 is ${price2:9}")  # add spaces according to given value to make the value 9 on count

# print(f"price 3 is ${price3:010}") #to make the value of 10 digit add 0's to starting
# print(f"price 3 is ${price3:110}") #no output bcz we cant allocate 1

# print(f"price 2 is ${price2:<}")
# print(f"price 3 is ${price3:<10}") #left justified (means no spaces on left )
# print(f"price 2 is ${price2:>10}")
# print(f"price 3 is ${price3:>10}") #right justified (means laast digit at 10 number)

# print(f"price 1 is ${price1:^10}") #for center
# print(f"price 2 is ${price2:^10}")

# print(f"price 1 is ${price1:+}") #number will represent with plus sign
# print(f"price 2 is ${price2:+}") #number will represent with negative sign if already negative 
# print(f"price 3 is ${price3:+}")

# print(f"price 1 is ${price1: }") #we can use to aligned all in line if negative sign takes space
# print(f"price 2 is ${price2: }") #here negative sign will take place that's why we used spaces  
# print(f"price 3 is ${price3: }")

# print(f"price 1 is ${price1:,}") #thousand seperator if value is in thousand like 6576.89 so it give 65576.89
print(f"price 1 is ${price1:+,.2f}") 
print(f"price 2 is ${price2:+,.2f}") 
print(f"price 3 is ${price3:+,.2f}") #we can also use it in combo