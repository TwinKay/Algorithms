import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[j]+1, dp[i])
            
print(max(dp))