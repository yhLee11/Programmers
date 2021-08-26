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
"""
combinations: 조합
Counter: 딕셔너리 형태로 요소 개수 확인 가능
.mostcommon(): value 개수가 가장 많은 순으로 리스트 반환
"""
