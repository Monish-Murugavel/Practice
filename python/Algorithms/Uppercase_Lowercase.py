n=int(input('enter no'))
while n!=0:
    s=input('enter str')
    x=[]
    for i in s:
        if i.isupper():
            x.append(i.lower())
        else:
            x.append(i.upper())
    for y in x:
        print(y,end='')
    print()
    n=n-1
