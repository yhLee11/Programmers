def solution(m=4, n=5, board=["CCBDE", "AAADE", "AAABF", "CCBBF"]):
    b=list(map(list,zip(*board)))
    cnt=0
    print(b)
    pop_set=set()
    while True:
        pop_set=set()
        for i in range(n-1):
            for j in range(m-1):
                if b[i][j]==b[i][j+1]==b[i+1][j]==b[i+1][j+1]!='_':
                    pop_set|=set([(i,j),(i,j+1),(i+1,j),(i+1,j+1)])#합집합
        if not pop_set:break

        for i,j in pop_set:
            b[i][j]=0
        for i,row in enumerate(b):
            empty=['_']*row.count(0)
            b[i]=empty+[block for block in row if block!=0]

        cnt+=len(pop_set)
    return cnt
print(solution())
