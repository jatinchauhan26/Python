#indexing = accessing elemnts of a sequence using [] (indexing operators)
# [start : end : step]
credit_number = "1234-5678-3242-6435"
# print(credit_number[4])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-3]) #- count starts from last with first count -1
print(credit_number[::2]) #print every second character of string
print(credit_number[::3]) 
# lastdigits = credit_number[-8:]
credit_number = credit_number[::-1] #reverse the nubmbers in credit number if step=-1