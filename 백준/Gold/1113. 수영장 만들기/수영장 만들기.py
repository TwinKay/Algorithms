import sys
import heapq as hq

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = []
for _ in range(N):
    visited.append([False]*M)

pq = []
for i in range(N):
    for j in range(M):
        if i in [0,N-1] or j in [0,M-1]:
            hq.heappush(pq, [graph[i][j],j,i])
            visited[i][j] = True

res = 0
while pq:
    cur = hq.heappop(pq)
    height = cur[0]
    x = cur[1]
    y = cur[2]
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and not visited[dy][dx]:
            if graph[dy][dx] < height:
                res += height-graph[dy][dx]
                hq.heappush(pq, [height,dx,dy])
            else:
                hq.heappush(pq, [graph[dy][dx],dx,dy])
            visited[dy][dx] = True

print(res)