from collections import defaultdict as dd
def solution(ids, rept, k):
    singo=dd(list)
    recv=dd(int)
    for i in ids:
        singo[i]=[]
        recv[i]=0
    
    for i in rept:
        to,fm = i.split()
        if fm not in singo[to]:
            singo[to].append(fm)
            recv[fm]+=1
    ans=[0]*len(ids)
    for key,vnum in recv.items():
        # print(key,vnum)
        if vnum>=k:
            idx=0
            for kk,vlist in singo.items():
                if key in vlist:
                    # print(kk,vlist)
                    ans[idx]+=1
                    # print(ans)
                    
                idx+=1    
    # print(ans)
    return ans