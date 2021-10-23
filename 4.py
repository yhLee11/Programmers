def solution(vac, peo):
    vacinfo,res=dict(),dict()
    for i in vac:
        lst=i.split(' ')
        vacinfo[lst[0]]={'stock':int(lst[1]),'age':range(int(lst[2]),int(lst[3])+1)}
        res[lst[0]]=[]
    people=[]
    order=1
    for i in peo:
        lst=i.split(' ')
        oneP=[]
        oneP.append(order)
        oneP.append(lst[0])
        oneP.append(int(lst[1]))
        oneP.append(lst[2:])
        people.append(oneP)
        order+=1
    people.sort(key=lambda x: [-x[2],x[0]])

    ans=[]
    for i in people:
        vaclst=i[-1]
        page=i[2]
        for v in vaclst:
            if vacinfo[v]['stock']>0 and i[2] in vacinfo[v]['age']:
                vacinfo[v]['stock']-=1
                res[v].append(i[1])
                break
    rr=[]
    vacK=sorted(list(res.keys()))
    for k in vacK:
        if res[k]:
            vacV=sorted(res[k])
            oneVac=[k]+vacV
            rr.append(' '.join(oneVac))
    return rr
