from itertools import combinations
from collections import Counter
def solution(orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], course=[2,3,4]):
    answer=[]
    for k in course:
        temp=[]
        for ord in orders:
            comb=combinations(sorted(ord),k)
            temp+=comb

        counter=Counter(temp)
        if len(counter)!=0 and max(counter.values())!=1:
            answer+=[''.join(f) for f in counter if counter[f]==max(counter.values())]
    return sorted(answer)
print(solution())
