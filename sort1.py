#k번째수
def solution(array, commands):
    res=[]
    for comm in commands:
        arr=array[comm[0]-1:comm[1]]
        arr.sort()
        res.append(arr[comm[2]-1])
    return res
