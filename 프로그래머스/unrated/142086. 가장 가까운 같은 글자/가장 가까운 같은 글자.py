def solution(s):
    res = []
    dic = {}
    for i in s:
        if i not in dic.keys():
            dic[i] = 0
            res.append(-1)
        else:
            res.append(dic[i])
            dic[i] = 0
        
        for j in dic.keys():
            dic[j] += 1

    return res