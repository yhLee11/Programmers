board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
import numpy as np

def solution(board, moves):
    answer = 0
    stk=[]
    for i in range(len(board)):
        line=[]
        for j in range(len(board)):
            if board[j][i]==0: continue
            line.append(board[j][i])
        stk.append(line)


    res=[]
    for idx in moves:
        if not stk[idx-1]:#list is empty
            continue

        item=stk[idx-1].pop(0)
        if res and res[-1]==item:
            res.pop()
            answer+=2
        else:
            res.append(item)

    return answer
