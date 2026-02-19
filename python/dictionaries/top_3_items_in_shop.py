shop={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
v=[]
z=[]
a=[]
e=[]
for j in shop:
    d=shop.get(j)
    v.append(d)

w=sorted(v)

for k in shop:
    if w[-1]==shop[k]:
        print(w[-1],k)

    elif w[-2]==shop[k]:
        print(w[-2],k)

    elif w[-3]==shop[k]:
        print(w[-3],k)