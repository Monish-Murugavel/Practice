products = [
    {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
    {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
    {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
]

def bubblesort():
    for i in range(len(products)-1):
        for j in range(0,len(products)-i-1):
            if products[j]['id']>products[j+1]['id']:
                products[j],products[j+1]=products[j+1],products[j]
    return products
print(bubblesort())

def selectionsort():
    for i in range(len(products)):
        minpos=i
        for j in range(i,len(products)):
            if products[j]['id']>products[minpos]['id']:
                minpos=j
                products[j],products[minpos]=products[minpos],products[j]
    return products
print(selectionsort())

def insertionsort():
    for i in range(1,len(products)):
        key=products[i]
        j=i-1
        while j>=0 and products[j]['id']>key['id']:
            products[j+1]=products[j]
            j-=1
        products[j+1]=key
    return products
print(insertionsort())

def binarysearch():
    high=len(products)-1
    low=0
    target=int(input('Enter id'))
    while low<high:
        mid=(low+high)//2
        if products[mid]['id']==target:
            return products[mid]
            break
        elif products[mid]['id']<target:
            low=mid+1
        else:
            high=mid-1
print(binarysearch())