def invest(amount, rate, years):
  i = 0
  while i < int(years):
    amount = float(amount) *( 1 + float(rate))
    print(f"year { i+ 1} : {amount:.2f}")
    i+=1
years = int(input("Enter a year: "))
amount = float(input("Enter an amoount: "))
rate = float(input("Enter a rate: "))
invest(amount, rate, years)

