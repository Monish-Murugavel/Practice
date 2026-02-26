bus=[]
n=int(input('Enter number of buses'))
for i in range(n):
    d={}
    bus_id=input('Enter bus id')
    route=input('Enter route')
    trips=int(input('Enter np of treips'))
    avg=int(input('enter avg mins'))
    depot=input('Enter station')
    d['BUSID']=bus_id
    d['Route']=route
    d['Trips Completed']=trips
    d['Avg Delay']=avg
    d['Depot']=depot
