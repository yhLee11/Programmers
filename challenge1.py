# from funtools import reduce
def solution(price, money, count):
    answer = -1
    for i in range(1,count+1):
        money-=price*i
        if money<0:
            answer=abs(money)
        else:
            answer=0
    return answer

print(solution(4,3,3))



def solution1(price, money, count):
    return(max(0,price*(count+1)*count//2-money))#산술평균 이용 풀이
    # print(price,count+1,count)
def solution2(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
