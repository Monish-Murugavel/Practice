books =[{"title": "The Hobbit", "author": "Tolk", "year": 1937},
    {"title": "The Globe", "author": "Muffy", "year": 1942},
    {"title": "The Earth", "author": "Dong", "year": 1911}]

'''for i in range(1,len(books)):
    key=books[i]
    j=i-1
    while j>=0 and books[j]['title']>key['title']:
        books[j+1]=books[j]
        j-=1
    books[j+1]=key
print(books)

for k in range(len(books)):
    minpos=k
    for l in range(k,len(books)):
        if books[l]['author']>books[minpos]['author']:
            minpos=l
        books[l],books[minpos]=books[minpos],books[l]
print(books)

for m in range(len(books)):
    for n in range(0,len(books)-1-m):
        if books[n]['year']>books[n+1]['year']:
            books[n],books[n+1]=books[n+1],books[n]
print(books)

target=input('Enter author name')
low=0
high=len(books)-1
found=False

while low<=high:
    mid=(high+low)//2
    if books[mid]['author']==target:
        print(books[mid])
        found=True
        break
    elif books[mid]['author']<target:
        low=mid+1
    elif books[mid]['author']>target:
        high=mid-1

if not found:
    print('Not found')'''
    
target=input('Enter author name')
found=False
for i in range(len(books)):
    if target==books[i]['author']:
        print(books[i])
        found=True

if not found:
    print('Not found')

word=input('Enter words')
for j in range(len(books)):
    if word in books[j]['title']:
        print(books[j])

early=[]
for k in books:
    early.append(k['year'])
min=min(early)
for l in range(len(books)):
    if books[l]['year']==min:
        print(books[l])








