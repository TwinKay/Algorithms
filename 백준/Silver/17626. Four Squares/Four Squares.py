import sys, math

n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[1] = 1

for i in range(2, n+1):
    if i**(1/2) % 1 == 0:
        dp[i] = 1

    else:
        temp = []
        for j in range(1, math.floor(i**(1/2))+1):
            temp.append(dp[i-(j**2)]+1)
        dp[i] = min(temp)

print(dp[n])