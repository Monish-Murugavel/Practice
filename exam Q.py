rules=[('a','b'),('c','d'),('b','c'),("b",'a')]
s=[]
target=input('enter name')
for i in rules:
    if i[0]==target:
        s.append(i[1])
p=[]
for i in s:
    for j in rules:
        if i==j[0]:
            p.append(j[1])
v=p+s
for i in rules:
    if target==i[1]:
      continue
    else:
        v.append(i[1])


z=set(v)
print(z)
    
        