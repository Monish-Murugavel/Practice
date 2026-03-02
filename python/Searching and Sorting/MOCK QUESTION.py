data=[{'BUS ID':'B201','Route':'Route A','Trip Completed':42, 'Avg_delay':3,'Depot':'Central'},
      {'BUS ID':'B202','Route':'Route B','Trip Completed':35, 'Avg_delay':6,'Depot':'North'},
       {'BUS ID':'B203','Route':'Route C','Trip Completed':50, 'Avg_delay':2,'Depot':'Central'},
        {'BUS ID':'B204','Route':'Route D','Trip Completed':28, 'Avg_delay':8,'Depot':'South'}]

def find_busid():
    want=input('enter busid')
    for i in data:
        if i['BUS ID']==want:
            return(i)
print(find_busid())
        
def comp_trips():
    for j in range(len(data)):
        for k in range(0,len(data)-j-1):
            if data[k+1]['Trip Completed']>data[k]['Trip Completed']:
                data[k],data[k+1]=data[k+1],data[k]
    return(data)
print(comp_trips())

def find_route():
    l1=[]
    find=input('ENter Route')
    for l in data:
        if l['Route']==find:
            l1.append(l)
    return(l1)
print(find_route())

def avg_del():
    l2=[]
    for m in data:
        if m['Avg_delay']<5:
            l3=[]
            l3.append((m['Trip Completed']))
            l4=sum(l3)/len(l3)
            l2.append((m['Route'],l4))
    return l2
print(avg_del())

def high_rel():
    l5=[]
    for o in data:
        if o['Trip Completed']>40 and o['Avg_delay']<=4:
            l5.append(o)
    return l5
