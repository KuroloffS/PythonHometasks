def check(func):
  def wrapper(*args, **kwargs):
    reminder = func(*args, **kwargs)
    return reminder 
  return wrapper
@check
def div(a, b):
  if b == 0 :
    print("Denominator can't be zero")
  else :
    return a / b

result = div(6, 0)
print(result)