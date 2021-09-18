def solution(info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]):
    answer = []
    db=[]
    for i in info:
        db.append(i.split())

    #db.sort(key=lambda x:[x[0],x[1],x[2],x[3],x[4]])
    # print(db)

    search=''
    for q in query:
        q=q.replace('and','')
        search=q.split()
        # print(search)
        cnt=0
        for i in search:
            if i=='-':
                continue
            db.sort(key=lambda x:)
            print(db)
            break
        break

    # return print(answer)
solution()
