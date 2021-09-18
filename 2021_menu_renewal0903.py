from collections import Counter
from itertools import combinations
def solution(orders=["XYZ", "XWY", "WXA"], course=[2,3,4]):

    for i in range(len(orders)):
        orders[i]=sorted(list(orders[i]))

    res=[]
    for c in course:
        cnt={}
        comb=[]
        for od in orders:
            comb+=list(combinations(od,c))
        if comb:
            cnt=Counter(comb)
            print(cnt)
            most=cnt.most_common()
            most=most[0][1]
            if most==1:continue
            for k,v in cnt.most_common():
                if v<most:break
                # print(k,v)
                res.append(k)
    lst=[]
    for i in res:
        i="".join(i)
        lst.append(i)
    return sorted(lst)
print(solution())
