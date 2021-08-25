from collections import deque
def solution(cacheSize, cities):
    time = 0
    stk=deque()
    if cacheSize==0:
        time=len(cities)*5
        return time
    for c in cities:
        c=c.upper()
        if len(stk)==cacheSize:
            if c not in stk:
                time+=5
                stk.popleft()
                stk.append(c)
            else:
                time+=1
                stk.remove(c)
                stk.append(c)
        else:
            if c not in stk:
                time+=5
                stk.append(c)
            else:
                time+=1
                stk.remove(c)
                stk.append(c)
    return time
