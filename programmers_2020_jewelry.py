from collections import defaultdict
def solution(gems):
    dic=defaultdict(int)
    jew=len(set(gems))
    gems_len=len(gems)
    ans=[]
    start,end=0,0

    while True:
        if end==gems_len:
            if start==gems_len:break
            if len(dic)==jew:
                ans.append([end-start,start,end])
                dic[gems[start]]-=1
                if dic[gems[start]]==0:
                    del(dic[gems[start]])
            start+=1

        else:
            if len(dic)==jew:
                ans.append([end-start,start,end])
                dic[gems[start]]-=1
                if dic[gems[start]]==0:
                    del(dic[gems[start]])
                start+=1
            else:
                dic[gems[end]]+=1
                end+=1
    ans.sort(key=lambda x:(x[0],x[1]))
    return [ans[0][1]+1,ans[0][2]]
