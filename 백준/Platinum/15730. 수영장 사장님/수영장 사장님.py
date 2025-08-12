import sys
from heapq import heappop,heappush


def is_valid(x,y):
    return 0<=x<M and 0<=y<N


delta_x = [0,0,1,-1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


visited = []
for _ in range(N):
    visited.append([False]*M)

pq = []
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            heappush(pq, (graph[i][j],j,i))
            visited[i][j] = True

res = 0
while pq:
    h,x,y = heappop(pq)
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and not visited[dy][dx]:
            if graph[dy][dx] < h:
                res += h-graph[dy][dx]
                heappush(pq, (h,dx,dy))
            else:
                heappush(pq, (graph[dy][dx],dx,dy))
            visited[dy][dx] = True

print(res)