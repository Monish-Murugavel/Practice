pt={'H':[14,20],'He':[1,4],'Li':[453,1603]}

ele=input('Enter element')
temp=int(input('Enter temp'))
x=pt.get(ele)
if temp<=x[0]:
        print('Solid')
elif temp>x[0] and temp<x[1]:
        print('Liquid')
elif temp>=x[1]:
        print('Gas')