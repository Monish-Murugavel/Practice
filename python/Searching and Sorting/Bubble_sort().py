l1=[3,4,2,5,1]
def bubblesort(l1):
    for i in range(len(l1)-1):
        for j in range(0,len(l1)-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1
print(bubblesort(l1))
