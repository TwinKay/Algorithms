'''
아이디어:
역으로 다익스트라 이용하기
'''
import sys
from heapq import heappush, heappop

N, M, K = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N + 1):
    graph.append([])

for _ in range(M):
    e, s, w = map(int, input().split())
    graph[s].append((w, e))

INF = float('inf')
dist = [INF] * (N + 1)
pq = []

start_nodes = list(map(int, sys.stdin.readline().split()))
for start_node in start_nodes:
    dist[start_node] = 0
    heappush(pq, (0, start_node))  # weight,start_node

while pq:
    w, v = heappop(pq)

    if dist[v] < w:  # 이미 최단거리가 더 작으면
        continue
    for next_node in graph[v]:  # 경유해서 가는 경우들
        nw, nv = next_node
        total_w = w + nw  # 가중치 누적
        if total_w < dist[nv]:  # 갱신할 수 있으면
            dist[nv] = total_w
            heappush(pq, (total_w, nv))

dist[0] = -1  # dummy
res_max = max(dist)
res_idx = dist.index(res_max)
print(res_idx)
print(res_max)
