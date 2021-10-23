from itertools import permutations
def solution(s1, s2):
    str1,str2=str(s1),str(s2)
    res1,res2=[],[]
    def sol(st):
        res=[]
        for i in range(0,len(st),2):
            n1,n2=int(st[i]),int(st[i+1])
            for k in range(n2):
                res.append(n1)
        return res
    def makeStr(lst):
        num=1000000000
        numlst=[]
        leng=len(lst[0])
        for i in lst:
            intNum=int(''.join(list(map(str,i))))
            if len(str(intNum))==leng:
                num=min(intNum,num)
                numlst.append(intNum)
        return sorted(numlst)
    res1=sol(str1)
    res2=sol(str2)
    lst1=list(set(permutations(res1)))
    lst2=list(set(permutations(res2)))
    ans1,ans2=makeStr(lst1),makeStr(lst2)
    for i in ans1:
        if i+1 in ans2:
            return [i,i+1]
            break
