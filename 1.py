def solution(price):
    #최소구입비용
    first=[[] for _ in range(len(price[0]))]
    res=0
    cost=1000000000
    for i,val in enumerate(price):
        one=[]
        c=0
        fi=0
        for elem in val:
            c+=elem
            first[fi].append((elem,i+1))
            fi+=1
        cost=min(cost,c)
    for i in first:
        r=sorted(i,key=lambda x: (x[0]))
        res+=r[0][0]
    return [res,cost]
