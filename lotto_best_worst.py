def solution(lottos, win_nums):
    dic={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt=0
    zero=0
    for lt in lottos:
        if lt==0:zero+=1
        if lt in win_nums:
            cnt+=1
    best=cnt+zero
    worst=cnt
    print(best,worst)
    return [dic[best],dic[worst]]
