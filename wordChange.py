def solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log", "cog"]):
    if target not in words:
        return 0
    ans=0
    word_lst=[begin]
    word_len=len(begin)
    while True:
        for wl in word_lst:
            diff_lst=[]
            for w in words:
                diff=0
                for i in range(word_len):
                    if w[i]!=wl[i]:
                        diff+=1
                    if diff>1:break
                if diff==1:
                    diff_lst.append(w)
                    words.remove(w)
        ans+=1
        if target in diff_lst:
            return ans
        else:
            word_lst=diff_lst

print(solution())
