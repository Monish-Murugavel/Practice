products = [
    {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
    {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
    {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
]
price=[]
for x in products:
    price.append(x['price'])

for i in range(1,len(price)):
    key=price[i]
    j=i-1
    while j>=0 and price[j]>key:
        price[j+1]=price[j]
        j-=1
    price[j+1]=key
print(price)

stocks=[]
for y in products:
    stocks.append(y['stock'])
for k in range(len(stocks)):
    for l in range(0,len(stocks)-1-k):
        if stocks[l]>stocks[l+1]:
            stocks[l],stocks[l+1]=stocks[l+1],stocks[l]
print(stocks)

name=[]
for z in products:
    name.append(z['name'])

for m in range(len(name)):
    minpos=m
    for n in range(m,len(name)):
        if name[n]>name[minpos]:
            minpos=n
        name[n],name[minpos]=name[minpos],name[n]
print(name)

id=[]
for a in products:
    id.append(a['id'])
id.sort()

target=int(input('Enter product id'))

low=0
high=len(id)-1
found=False

while low<=high:
    mid=(high+low)//2
    if id[mid]==target:
        print(mid)
        found=True
        break
    elif id[mid]<target:
        low=mid+1
    elif id[mid]>target:
        high=mid-1

if found:
    for p in products:
        if p['id']==target:
            print(p)
else:
    print('Not found')

want=input('Enter name')
for b in products:
    if b=='':
        print('Found')
    else:
        print('Not present')

def range():
    l=int(input('Enter low  range'))
    h=int(input('Enter high range'))
    output=[]
    for c in products:
        if c['price']>l and c['price']<h:
            output.append((c['name'],c['price']))
    return output
print(range())

