def solution(numbers, hand):
    answer = ''
    l=[1,4,7]
    r=[3,6,9]
    m=[2,5,8,0]
    pad=[[1,[1,2,3]],[2,[4,5,6]],[3,[7,8,9]],[4,[0]]]
    ptrL=-1
    ptrR=-1
    current,cur_r,cur_l=-1,-1,-1
    for i in range(len(numbers)):
        if numbers[i] in l:
            ptrL=numbers[i]
            answer+='L'
        elif numbers[i] in r:
            ptrR=numbers[i]
            answer+='R'
        else:
            for j in range(4):
                if numbers[j] in pad[j][1]:
                    current=pad[j][0]
                if ptrR in pad[j][1]:
                    cur_r=pad[j][0]
                if ptrR in pad[j][1]:
                    cur_l=pad[j][0]
            if abs(cur_r-current)>abs(cur_l-current):
                answer+='L'
            elif abs(cur_r-current)<abs(cur_l-current):
                answer+='R'
            else:
                if hand=="right":
                    answer+='R'
                else:
                    answer+='L'
    
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
