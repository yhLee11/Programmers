def solution(pg, speeds):
    leftover,ans=[],[]
    for i in range(len(pg)):
        a,b=divmod(100-pg[i],speeds[i])
        if b==0:
            leftover.append(a)
        else:
            leftover.append(a+1)
    
    maxnum=leftover[0]
    idx=1
    for i in leftover[1:]:
        if maxnum<i:
            leftover=leftover[idx:]
            ans.append(idx)
            maxnum=i
            idx=0
        idx+=1
    if leftover:
        ans.append(len(leftover))
    return ans