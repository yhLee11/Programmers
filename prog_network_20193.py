def solution(user_id, banned_id):
    answer = 0
    bandic={}
    star=True

    for id in banned_id:#{5:["fr*d*","*rodo"]}
        if len(id) in bandic:
            bandic[len(id)]+=[id]
        else:
            bandic[len(id)]=[id]
    res=[]
    cnt=0
    for user in user_id:#유저아이디 하나 골랐음
        banlst=set(bandic.get(len(user)))#길이가 5인 벤아이디
        print('user',user,'banlst',banlst)
        possible=[]
        for ban in banlst:
            star=True
            for i in range(len(user)):
                if user[i]==ban[i]:
                    continue
                elif ban[i]!='*':
                    star=False
                    break

            print('star',star)
            if star==True:
                possible.append(ban)
                answer+=1
        res.append(possible)
    print(res)
    return answer
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
