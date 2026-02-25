l1=[2,4,5,3,1]
def insertion_sort(l1):
    for i in range(1,len(l1)):
        key=l1[i]
        j=i-1
        while j>=0 and l1[j]>key:
            l1[j+1]=l1[j]
            j-=1
        l1[j + 1] = key
    return l1
print(insertion_sort(l1))