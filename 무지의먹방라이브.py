import heapq as hq
def solution(times, k):
    if sum(times)<=k:
        return -1
    
    q=[]
    for i in range(len(times)):
        hq.heappush(q,(times[i],i+1))
        
    muk_time=0#먹기 위해 사용한 시간
    prev=0#직전에 다 먹은 음식 시간
    length=len(times)
    
    while muk_time+((q[0][0]-prev)*length)<=k:
        now=hq.heappop(q)[0]
        muk_time+=(now-prev)*length
        length-=1#다 먹은 음식 제외
        prev=now#이전 음식 시간 재설정
    
    res=sorted(q,key=lambda x:x[1])#음식 번호 기준 정렬
    return res[(k-muk_time)%length][1]
    