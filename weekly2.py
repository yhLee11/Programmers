import numpy as np
def solution(scores=[[50,90],[50,87]]):
    answer = ''
    arr=np.array(scores)
    dic={50:'F',70:'D',80:'C',90:'B',101:'A'}

    for i in range(len(scores)):
        mid=0
        line=arr[:,i]
        sorted_lst=sorted(line)
        # print('line',line,'sorted_lst',sorted_lst)
        print('###line[i]',line[i])
        if line[i]==max(line):
            print(i,sorted_lst,line[i],max(scores[i]))
            print('sorted_lst[1],line',sorted_lst[1],line[i])
            if sorted_lst[-2]==line[i]:
                print('max break')
                pass
            else:
                print('max cut',sorted_lst[-1])
                sorted_lst.pop()
        elif line[i]==min(line):#최고 혹은 최저점이 자신
            print(i,sorted_lst,line[i],min(scores[i]))
            print('sorted_lst[1],line',sorted_lst[1],line[i])
            if sorted_lst[1]==line[i]:
                print('line[i]',line[i],i,sorted_lst[1])
                # print('min break')
                pass
            else:
                print('min cut',sorted_lst[0])
                sorted_lst.pop(0)
        mid=sum(sorted_lst)/len(sorted_lst)
        # print('mid',mid)

        for key,val in dic.items():
            if mid<key:
                print('mid,key',mid,key)
                answer+=val
                break
    # print(answer)
    return answer
print(solution())
