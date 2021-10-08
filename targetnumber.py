#SOL1
from collections import deque
def solution(numbers, target):
    answer = 0
    dq=deque([(0,0)])#합과 깊이

    while dq:
        sum,level=dq.popleft()

        if level > len(numbers):
            break
        elif level==len(numbers) and sum==target:
            answer+=1
        dq.append((sum+numbers[level-1],level+1))
        dq.append((sum-numbers[level-1],level+1))

    return answer
#SOL2
ans=0
def solution(numbers, target):
    global ans
    def dfs(idx,val):
        global ans
        if len(numbers)==idx and target==val:
            ans+=1
            return
        if len(numbers)==idx:
            return
        dfs(idx+1,val+numbers[idx])
        dfs(idx+1,val-numbers[idx])
    dfs(0,0)
    print(ans)
    return ans
