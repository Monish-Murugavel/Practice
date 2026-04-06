r=open("sample.txt",'r')
x=r.read()
r.close()
print(x)

r=open("sample.txt",'r')
y=r.readlines()

r.close()
print(y)

r=open("sample.txt",'r')
z=r.readlines(5)
for i in z:
    print(i)
r.close()

r=open('sample.txt','r')
s=open('sample2.txt','w')
a=r.read()
s.write(a)
r.close()
s.close()

s=open('sample2.txt','r')
b=s.read()
print(b)
s.close()

r=open('sample.txt','r')
p=r.readline()
q=p.split(' ')
count=0
for j in q:
    count+=1
print(count)
r.close()

r1=open('y:\sample3.txt','r')
a1=r1.read()
a2=[]
a3=[]
for i in a1:
    a2.append(int(i))
r1.close()
r2=open('y:\sample3.txt','a')
r2.write(str(sum(a2)))
r2.close()

r2=open('y:\sample3.txt','r')
b=r2.read()
print(b)
print(a2)