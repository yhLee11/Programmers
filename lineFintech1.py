import itertools 
def solution(arr):
    res=[0,0]
    hap=[]
    hap.append(arr[0])
    hap.append(arr[0]+arr[1])
    if hap[0]>0:res[0]=1
    if hap[1]>0:res[1]=1
    for i in range(2,len(arr)):
        hap.append(hap[i-1]+arr[i])
        if hap[i]>0:
            res.append(1)
        else:
            res.append(0)
    return sum(res)