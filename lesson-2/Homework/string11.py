#lesson2 #string #problem11
def contains_digits(s):
  for char in s:
      if char.isdigit():
          return True
  return False

input_string = input("Enter a string: ")

if contains_digits(input_string):
  print("The string contains digits.")
else:
  print("The string does not contain any digits.")