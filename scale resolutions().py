resolutions = [
(1920 , 1080) ,
(1280 , 720) ,
(2560 , 1440)
]
factor = 0.5

def scale_resolution(resolutions, factor):
    l1=[]
    l2=[]
    for i in resolutions:
        width=i[0]*factor
        height=i[1]*factor
        l1.append(width)
        l2.append(height)
    return(list(zip(l1,l2)))
print(scale_resolution(resolutions, factor))
        

