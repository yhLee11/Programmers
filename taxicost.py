import sys
def solution(n, s, a, b, fares):
    INF=int(1e9)
    maps=[[INF]*(n) for _ in range(n)]
    for i in range(n):#자기자신으로 가는 길 0
        maps[i][i]=0
    for f in fares:
        maps[f[0]-1][f[1]-1]=f[2]
        maps[f[1]-1][f[0]-1]=f[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i!=j:#최소 비용
                    temp=min(maps[i][j],maps[i][k]+maps[k][j])
                    maps[i][j]=maps[j][i]=temp

    #경유지점에 따라 최소 합승 비용 탐색
    ans=INF
    for i in range(n):
        temp=maps[s-1][i]+maps[i][b-1]+maps[i][a-1]
        ans=min(ans,temp)
    return ans
