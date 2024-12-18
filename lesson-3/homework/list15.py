# Initializing counters for even and odd numbers
even = 0
odd = 0

for num in list:
  
    # Checking if the number is even
    if num % 2 == 0:  
        even += 1
    else:  
        odd += 1

# Printing the results
print("Even numbers:", even)
