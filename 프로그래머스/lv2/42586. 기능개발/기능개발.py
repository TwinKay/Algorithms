def solution(progresses, speeds):
    import math
    res = []
    for i in range(len(progresses)):
        res.append(math.ceil((100-progresses[i])/speeds[i]))
    print(res)
    
    cnt = 0
    first = res[0]
    for i in range(1,len(res)):
        if res[i] < res[i-1]:
            res[i] = res[i-1]
    total = list(set(res))
    total.sort()
    ans = []
    for i in total:
        ans.append(res.count(i))
        print(i)
        print(total)
    print(ans)
    return ans