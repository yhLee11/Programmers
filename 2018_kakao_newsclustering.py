from collections import Counter
import re
def solution(str1="FRANCE", str2="french"):

    rule=re.compile("[^a-zA-Z]+")#알파벳이 아닌것의 패턴이 하나 이상
    str1=[str1[i:i+2].lower() for i in range(0,len(str1)-1) if not rule.findall(str1[i:i+2])]
    str2=[str2[i:i+2].lower() for i in range(0,len(str2)-1) if not rule.findall(str2[i:i+2])]
    # print(str1,str2)

    inter=set(str1)&set(str2)
    union=set(str1)|set(str2)
    # print(inter,union)
    if len(union)==0:
        return 65536
    inter_sum=sum([min(str1.count(i),str2.count(i)) for i in inter])
    # print(inter_sum)
    union_sum=sum([max(str1.count(i),str2.count(i)) for i in union])
    # print(union_sum)
    # print(inter_sum,union_sum)
    return int((inter_sum/union_sum)*65536)

print(solution())
"""
a=111
b=11111
교집합
min(3,5)=3
합집합
max(3,5)=5

"""
