'''
아이디어:
DP를 통한 해결
'''
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

if N==1:
    print(arr[0])
elif N==2:
    print(arr[0]+arr[1])
else:
    # dp 테이블 초기화
    dp = [0]*300
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2,N):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i]) # 3연속 피하기 위한 점화식

    print(dp[N-1])