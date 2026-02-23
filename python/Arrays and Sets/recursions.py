'''def fact(x):
    if(x==1):
        return 1
    else:
        return(x*fact(x-1))
num=int(input('enter :'))
print(fact(num))'''

n=int(input("Enter number:"))
def fibnocci(x):
    if n<=1:
        return n
    else:
        return(fibnocci(n-1)+fibnocci(n-2))
    
if n<=0:
        print("ENter positive integer")
else:
        print("Fibnocci is")

        for i in range(n):
            print(fibnocci(i),end='')


