a=[2,3,1,3,4,4,5,6,9]
b=set(a)
c={}
for i in b:
    for j in b:
        if i==j:
            pass
        else:
            c.update({i*j:(i,j)})
d=c.keys()
e=max(d)

print(c[e])

