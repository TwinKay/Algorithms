'''
아이디어:
다익스트라인걸 몰랐다면 시뮬로 풀다 시간초과 났을지도..
'''
import sys
from heapq import heappush,heappop

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
y1,x1,y2,x2 = map(int, sys.stdin.readline().split())
x1-=1;y1-=1;x2-=1;y2-=1 # 0-based-idx로 변경
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
    
graph[y1][x1] = '0' # 다익스트라 weight 적용해서 풀도록 변경
graph[y2][x2] = '1'
for i in range(N):
    graph[i] = list(map(int, graph[i]))

INF = float('inf')
dist = []
for _ in range(N):
    dist.append([INF]*M)

pq = []
heappush(pq,(0,(x1,y1)))
dist[y1][x1] = 0

while pq:
    w,idx = heappop(pq)
    cx,cy = idx
    if w > dist[cy][cx]:
        continue
    for k in range(4):
        dx = cx + delta_x[k]
        dy = cy + delta_y[k]
        if is_valid(dx,dy):
            total_w = w + graph[dy][dx]
            if dist[dy][dx] > total_w:
                dist[dy][dx] = total_w
                heappush(pq,(total_w,(dx,dy)))

print(dist[y2][x2])