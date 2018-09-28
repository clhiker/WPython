def pay(wage,hours):
  if hours <= 40:
    amount = wage * hours
  else:
    amount = (wage * 40) + ((1.5) * hours * wage * (hours - 40))
  return amount
    
