from collections import defaultdict
gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
dic=defaultdict(int)
jew=len(set(gems))
ans=[]
start,end=0,0
while True:
    print(start,end,dic)
    if start==len(gems):
        break
    # if end==len(gems):
        
    if len(dic)==jew:
        ans.append((end-start,[start,end]))
        print('append ans',ans)
        dic=defaultdict(int)
        start+=1
        end=start
    for i in range(start,end):
        dic[gems[i]]+=1

    end+=1

print(ans)