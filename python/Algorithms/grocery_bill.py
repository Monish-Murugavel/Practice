x=[]
y=True
while y==True:
        price=int(input("Enter price of item:"))
        nos=int(input("ENter number of items:"))
        z=price*nos
        x.append(z)

        j=input("DO YOU WANT TO CONTINUE:(YES/NO)?")
        if j.upper()=="YES":
                    y=True
        elif j.upper()=="NO":
                    y=False
                    print("Thank you for shopping!")
        else:
                    print("Invalid")
print("Total bill amount:",sum(x))
    
        


