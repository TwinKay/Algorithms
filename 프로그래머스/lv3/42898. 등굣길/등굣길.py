def solution(m, n, puddles):
    dp = []
    for _ in range(n):
        dp.append([0]*m)
    dp[0][0] = 1

    for y in range(n):
        for x in range(m):
            if x==0 and y==0:
                pass
            elif [x+1,y+1] in puddles:
                dp[y][x] = 0
            else:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

    return dp[-1][-1]%1000000007