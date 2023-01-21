def solution(k, m, score):
    res = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        temp = score[i:i+m]
        if len(temp) == m:
            res += min(temp)*m

    return res