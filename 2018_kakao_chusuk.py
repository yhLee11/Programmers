import datetime as dt
import time
def solution(lines=[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]):
    cnt=0
    res=0
    timeline=[]
    for i in lines:
        day,S,T=i.split()
        h,m,s=S.split(":")
        s1,s2=s.split('.')
        s2=float('0.'+s2)
        s1=int(s1)
        h=int(h)
        m=int(m)
        T=T.strip('s')
        T=float(T)

        total=h*(3600)+m*(60)+s1*(1000)+s2
        # print(total)
        T=T*1000
        # print(T)

        timeline.append((total-T+0.001,total,T))#ms

    # print(timeline)
    last=timeline[-1][1]

    for i in range(int(timeline[0][0]),int(last),1000):
        res=max(res,cnt)
        cnt=0
        i*=1000
        print(i)
        for j in timeline:
            print(j[0]*1000)
            if j[0]*1000 in range(i,i+1001) or j[1]*1000 in range(i,i+1001):
                cnt+=1
                print(j[0]*1000,j[1]*1000)

    print(res)
    # return
solution()
