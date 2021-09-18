#H-index
def solution(citations):
    citations.sort()
    cnt=0
    if sum(citations)==0:return 0
    for i in reversed(citations):
        if i>=cnt:
            cnt+=1
        else:break

    return cnt
