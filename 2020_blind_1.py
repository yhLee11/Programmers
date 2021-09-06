#문자열압축
def solution(s):
    res=[]
    if len(s)==1:return 1
    for i in range(1,len(s)):
        cnt=1
        ss=''
        for j in range(0,len(s),i):
            cur=s[j:j+i]
            if j+2*i<len(s):
                nxt=s[j+i:j+2*i]
            else:
                nxt=s[j+i:len(s)]
                # ss+=s[j+i:len(s)]
            # print(cur,nxt)
            if cur==nxt:
                cnt+=1
            else:
                if cnt==1:
                    ss+=cur
                else:
                    ss+=str(cnt)+cur
                    cnt=1

        res.append(len(ss))

    return min(res)
