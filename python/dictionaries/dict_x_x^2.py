dict={}
r=1
num=int(input('Enter number"'))

while r<num+1:
    dict.update({r:r*r})
    r+=1
print(dict)