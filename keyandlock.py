"""https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python"""
import numpy as np
def rotate90(arr):
    return list(zip(*arr[::-1]))
def attach(x,y,M,rkey,maps):
    for i in range(M):
        for j in range(M):
            maps[i+x][j+y]+=rkey[i][j]
def detach(x,y,M,rkey,maps):
    for i in range(M):
        for j in range(M):
            maps[i+x][j+y]-=rkey[i][j]
def check(M,N,maps):
    for i in range(N):
        for j in range(N):
            if maps[M+i][M+j]!=1:
                return False
    return True
def solution(key, lock):
    M,N=len(key),len(lock)
    maps=[[0]*(M*2+N) for _ in range(M*2+N)]
    for i in range(N):
        for j in range(N):
            maps[M+i][M+j]=lock[i][j]
    # print(np.array(maps))

    rkey=key
    for _ in range(4):
        rkey=rotate90(rkey)
        for i in range(1,M+N):
            for j in range(1,M+N):
                attach(i,j,M,rkey,maps)
                if check(M,N,maps): return True
                detach(i,j,M,rkey,maps)
    return False
