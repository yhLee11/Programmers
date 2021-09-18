def solution(gems):
    answer = []
    kinds=list(set(gems))
    print(kinds)
    lst=[]
    for g in gems:

        if g in kinds:
            lst.append(g)

    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
