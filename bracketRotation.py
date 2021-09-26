from collections import deque
def solution(s):
    s=list(s)
    q=deque()
    for i in s:
        q.append(i)
    cnt=0
    for i in range(len(q)):
        q.rotate(1)
        tmp=q
        stk=deque()
        for elem in tmp:
            if not stk:
                stk.append(elem)
            elif stk[-1]=='{':
                if elem=='}':
                    stk.pop()
                else:
                    stk.append(elem)
            elif stk[-1]=='(':
                if elem==')':
                    stk.pop()
                else:
                    stk.append(elem)
            elif stk[-1]=='[':
                if elem==']':
                    stk.pop()
                else:stk.append(elem)
            else:
                break
        if not stk:
            cnt+=1
    return cnt
