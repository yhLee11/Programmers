import re
def solution(new_id):

    #step1
    low=''
    for i in range(len(new_id)):
        if new_id[i].isalpha():
            low+=new_id[i].lower()
        else:
            low+=new_id[i]
    new_id=low
    #step2
    rule1=re.compile('\w*[-_.]*')
    lst=rule1.findall(new_id)
    new_id=''.join(lst)

    #step3
    dot=0
    rm=''
    for i in range(len(new_id)):
        if new_id[i]=='.':
            dot+=1
            if dot>1:
                continue
            else:
                rm+=new_id[i]
        else:
            dot=0
            rm+=new_id[i]
    new_id=rm

    #step4
    new_id=new_id.rstrip('.').lstrip('.')

    #step5
    if new_id=='':new_id='a'
    #step6
    if len(new_id)>=16:
        new_id=new_id[:15]
        new_id=new_id.rstrip('.')

    #step7
    if len(new_id)<=2:
        for i in range(3-len(new_id)):
            new_id+=new_id[-1]

    return print(new_id)

solution("...!@BaT#*..y.abcdefghijklm")
