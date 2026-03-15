x=[]
price=1
while price!=0:
        price=int(input("Enter price of item:"))
        nos=int(input("Enter number of items:"))
        z=price*nos
        x.append(z)
print("Total bill:",sum(x))