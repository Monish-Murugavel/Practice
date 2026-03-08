plant=[{1:'Hibiscus', 'Unit Price':100, 'Colours available':('Red', 'White', 'Pink', 'Violet', 'Orange','Yellow')},
    {2:'Rose','Unit Price': 200, 'Colours available':('Red', 'White', 'Maroon', 'Yellow')},
    {3:'Marigold','Unit Price': 50,'Colours available':('Orange', 'Yellow')},
    {4: 'Dahlia','Unit Price': 150, 'Colours available':('Red', 'White', 'Pink')}]
def vari():
    l=0
    for i in plant:
        x=i['Colours available']
        y=len(x)
        l=y

    for j in plant:
        if len(j['Colours available'])==l:
            return(plant[j])
print(vari())


            
