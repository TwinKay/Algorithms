'''
아이디어:
DP 사용하기
각 정수마다 가능한 연산끼리 min
'''

import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1) # 초기 dp 테이블 생성

num = 1
dp[num] = 0
for i in range(2,N+1):
    if i % 3 == 0 and i % 2 == 0: # 나누어 떨어지는 경우
        dp[i] = min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i//3]+1,dp[i-1]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
    else:
        dp[i] = dp[i-1]+1

print(dp[N])