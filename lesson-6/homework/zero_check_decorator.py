def check(func):
  def wrapper(*args, **wargs):
    a, b = args
    if b == 0:
      return "Denominator can't be zero"
    else:
      return func(*args, **wargs)
  return wrapper      

@check
def div(a, b):
  return a / b

print(div(6, 0))

