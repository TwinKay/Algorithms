'''
땅 높이는 0<=높이<=256
답이 여러 개면 땅의 높이가 가장 높은 것!
불가능한 경우 언급 X
아이디어:
가지고 있는 땅: 실제 땅 + 인벤토리 땅
가능한 높이 전부 다
단순 계산으로 가중치
'''

import sys

N,M,B = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

total_b = B
for i in range(N):
    for j in range(M):
        total_b += graph[i][j]

max_height = int(total_b/(N*M))

min_time,res_height = 500*500*256*10, -1

for h in range(max_height,-1,-1):
    time = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= h:
                time += (graph[i][j]-h)*2 # 없애는 건 두 배
            else:
                time += h-graph[i][j]

    if time < min_time:
        min_time = time
        res_height = h

print(min_time,res_height)