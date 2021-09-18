from itertools import permutations
operation=('*','+','-')
prioritys=list(permutations(operation,3))
def calc(priority,n,expression):
    #priority:우선순위모음, n:우선순위(낮은것부터0,1,2), expression:더 낮은 우선순위에서 쪼개진 식 문자열
    if n==2:
        return str(eval(expression))
    if priority[n]=='*':
        res=eval('*'.join([calc(priority,n+1,e) for e in expression.split('*')]))
        print('*',res)
    if priority[n]=='+':
        res=eval('+'.join([calc(priority,n+1,e) for e in expression.split('+')]))
        print('+',res)
    if priority[n]=='-':
        res=eval('-'.join([calc(priority,n+1,e) for e in expression.split('-')]))
        print('-',res)

    return str(res)
def solution(expression):
    answer=0
    for prio in prioritys:
        res=int(calc(prio,0,expression))
        answer=max(answer,abs(res))
    return answer
print(solution("100-200*300-500+20"	))
# stk=[]
# token=[]
# operation=('*','+','-')
# prec=list(permutations(operation,3))
# max_num=-1
# def postfix(token):
#     post=[]
#     global stk
#     global max_num
#     for prio in prec:#조합순서6개 만큼
#         prio=list(prio)
#
#         for e in token:#숫자,문자 토큰
#             if type(e)==int:
#                 post.append(e)
#             elif e in prio:
#                 if stk:
#                     if prio.index(e)<=prio.index(stk[-1]):#현재더높음
#                         print(prio,prio.index(e),prio.index(stk[-1]))
#                         post.append(stk.pop())
#                         stk.append(e)
#                     else:
#                         post.append(e)
#                 elif not stk:
#                     stk.append(e)
#                     print('stk',stk)
#         while not stk:
#             post.append(stk.pop())
#         print('post',post)
#
#         #eval
#         opstk=[]
#         for p in post:
#             if type(p)==int:
#                 opstk.append(p)
#             elif p=='*':
#                 n1=opstk.pop()
#                 n2=opstk.pop()
#                 opstk.append(n1*n2)
#             elif p=='+':
#                 n1=opstk.pop()
#                 n2=opstk.pop()
#                 opstk.append(n1+n2)
#             elif p=='-':
#                 n1=opstk.pop()
#                 n2=opstk.pop()
#                 opstk.append(n2-n1)
#         if max_num<abs(opstk[-1]):
#             max_num=abs(opstk[-1])
#             print(max_num)
#         post=[]
#         stk=[]
#
# def tokenizer(exp):
#     oper=''
#     num=''
#     for i in exp:
#
#         if i.isdigit():
#             num+=i
#         else:
#             oper=i
#             token.append(int(num))
#             token.append(oper)
#             num=''
#             oper=''
#     token.append(int(num))
#
#
# def solution(expression):
#     answer = 0
#     tokenizer(expression)
#     postfix(token)
#     print(max_num)
# print(solution("100-200*300-500+20"))
