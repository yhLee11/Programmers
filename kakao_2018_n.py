def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
def solution(n=2, t=4, m=2, p=1):
    res=[]
    num=0
    for i in range(t*m):
        num=convert(i,n)
        for j in num:
            res.append(j)

    ans=''
    for i in range(p-1,t*m,m):
        ans+=res[i]

    print(ans)

solution()
