import time 
def test_timpe(func):
  def wrapper(*args, **kwargs):
    st = time.time()
    res = func(*args, **kwargs)
    end = time.time()
    dt = end - st
    print(f"Время работы : {dt} сек")
    return res

  return wrapper  
  
@test_timpe    
def get_slow_nod(a, b):
  while a!=b:
    if a > b:
      a-=b
    else :
      b-=a
  return a 

@test_timpe
def get_fast_nod(a, b):
  if a < b:
    a, b = b, a
  while b :
    a, b = b, a % b 
  return a   

#get_slow_nod = test_timpe(get_slow_nod)
#get_fast_nod = test_timpe(get_fast_nod)

res = get_slow_nod(48, 1000000)
res2 = get_fast_nod(48, 1000000)
print(res, res2)
