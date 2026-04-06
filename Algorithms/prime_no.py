'''n=int(input("Enter a number :"))
flag=False
for i in range(2,n):
    if n%i==0:
        flag=True
        break
if flag==False:
    print('Prime')
else:
    print("Composite")'''

n=int(input("Enter a number :"))
x=[]
y=[2]
for i in range(2,n+1):
    if n%i!=0 :
        x.append(i)
for j in x:
    if j%2!=0:
        y.append(j)
print(y)


