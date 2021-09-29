import sys
from collections import deque
dic={0:(0,-1),1:(0,1),2:(-1,0),3:(1,0)}
def solution(board):
    #직선:100, 코너:500, 최소비용
    length=len(board)
    def bfs(i,j,D,C):#x,y,direction,cost
        q=deque()
        q.append((i,j,D,C))
        visit=[[sys.maxsize]*length for _ in range(length)]
        while q:
            x,y,d,c=q.popleft()
            for i in range(4):
                nx=x+dic[i][0]
                ny=y+dic[i][1]
                if 0<=nx<length and 0<=ny<length and board[nx][ny]==0:
                    nextcount=c+100 if i==d else c+600
                    if nextcount<visit[nx][ny]:
                        visit[nx][ny]=nextcount
                        q.append([nx,ny,i,nextcount])
        return visit[-1][-1]

    right=bfs(0,0,3,0)
    bottom=bfs(0,0,1,0)
    return min(right,bottom)
