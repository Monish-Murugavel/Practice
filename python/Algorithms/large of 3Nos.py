x=int(input("Enter first Numbver:"))
y=int(input("Enter second Number:"))
z=int(input("Enter third number"))
if x>y and x>z:
    print("The largest number is",x)
elif y>z:
    print("The largest number is",y)
else:
    print("The largest number is",z)
