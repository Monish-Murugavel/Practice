entries = [
{'name ': 'Alice ', 'score ': 85} ,
{'name ': 'Bob ', 'score ': 90} ,
{'name ': 'Alice ', 'score ': 92} ,
{'name ': 'Charlie ', 'score ': 78} ,
{'name ': 'Bob ', 'score ': 88} ,
{'name ': 'Alice ', 'score ': 81}
]

a=[]
names=[]
for i in entries:
    x=list(i.values())
    a.append(x)
for j in a:
    names.append(j[0])

unique=list(set(names))
score=[]

for k in unique:
    list=[]
    for l in a:
        if l[0]==k:
            list.append(l[1])
    score.append(list)
print(dict(zip(unique,score)))




