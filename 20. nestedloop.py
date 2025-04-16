#nested loop = A loop within another loop (outer,inner)
# outer loop :
#   inner loop:

# for x in range(3):
#  for y in range(1, 11):
#     print(y, end = "") # print in same line also we can give anything in question marks
  
#  print() #print a new line


rows = int(input("enter the number of rows"))
columns = int(input("enter the number of columns"))
symbol = input("enter the symbol to use")
  
for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()    

   
   