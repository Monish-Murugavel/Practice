
def distribute_tasks(server_loads, new_tasks):
    while new_tasks>0:
        for i in range(len(server_loads)):
            if server_loads[i]==min(server_loads):
                server_loads[i]+=1
                new_tasks-=1
    return(server_loads)
print(distribute_tasks([10 , 5 , 2 , 8],(int(input('ENter number of task')))))
            