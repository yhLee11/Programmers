def solution(s):
    answer = []
    s=s[2:-2]
    s=s.split('},{')
    line=[]
    #print(s)

    lst=[]
    for elem in s:
        line=list(map(int,elem.split(',')))
        lst.append((len(line),line))
    lst.sort(key=lambda x: (x[0],x[1]))

    #print(lst)

    for tu in lst:
        for i in tu[1]:
            if i in answer:
                continue
            else:
                answer.append(i)

    return answer
