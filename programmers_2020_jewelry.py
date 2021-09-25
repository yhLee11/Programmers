from collections import defaultdict
def solution(gems):
    start,end=0,0
    kinds=list(set(gems))
    num=[0]*len(kinds)
    cnt=0
    res=[]
    for i in range(len(gems)):
        num=[0]*len(kinds)
        zero=True
        start=i+1
        for j in range(i,len(gems)):
            idx=kinds.index(gems[j])
            num[idx]+=1
            for z in range(len(num)):
                if num[z]==0:
                    break
                if z==len(num)-1 and num[z]!=0:
                    zero=False
                    end=j+1
                    break
            if z==len(num)-1 and num[z]!=0:
                break
        if not zero:
            res.append((start,end))
    res.sort(key=lambda x:(x[1]-x[0],x[0]))
    return list(res[0])