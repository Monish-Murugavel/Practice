import array as arr
arr= arr.array('i',[10, 5, 2, 7, 1, -10])
k=int(input('ENter number'))
x=[]
while k!=0:
    for i in arr:
        y=[]
        for j in arr:
            y.append(i-j)
            k-=i
        x.append(y)

        
