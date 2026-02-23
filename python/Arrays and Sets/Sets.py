a={1,2,3,4,5}
b={4,5,6,7,8}
for i in a:
    if i not in b:
        print(i,end=' ')
print()
for j in b:
    if j not in a:
        print(j,end=' ')
print()

missing_in_first=a-b
missing_in_second=b-a
print(missing_in_first)
print(missing_in_second)

#Unique words
words=['Red','Blue','Green','Red','Red','Green']
key=[]
set_words=set(words)
for i in set_words:
    key.append(words.count(i))
result=dict(zip(set_words,key))
print(result)

#Removing intersection
intersection_of_a=a-b
intersection_of_b=b-a

print(intersection_of_a)
print(intersection_of_b)










