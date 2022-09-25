from collections import defaultdict as dd
import math
def solution(fees, rcd):
    #default time, over time
    dtime,dfee,otime,ofee=fees[0],fees[1],fees[2],fees[3]
    lst=[]
    dic=dd(list)
    for r in rcd:
        tmp=r.split(" ")
        h,m=map(int,tmp[0].split(":"))
        time=h*60+m
        dic[tmp[1]].append(time)
    # print(dic)
    res=dd(int)
    for k,v in dic.items():
        if len(v)%2==1:
            dic[k].append(24*60-1)
        tsum=0
        for i in range(0,len(v),2):
            tmp=v[i+1]-v[i]
            tsum+=tmp
        over=tsum-dtime
        # print(k,tsum,dtime,over)
        if over<0:
            res[k]=dfee
        else:
            final=dfee+math.ceil(over/otime)*ofee
            res[k]=final
    res=sorted(res.items())
    # print(res)
    ans=[]
    for num,val in res:
        ans.append(val)
    return ans