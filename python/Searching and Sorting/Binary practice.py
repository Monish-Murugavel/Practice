list=[1,2,3,4,5,6,7,8]
low=0
high=len(list)-1
found=False

target=int(input('Enter num'))

while low<=high:
    mid=(low+high)//2

    if list[mid]==target:
        print(mid)
        found=True
        break

    elif list[mid]<target:
        low=mid+1
    elif list[mid]>target:
        high=mid-1

if not found:
    print('Not found')

    

