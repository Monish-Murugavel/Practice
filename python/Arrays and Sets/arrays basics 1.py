import array as arr
a=arr.array('i',[1,3,5,6,3,6,9,2])

#sum
b=0
for i in range(len(a)):
    b+=a[i]
print(b)


#Max,Min
x=[]
sorted_list=sorted(a)
print('largest=',sorted_list[0],'smallest=',sorted_list[-1])


#Even,Odd
odd=0
even=0
for k in a:
    if k%2==0:
        odd+=k
    else:
        even+=k
print('sum of odd is',odd,'sum of even is',even)


#Pair with highest product
#Using list
l1=[]
l2=[]
for l in a:
    l1.append(l)
    for m in l1:
        if m==l:
            pass
        else:
            l2.append(l*m)
print(max(l1),int(max(l2)/max(l1)),max(l2))


#Without list
h1=0
h2=0
for n in a:
    if n>h1:
        h1=n
for n in a:
    if n>h2 and h1!=n:
        h2=n
print(h1,h2,h1*h2)

#Duplicates
unique=list(set(a))
unique_arr=arr.array('i',unique)
print(unique_arr)

unique_arr2=arr.array('i',[])
for o in a:
    if o not in unique_arr2:
        unique_arr2.append(o)
print(unique_arr2)














