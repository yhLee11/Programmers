from collections import deque
import numpy as np
def solution(maps):
    row,col=len(maps),len(maps[0])
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    q=deque()
    q.append((0,0))
    visit=[[-1]*col for _ in range(row)]
    visit[0][0]=1
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<row and 0<=ny<col and maps[nx][ny]==1:
                if visit[nx][ny]==-1:
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))

    print(np.array(visit))
    return visit[-1][-1]
