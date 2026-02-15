num=int(input('Enter num'))
def perfect_num(num):
    l=[]
    for i in range(num):
        if i==0:
            continue
        elif num%i==0:
            l.append(i)
    if sum(l)==num:
        return(True)
    else:
        return(False)
print(perfect_num(num))
