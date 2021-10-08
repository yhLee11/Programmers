# def dfs(n,com,vis,start):
#     stack=[start]
#     while stack:
#         k=stack.pop()
#
#         if vis[k]==0:
#             vis[k]=1
#
#         for i in range(n):
#             if vis[i]==0 and com[k][i]==1:
#                 stack.append(i)
# def solution(n, computers):
#     answer = 0
#     v=[0]*n
#
#     for i in range(n):
#         if v[i]==0:
#             dfs(n,computers,v,i)
#             answer+=1
#
#     return answer
#
# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
def dfs(node,n,v,computers):
    stk=[node]
    while stk:
        k=stk.pop()
        if v[k]==False:
            v[k]=True
        for i in range(n):
            if v[i]==False and computers[k][i]==1:
                stk.append(i)
def solution(n=3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]):
    ans=0
    v=[0]*n
    for i in range(n):
        if v[i]==False:
            dfs(i,n,v,computers)
            ans+=1
    print(ans)
solution()
