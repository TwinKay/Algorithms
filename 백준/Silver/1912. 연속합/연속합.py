'''
아이디어:
매 구간 더해온 값과 현재의 값 중 MAX로 dp적용
'''

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
dp[0] = arr[0]
for i in range(1,N):
    dp[i] = max(dp[i-1]+arr[i], arr[i]) # 이전까지의 합+현재 값, 현재 값

print(max(dp))