from collections import defaultdict
def solution(gems):
    dic=defaultdict(int)
    jew=len(set(gems))
    if jew==len(gems):
        return list(1,len(gems))
    ans=[]
    start,end=0,0
    while True:
        if start==len(gems):
            break
        if end==len(gems):
            dic[gems[end-1]]+=1
            if len(dic)==jew:
                ans.append((end-start,start,end))
            dic=defaultdict(int)
            start+=1
            end=start
        for i in range(start,end):
            dic[gems[i]]+=1
        if len(dic)==jew:
            ans.append((end-start,start,end))
            dic=defaultdict(int)
            start+=1
            end=start
        end+=1
    ans.sort(key=lambda x:(x[0],x[1]))
    return [ans[0][1]+1,ans[0][2]]
