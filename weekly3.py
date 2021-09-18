#bfs로 이어져 있는 영역 찾고 최대 길이로 정사각 행렬 만듬
#슬라이싱 -> 슬라이싱 된 정방행렬로 다익스트라?
from collections import deque
import numpy as np
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visit=[]
blocks=[]
def bfs(table,dim,i,j):
    global visit
    q=deque()
    q.append((i,j))
    cnt=1
    loc=[]
    while q:
        dim_cnt=0
        x,y=q.popleft()
        loc.append([x,y])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<dim and 0<=ny<dim and table[nx][ny] and not visit[nx][ny]:
                visit[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    print('loc',loc)
    print('cnt',cnt)
    #numpy 배열 만들어서 추가하기
    


def solution(game_board=[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], table=[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]):
    answer = -1
    cnt=0
    dim=len(table)
    global visit
    visit=[[False]*dim for _ in range(dim)]
    table=np.array(table)
    for i in range(dim):
        for j in range(dim):
            if table[i][j]==1 and not visit[i][j]:
                visit[i][j]=True
                bfs(table,dim,i,j)
                cnt+=1
    print('all count',cnt)
    # return print(answer)

solution()
