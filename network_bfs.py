from collections import deque
def solution(n, computers):
    def bfs(a):
        q=deque([a])
        while q:
            node=q.popleft()
            visit[node]=1
            for i in range(n):
                if not visit[i] and computers[node][i]:
                    q.append(i)

    visit=[0]*(n)
    cnt=0
    for i in range(n):
        if not visit[i]:
            bfs(i)
            cnt+=1
    return cnt
