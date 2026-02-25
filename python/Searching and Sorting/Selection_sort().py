l1=[3,5,2,4,1]
def selection_sort():
    for i in range(len(l1)):
        minpos=i
        for j in range(i,len(l1)):
            if l1[j]<l1[minpos]:
                minpos=j
        temp=l1[i]
        l1[i]=l1[minpos]
        l1[minpos]=temp
    return l1
print(selection_sort())


