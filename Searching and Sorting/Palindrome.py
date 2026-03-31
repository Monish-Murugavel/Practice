a=['apple','banana','carrot','mango','kiwi']
b=[1,2,3,4,5,6,7,8,9]
c=[]
new=[i for i in a if 'a' in i]
print(new)

print(max(b))
print(min(b))
print(a.reverse())
print(new)
print(len(new))

if a==a.reverse():
    print('Yes Palendrome')
else:
    print('Not a Palendrome')

print(sum(b))
print(a.extend(b))

for j in a:
    c.append(j)
    d=d+'j'
    for k in b:
        
        print(c)




