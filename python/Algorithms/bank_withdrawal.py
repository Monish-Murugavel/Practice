n=int(input("Enter bank balance:"))
m=int(input("Enter amount to be withdrawed:"))
while m!=0:
    if m<=n:
      print("Bank balance:",n-m)
      m=int(input("Enter amount to be withdrawed:"))
      n=n-m
    else:
      print("Insuffcient bank balance")
      print("Balance:",n)
      break 
        
