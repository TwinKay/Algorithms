'''
아이디어:
DP 사용하기
'''

import sys

N = int(sys.stdin.readline())

dp = [0,1] # 초기 dp 테이블 생성
for i in range(2,N+1):
    dp.append(dp[-2]+dp[-1]) # 마지막 두 요소 더하기
    
print(dp[N])