def dfs(n,com,vis,start):
    stack=[start]
    while stack:
        k=stack.pop()

        if vis[k]==0:
            vis[k]=1

        for i in range(n):
            if vis[i]==0 and com[k][i]==1:
                stack.append(i)
def solution(n, computers):
    answer = 0
    v=[0]*n

    for i in range(n):
        if v[i]==0:
            dfs(n,computers,v,i)
            answer+=1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
