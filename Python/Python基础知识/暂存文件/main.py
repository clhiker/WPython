import finance
hourlywage = eval(input("enter wage"))
hoursworked = eval(input("enter hours"))
earning = finance.pay(hourlywage,hoursworked )
print("earning:{0:,.2f}".format(earing))
