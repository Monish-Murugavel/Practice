packets = []
dict={}
def packet_fun():
    n=int(input('Number of inputs'))
    for i in range(n):
        m=int(input('Enter element'))
        packets.append(m)
    for i in packets:
        if packets.count(i)>1:
            dict.update({i:packets.count(i)})
    return(dict)
packet_fun()
print(packets)
print(dict)
