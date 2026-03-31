def hcf(max,min):
    if(min==0):
        return max
    else:
        return hcf(min,max%min)

a=int(input("Enter 1st no"))
b=int(input("Enter 2nd no"))
if a<b:
    min=a
    max=b
else:
    min=b
    max=a
    
print(hcf(max,min))
