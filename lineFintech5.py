import re
def solution(strs):
    #(AAB~|BAB~A)~
    # p=re.compile('((AAB)+|((BAB)+A$))+')
    p=re.compile('((AAB)+|(BAB)+A$)+')
    cnt=0
    for s in strs:
        # print(s)
        res=p.match(s)
        if res!=None:
            cnt+=1
        print(res)
    return cnt