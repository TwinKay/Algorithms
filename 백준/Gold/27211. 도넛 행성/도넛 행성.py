import sys
from collections import deque

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
visited = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([False]*M)

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            cnt += 1
            deq = deque()
            deq.append([j,i])
            visited[i][j] = True
            while deq:
                cur = deq.popleft()
                for k in range(4):
                    dx = cur[0] + delta_x[k]
                    dy = cur[1] + delta_y[k]
                    dx = (dx+M)%M
                    dy = (dy+N)%N
                    if graph[dy][dx] == 0 and not visited[dy][dx]:
                        deq.append([dx,dy])
                        visited[dy][dx] = True

print(cnt)