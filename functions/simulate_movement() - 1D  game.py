size=int(input('Ennter size of board'))
x=int(input('Total number of moves'))
moves=[]
while x>0:
    m=int(input('Enter move'))
    x-=1
    moves.append(m)
def simulate_movement(size, moves):
    total=sum(moves)
    if  total<0:
        return('0')
    if total>size:
        return(size-1)
    else:
        return(total)
    
print(simulate_movement(size, moves))






    
