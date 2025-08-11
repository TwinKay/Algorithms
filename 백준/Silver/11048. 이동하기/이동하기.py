'''
아이디어:
x,y좌표 모두 한 길밖에 없기에 누적합으로 dp 테이블 초기화 해두고,
나머지는 3방향에 대해서 max 갱신해주기
'''

import sys

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp = []
for _ in range(N):
    dp.append([0]*M)

# 0열 초기화
sm = 0
for i in range(N):
    sm += graph[i][0]
    dp[i][0] = sm

# 0행 초기화
sm = 0
for j in range(M):
    sm += graph[0][j]
    dp[0][j] = sm

# 0행, 0열 제외하고 3방향 dp
for i in range(1,N):
    for j in range(1,M):
        dp[i][j] = max(dp[i-1][j]+graph[i][j], dp[i][j-1]+graph[i][j], dp[i-1][j-1]+graph[i][j])

print(dp[-1][-1])
