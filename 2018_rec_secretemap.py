def solution(n=5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28]):
    answer = []
    map1=[]
    map2=[]
    for i in arr1:
        b_str=str(bin(i)).lstrip('0b')
        if len(b_str)!=5:
            num=5-len(b_str)
            zero='0'
            for _ in range(num):
                b_str=zero+b_str
        map1.append(b_str)
    print(map1)
    for i in arr2:
        b_str=str(bin(i)).lstrip('0b')
        if len(b_str)!=n:
            num=n-len(b_str)
            zero='0'
            for _ in range(num):
                b_str=zero+b_str
        map2.append(b_str)
    print(map2)
    answer=[]
    for i in range(n):
        res=""
        for j in range(n):
            if map1[i][j]=='1' or map2[i][j]=='1':
                res+="#"
            else:
                res+=" "
        answer.append(res)

    return answer
print(solution())


# print(str(bin(9)).lstrip('0b'))
