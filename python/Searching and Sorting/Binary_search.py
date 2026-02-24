import array as arr
arr=arr.array('i',[1,2,3,4,5,6,7,8,9])
target=int(input('Enter no.'))
def binary_search():
    
    low=arr[0]
    high=arr[-1]
    mid=(high+low)//2
    
    while low<=high:
        if arr[mid]==target:
            return mid
        elif arr[mid]>=target:
            high=mid+1
            return mid
        elif arr[mid]<=target:
            low=mid
            return mid
    

print(binary_search())

