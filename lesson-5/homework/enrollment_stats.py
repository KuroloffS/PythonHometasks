def enrollment_stats(lists):
  lists_price = [lists[2:] for i in lists]
  lists_admission = [lists[1:2] for a in lists]
  print("Total students : ", sum(lists_admission))
  print("Total tuition : ", sum(lists_price))

lists = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
enrollment_stats(lists)