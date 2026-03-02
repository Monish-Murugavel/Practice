'''products = [
    {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
    {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
    {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
]

def price():
    for i in range(1,len(products)):
        key=products[i]
        j=i-1
        while j>=0 and products[j]['price']>key['price']:
            products[j+1]=products[j]
            j-=1
        products[j+1]=key
    return products
print(price())

print()

def stock():
    for i in range(1,len(products)):
        key=products[i]
        j=i-1
        while j>=0 and products[j]['stock']<key['stock']:
            products[j+1]=products[j]
            j-=1
        products[j+1]=key
    return products
print(stock())

print()

def name():
    for i in range(1,len(products)):
        key=products[i]
        j=i-1
        while j>=0 and products[j]['name']>key['name']:
            products[j+1]=products[j]
            j-=1
        products[j+1]=key
    return products
print(name())

def prod_id():
    low=0
    high=len(products)-1
    target=int(input('Enter id'))
    found=False

    while low<=high:
        mid=(low+high)//2
        if products[mid]['id']==target:
            found=True
            return products[mid]
            break
        elif products[mid]['id']<target:
            mid=low+1
        elif products[mid]['id']>target:
            mid=high-1
    if not found:
        return('Target not found')
print(prod_id())

def lin_search():
    name=input('enter name')
    for i in products:
        if i['name']==name:
            return i
print(lin_search())

def range1():
    upper=int(input('Enter upper limit'))
    lower=int(input('Enter lower limit'))
    l=[]
    for i in products:
        if i['price']>lower and i['price']<upper:
            l.append((i['name'],i['price']))
    return l
print(range1())'''
        
books =[{"title": "The Hobbit", "author": "Tolk", "year": 1937},
    {"title": "The Globe", "author": "Muffy", "year": 1942},
    {"title": "The Earth", "author": "Dong", "year": 1911}]

def sort_title():
    for i in range(len(books)):
        minpos=i
        for j in range(i,len(books)):
            if books[j]['title']>books[minpos]['title']:
                minpos=j
                books[j],books[minpos]=books[minpos],books[j]
    return books
print(sort_title())

print()

def sort_author():
    for i in range(len(books)):
        minpos=i
        for j in range(i,len(books)):
            if books[j]['author']>books[minpos]['author']:
                minpos=j
                books[j],books[minpos]=books[minpos],books[j]
    return books
print(sort_author())

print()


def sort_year():
    for i in range(len(books)):
        minpos=i
        for j in range(i,len(books)):
            if books[j]['year']>books[minpos]['year']:
                minpos=j
                books[j],books[minpos]=books[minpos],books[j]
    return books
print(sort_year())


print()

def search_author():
    author=input('ENter author')
    l=''
    for i in books:
        if i['author']==author:
            l+=str(i)
    return(str(l))
print(search_author())