def solution(lto, wnum):
    win={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    zero=0
    for i in lto:
        if i==0:
            zero+=1
        if i in wnum:
            wnum.pop(wnum.index(i))
    wcnt=6-len(wnum)#당첨확정개수
    if wcnt==6:
        return [1,1]
    elif wcnt+zero<=6:
        return [win[wcnt+zero],win[wcnt]]
