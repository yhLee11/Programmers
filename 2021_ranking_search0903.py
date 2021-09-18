from itertools import combinations
def solution(info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]):
    lst=[]
    for i in info:
        lst.append(i.split(' '))

    lst.sort(key=lambda x: [x[0],x[1],x[2],x[3],x[4]])
    print(lst)

    q=[]
    for i in query:
        line=i.split(' and ')
        food,score=line[-1].split(' ')
        line[-1]=food
        line.append(int(score))
        q.append(line)
    # print(q)
    cnt=0
    for i in q:
        for elem in i:
            if elem!='-':
                for l in lst:
                    if elem==

solution()
