def solution(dartResult='1D2S#10S'):
    answer = 0
    stk=[]
    option=['*','#']
    score=''
    idx=0
    alpha=False
    digit=False

    for i in dartResult:
        # print(i)
        if i in option:
            score+=i
            stk.append(score)
            score=''
            alpha,digit=False,False
        else:
            if i.isalpha():
                alpha=True
                score+=i
                if i==dartResult[-1]:
                    stk.append(score)
            elif i.isdigit():
                # print(i,alpha,digit)
                if alpha:
                    stk.append(score)
                    score=i
                    digit=True
                    alpha=False
                else:
                    score+=i
                    digit=True
                # print(score)
    print(stk)


                    # if len(score)<2:
        #     if i.isdigit() or i.isalpha():
        #         score+=i
        # else:
        #     if i in option:
        #         score+=i
        #     else:
        #         stk.append(score)

    # while idx<len(dartResult):
    #     for i in range(3):
    #         if dartResult[idx+i].isdigit() or dartResult[idx+i].isalpha():
    #             if i==2:#3번째까지
    #                 stk.append(score)
    #                 score=''
    #             else:
    #                 score+=dartResult[idx]
    #         score=''
    #     idx+=3
    # print(stk)

    # while idx<len(dartResult):
    #
    #     if dartResult[idx].isalpha():
    #         if dartResult[idx-1].isalpha():
    #             stk.append(score)
    #             score=''
    #         score+=dartResult[idx]
    #     elif dartResult[idx].isdigit():
    #         score+=dartResult[idx]
    #     else:
    #         if score and dartResult[idx] in option:
    #             score+=dartResult[idx]
    #             stk.append(score)
    #             score=''
    #         else:
    #             stk.append(score)
    #             score=''
    #
    #     idx+=1
    # print(stk)

    # for i,val in enumerate(dartResult):
    #     score=''
    #     while True:
    #         score=
    #     if val.isdigit():
    #         score+=val
    #     elif val.isalpha():
    #         score+=val
    #         if (i+1)!=len(dartResult):
    #             print(i)
    #             if dartResult[i+1] in option:
    #                 score+=val
    #             else:
    #                 stk.append(score)
    #                 score=''
    #
    #
    # print(stk)

    # return print(answer)

solution()
"""
1S 2D* 3T
1D 2S# 10S
보너스SDT

"""
