def solution(triangle):
    res = []
    for i in range(len(triangle)):
        res.append([0]*len(triangle[i]))
    res[0][0] = triangle[0][0]

    for m,i in enumerate(res):
        if m+1 == len(res):
            break
        for n,j in enumerate(i):
            res[m+1][n] = max(res[m+1][n],triangle[m+1][n]+j)
            res[m+1][n+1] = max(res[m+1][n+1],triangle[m+1][n+1]+j)

    return max(res[-1])