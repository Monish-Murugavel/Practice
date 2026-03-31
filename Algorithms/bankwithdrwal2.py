n=int(input("Enter bank balance:"))
m=1
while m!=0:
    m=int(input("Enter amount to be withdrawed:"))
    if m<=n:
      print("Bank balance:",n-m)
      n=n-m
      if n==0:
         print("No balance")
         break
    else:
      print("Insuffcient bank balance")
      print("Balance:",n)