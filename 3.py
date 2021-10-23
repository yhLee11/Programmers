from itertools import permutations
def solution(n):
    if n==0:return 0
    num={2:[1],4:[4,7],5:[2,3,5],6:[0,6,9],7:[8]}
    op={1:['-','/'],2:['+','*']}
    lst=[]
    numK=list(num.keys())*3#3개
    opK=list(op.keys())#1개
    pm=list(permutations(numK,3))
    for o in op:
        for i in pm:
            # print(sum(i),i)
            if sum(i)==n-o:
                lst.append((o,i))
    lst=list(set(lst))
    # print(lst)
    ans=0
    for i in lst:
        #i=(1,(7,6,7))
        opV=op[i[0]]
        one=num[i[1][0]]
        two=num[i[1][1]]
        three=num[i[1][2]]
        for o in opV:
            for a in one:
                for b in two:
                    res=-1
                    for c in three:
                        if o=='-':
                            res=a-b
                            if res==c:ans+=1
                        elif o=='/':
                            if b!=0:
                                res=a/b
                                if res==c:ans+=1
                        elif o=='+':
                            res=a+b
                            if res==c:ans+=1
                        elif o=='*':
                            res=a*b
                            if res==c:ans+=1
    return ans
