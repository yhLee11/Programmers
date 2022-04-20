import sys
from collections import deque
dx=[1,-1,0,0]#right, down
dy=[0,0,1,-1]
MAX=sys.maxsize
ans=MAX
def bfs(board):
    q=deque()
    size=len(board)
    visit=[[[MAX for _ in range(size)] for _ in range(size)] for _ in range(4)]
    #dir=0,1,2,3 밑,오른쪽,왼쪽,위
    for z in range(4):
        visit[z][0][0]=0
        
    if board[0][1]!=1:#1오른쪽
        q.append((0,1,100,1))
        visit[1][0][1]=100
        
    if board[1][0]!=1:#0밑
        q.append((1,0,100,0))
        visit[0][1][0]=100
        
    while q:
        x,y,c,d=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if d!=i:
                nc=c+600
            else:
                nc=c+100
            if 0<=nx<size and 0<=ny<size and board[nx][ny]!=1 and visit[i][nx][ny]>nc:
                q.append((nx,ny,nc,i))
                visit[i][nx][ny]=nc
    global ans
    for i in range(4):
        ans=min(ans,visit[i][size-1][size-1])
        
    return ans
def solution(board):
    return bfs(board)