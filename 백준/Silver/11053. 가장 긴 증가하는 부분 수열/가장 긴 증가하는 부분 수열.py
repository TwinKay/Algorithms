'''
아이디어:
DP를 통한 해결 -> n^2이지만 가능
'''
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1]*N # dp 테이블 초기화

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1) # 갱신

print(max(dp))
