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

print((solution([1,1,1,1,1],5)))
