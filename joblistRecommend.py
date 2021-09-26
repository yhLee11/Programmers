from collections import defaultdict
def solution(table, languages, pref):
    res=[]
    ans=[0]*len(table)
    table_name=[]
    for idx,lg in enumerate(languages):
        res=[]
        for t in table:
            t=t.split(' ')
            name=t[0]
            table_name.append(name)
            point=defaultdict(int)
            for i in range(1,len(t)):
                point[t[i]]=6-i
            if lg in point:
                res.append((name,pref[idx]*point[lg]))
            else:
                res.append((name,0))
        for i,r in enumerate(res):
            ans[i]+=r[1]

        print(ans)

    rrr=list(zip(table_name,ans))
    rrr.sort(key=lambda x:(-x[1],x[0]))
    return rrr[0][0]
