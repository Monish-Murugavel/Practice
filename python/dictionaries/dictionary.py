dict={}
r=1
num=int(input('Enter number"'))

while r<num:
    a=int(input('Enter key'))
    b=int(input('Enter value'))
    dict.update({a:b})
    r+=1
#1
while r<num+1:
    dict.update({r:r*r})
    r+=1
print(dict)

#2
l=dict.values()
print(sum(l))

#3
str=input('Enter string')
for i in str:
    dict.update({i:str.count(i)})
print(dict)

#4
pt={'H':[14,20],'He':[1,4],'Li':[453,1603]}

ele=input('Enter element')
temp=int(input('Enter temp'))
x=pt.get(ele)
if temp<=x[0]:
        print('Solid')
elif temp>x[0] and temp<x[1]:
        print('Liquid')
elif temp>=x[1]:
        print('Gas')

#5
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


curr={"USD": 1.0, "EUR": 0.92, "JPY": 155.5} 
a=int(input('Enter amount'))
b=input('Enter curr1')
c=input('Enter curr2')
if b=='USD' and c=='EUR'

