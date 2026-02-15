curr={"USD": 1.0, "EUR": 0.92, "JPY": 155.5, 'IND':82.5} 
a=int(input('Enter amount'))
b=input('Enter curr1')
c=input('Enter curr2')

x=curr.get(b)
y=curr.get(c)

output=(a*y)/x
print(output)
    