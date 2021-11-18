def solution(n,a,b):
    #1,2,3,4,5,6,7,8
    #1,2(4),5,4(7)
    cnt=0
    while a!=b:
        a=(a+1)//2
        b=(b+1)//2
        cnt+=1
        # print(a,b)
    return cnt