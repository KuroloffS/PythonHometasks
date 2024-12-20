def remainder(number):
  i = 1
  while i <= number :
    if number % i == 0:
      print(f"{i} is factor of {number}") 
    i += 1   
number = int(input("Enter a number : "))
remainder(number)  