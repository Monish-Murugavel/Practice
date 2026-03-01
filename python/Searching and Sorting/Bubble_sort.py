'''a=[3,2,5,3,7,4,7,4,2,1]
p=0
while p<len(a):
    swap=0
    while swap<len(a)-p-1:
        if a[swap]>a[swap+1]:
            t=a[swap]
            a[swap]=a[swap+1]
            a[swap+1]=t
            swap+=1
        p+=1
print(a)'''


def bubbleSort(arr):
    n=len(arr)
    swapped=False

    for i in range(n-1):
        for j in range(0,n-1-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
            if not swapped:
                return
    return(arr)
arr=[64,34,25,12,22,11,90]
print(bubbleSort(arr))
        