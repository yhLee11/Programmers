import sys
import heapq
INF=sys.maxsize
def solution(board):
    answer = 0
    start_cost=0
    start_node=[0,0]
    mat_size=len(board)
    dist=[[-1 for _ in range(mat_size)] for _ in range(mat_size)]
    dist[0][0]=[start_cost]

    q=[(start_cost,start_node,'R')]#start cost, start node,Right/Down

    while q:
        print('dist',dist)
        node=heapq.heappop(q)
        print(node)
        cur_cost,cur_node,dir=node[0],node[1],node[2]
        if cur_node[0]==mat_size-1 and cur_node[1]==mat_size-1:
            answer=dist[mat_size-1][mat_size-1]
            break

        if cur_node[0]<mat_size and cur_node[1]<mat_size:#범위를 벗어나지 않았을 때
            if cur_node[1]!=mat_size-1 and board[cur_node[0]][cur_node[1]+1]!=1:#Right
                next_node=[cur_node[0],cur_node[1]+1]
                if dir=='R':
                    heapq.heappush(q,(cur_cost+100,next_node,'R'))
                    dist[next_node[0]][next_node[1]]=cur_cost+100
                else:
                    heapq.heappush(q,(cur_cost+500,next_node,'R'))
                    dist[next_node[0]][next_node[1]]=cur_cost+500

            elif cur_node[0]!=mat_size-1 and board[cur_node[0]+1][cur_node[1]]!=1:#Down
                next_node=[cur_node[0]+1,cur_node[1]]
                if dir=='R':
                    heapq.heappush(q,(cur_cost+500,next_node,'D'))
                    dist[next_node[0]][next_node[1]]=cur_cost+500
                else:
                    heapq.heappush(q,(cur_cost+100,next_node,'D'))
                    dist[next_node[0]][next_node[1]]=cur_cost+100

            # else:
            #     if cur_node[0]==mat_size-1 and board[cur_node[0]][cur_node[1]+1]==1:
            #         heapq.heappush(q,)


    return print('ans',answer)
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
