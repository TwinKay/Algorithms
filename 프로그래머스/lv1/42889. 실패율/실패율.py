def solution(N, stages):
    total = []
    res = []
    for i in range(N+2):
        total.append([0,i])
        res.append([0,i])
        
    for i in stages:
        total[i][0] += 1
        
    n = len(stages)
    for i in range(N+1):
        if total[i][0] != 0:
            res[i][0] = total[i][0] / n
        n -= total[i][0]

    res = res[1:-1]
    res = sorted(res, key = lambda x : (-x[0],x[1]))
    answer = []
    for i in res:
        answer.append(i[1])

    return answer