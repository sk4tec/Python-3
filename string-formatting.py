expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum = 0

for x in expenses:
    sum += x

print("You speent £", sum) # notice the extra space after the £
print("You speent £", sum, sep='') # specify the separator as an empty string

# could also do total = sum(expenses)