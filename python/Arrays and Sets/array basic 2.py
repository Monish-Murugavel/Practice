import array as arr
a=arr.array('i',[2,4,3,5,3,3,7,9,8,7])

#6.reverse
print(a[::-1])

index=-1
for i in a:
    print(a[index],end='')
    index-=1
print()

#7.Avg,Count
avg=sum(a)/len(a)
count=0
for j in a:
    if j>avg:
        count+=1
print('avg=',avg,', count=',count)

#med ques 1
import array as arr
a=arr.array('i',[3,2,7,0,8,0,9,3,0,7,8])
zeros=[]
for i in a:
    if i==0:
        a.remove(i)
        zeros=zeros+[0]
a.extend(zeros)
print(a)


