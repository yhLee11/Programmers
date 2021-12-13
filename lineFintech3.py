import math
def solution(x, y):
    cord=[]
    for i in range(len(x)):
        cord.append((x[i],y[i]))
    cord.sort(key=lambda a:(a[0],a[1]))#x기준->y기준
    print(cord)
    dis=[]
    for c in range(1,len(cord)):
        dis.append(math.dist(cord[c-1],cord[c]))
    dis.sort(reverse=True)
    return math.ceil(dis[0])