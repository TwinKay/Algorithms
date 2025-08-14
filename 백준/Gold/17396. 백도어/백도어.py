import sys
from heapq import heappush,heappop

N,M = map(int ,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr[N-1] = 0
graph = []
for _ in range(N):
    graph.append([])
for _ in range(M):
    a,b,t = map(int ,sys.stdin.readline().split())
    if arr[a] != 1 and arr[b] != 1:
        graph[a].append((t,b))
        graph[b].append((t,a))

INF = float('inf')
dist = [INF]*N
pq = []
heappush(pq,(0,0))# weight, node
dist[0] = 0
while pq:
    w,v = heappop(pq)
    if w > dist[v]:
        continue
    for next_node in graph[v]:
        nw,nv = next_node
        total_w = nw + w
        if total_w < dist[nv]:
            dist[nv] = total_w
            heappush(pq, (total_w,nv))

if dist[N-1] == INF:
    print(-1)
else:
    print(dist[N-1])