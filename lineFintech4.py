from itertools import combinations
import numpy as np
def solution(needs, r):
    needs=np.array(needs).T
    # print(needs)
    comb=list(combinations(needs,r))
    # print(comb)
    res=-1
    for c in comb:
        arr1=c[0].tolist()
        arr2=c[1].tolist()
        if sum(arr1 and arr2)>res:
            res=sum(arr1 and arr2)
    return res