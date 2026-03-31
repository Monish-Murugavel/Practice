avatar=[]
count=int(input('Enter num of specices'))

for i in range(count):
    list=[]
    name=input('Enter name')
    type=input('Enter flora or fauna')
    num=int(input('Enter num of places'))
    list.append(name)
    list.append(type)
    c=[]
    for j in range(num):
        places=input('Enter name of place')
        c.append(places)
    list.append(c)
    avatar.append(tuple(list))
print(avatar)

c1=0
c2=0
dict={}  
for k in avatar:
    if k[1].lower()=='flora':
        c1+=1
    else:
        c2+=1
dict.update({'Flora':c1,'Fauna':c2})
print(dict)

details=input('Enter place wanted')
wanted=[]
for l in avatar:
    if details in l[2]:
        wanted.append(l[0])
print('Species in',details,':',wanted)

c3=[]
for m in avatar:
    list2=m[2][0]
    for n in list2:
        c3.append(n)
print('Region of greatest biodiversity:',max(c3))





