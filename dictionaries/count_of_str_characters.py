dict={}
str=input('Enter string')
for i in str:
    dict.update({i:str.count(i)})
print(dict)