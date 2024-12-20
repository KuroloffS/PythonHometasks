def convert_cel_to_far(temp_in_c):
  temp_in_f = temp_in_c * ( 9 / 5) + 32
  return temp_in_f
temp_in_c = float(input("Enter a temperature in degrees C : "))
print(f"{temp_in_c} degrees C = {convert_cel_to_far(temp_in_c):.2f} degrees F")
def convert_far_to_cel(F) :
  C = (F - 32) * 5/9
  return C 
F = float(input("Enter a temperature in degrees F : "))
print(f"{F} degrees F = {convert_far_to_cel(F):.2f} degrees C")