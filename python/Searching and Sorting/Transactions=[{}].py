transactions = [
    {"id": 1, "amount": 1000, "location": "NY"},
    {"id": 2, "amount": 4000, "location": "AB"},
    {"id": 3, "amount": 6000, "location": "CD"},
    {"id": 4, "amount": 3000, "location": "DY"},
    {"id": 2, "amount": 4000, "location": "AB"}
]

for i in range(len(transactions)):
    key=transactions[i]
    j=i-1
    while j>=0 and transactions[j]['amount']>key['amount']:
        transactions[j+1]=transactions[j]
        j-=1
    transactions[j+1]=key
x=transactions

for k in transactions:
    if k['amount']>1000:
        print(k)

loc=input('Enter location')
for m in transactions:
    if m['location']==loc:
        print(m)

for n in range(len(transactions)):
    key=transactions[n]
    o=n-1
    while o>=0 and transactions[o]['id']>key['id']:
        transactions[o+1]=transactions[o]
        o-=1
    transactions[o+1]=key
y=transactions

duplicates=[]
for p in range(len(y)-1):
    if y[p]['id']==y[p+1]['id']:
        duplicates.append(y[p])
print(duplicates)




