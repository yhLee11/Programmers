def solution(n, t, m, timetable):
    busTime=[]
    startTime=9*60
    lastTime=23*60+59
    busTime.append(startTime)
    cur=startTime
    
    while True:
        cur+=t
        if cur>lastTime or len(busTime)==n:break
        busTime.append(cur)

    for idx,val in enumerate(timetable):
        hour,minutes=map(int,val.split(":"))
        tmp=hour*60+minutes
        timetable[idx]=tmp
    
    timetable.sort(key=lambda x:-x)
    
    cur_time=busTime[0]
    al=[]
    for bt in busTime:
        busin=[]
        cnt=0
        if timetable:
            while cnt<m:
                if timetable and timetable[-1]<=bt:
                    cnt+=1
                    busin.append(timetable.pop())
                else:
                    break
            al.append(busin)
        else:break

    if len(busin)==m:
        ans=busin[-1]-1
        hour,minutes=divmod(ans,60)
    else:
        ans=busTime[-1]
        hour,minutes=divmod(ans,60)
        
    if len(str(hour))==1:
        hour='0'+str(hour)
    if len(str(minutes))==1:
        minutes='0'+str(minutes)
        
    return str(hour)+":"+str(minutes)
