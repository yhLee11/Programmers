def solution(N, number):
    #https://velog.io/@j_user0719/N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-PYTHON
    #DP
    #N이 i개 만큼 set을 만듬
    #dp[1]={5},dp[2]={5+5,5-5,5//5,5*5}
    #dp[3]={555,(dp[1],dp[2]),(dp[2],dp[1])}
    #dp[i] set에서 number가 존재하면 i를 반환
    #발견 못하면 return -1
    ans=-1
    dp=[]
    for i in range(1,9):
        all_case=set()
        chk_num=int(str(N)*i)
        #{N},{NN},{NNN}...
        all_case.add(chk_num)
        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    all_case.add(op1-op2)
                    all_case.add(op1+op2)
                    all_case.add(op1*op2)
                    if op2 !=0:
                        all_case.add(op1//op2)
        if number in all_case:
            ans=i
            break
        dp.append(all_case)
    return ans
