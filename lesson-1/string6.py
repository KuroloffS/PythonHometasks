#lesson2 #string #problem6
def check_substring(main_string, substring):
  if substring in main_string:
      return True
  return False

# Example usage
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if check_substring(main_string, substring):
  print(f'"{substring}" is found in "{main_string}".')
else:
  print(f'"{substring}" is not found in "{main_string}".')