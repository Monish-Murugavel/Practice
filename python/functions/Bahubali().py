army=[("Kuntala Army", "Kumar Varma", {"Infantry": 5000, "Cavalry": 2000,
"Archers": 3000}), ("Mahishmati Army", "Bhallaladeva", {"Infantry":
8000, "Cavalry": 3000, "Archers": 4000})]

for i in army:
    d=i[2]
    x=d.values()
    print(i[0],':',sum(x),end=' ')
print()
count=0
for j in army:
    d2=j[2]
    d3=d2['Cavalry']
    if d3>count:
        count=d3

for k in army:
    d4=k[2]
    if d4['Cavalry']==count:
            print('Army with Largest Cavalry:',k[0])

count1=0
for l in army:
    d5=l[2]
    d6=d5['Infantry']
    if d6>count1:
        count1=d6

for m in army:
    d7=m[2]
    if d7['Infantry']==count1:
         print('Commander with Most Infantry:',m[1])





        








