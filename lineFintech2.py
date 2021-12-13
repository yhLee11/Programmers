import numpy as np
def solution(pixels):
    lst=[]
    for i in pixels:
        lst.append(list(map(int,list(i))))
    lst=np.array(lst)
    lst=lst.T
    # print(lst)
    hap=[]
    ans=''
    for j in range(0,len(lst),3):
        one=lst[j:j+3]
        # print(one)
        # print(sum(sum(one)))
        hap=sum(sum(one))
        if hap==9:
            ans+='4'
        elif hap==13:
            ans+='8'
        elif hap==12:#0,6,9
            # print('0,6,9')
            # print(one)
            # print(one[0][1],one[2][3])
            if one[2][1]==1 and one[2][3]==1 and one[0][3]==1:
                ans+='0'
            elif one[2][1]==0 and one[2][3]==1:
                ans+='6'
            else:
                ans+='9'
        elif hap==11:#2,3,5
            # print(one,'2,3,5')
            if one[0][1]==0 and one[2][3]==0:
                ans+='2'
            elif one[0][1]==0 and one[2][3]==1:
                ans+='3'
            else:
                ans+='5'
        elif hap==8:#1,7
            # print(one,'1,7')
            if one[2][0]==0:
                ans+='1'
            else:
                ans+='7'
    return ans