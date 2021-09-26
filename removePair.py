from collections import deque
def solution(s):
    tmp=list(s)
    q=deque()
    for i in tmp:
        if not q:
            q.append(i)
        elif q[-1]==i:
            q.pop()
        else:
            q.append(i)
    print(q)
    return 1 if not q else 0
