'''
아이디어:
점화식 발견을 통한 DP 사용하기
'''

import sys

N = int(sys.stdin.readline())
dp = [0]*(1001) # dp table 초기화
dp[1] = 1
dp[2] = 3
for i in range(3,N+1):
    dp[i] = (dp[i-2]*2 + dp[i-1])%10_007 # 점화식

print(dp[N])