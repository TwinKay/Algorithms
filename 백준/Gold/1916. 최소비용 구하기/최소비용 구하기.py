'''
아이디어:
다익스트라를 통한 최단경로 찾기 (pq 사용)
'''
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = []
for _ in range(N + 1):
    graph.append([])

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

INF = float('inf')
dist = [INF] * (N + 1)
pq = []

start_node, end_node = map(int, sys.stdin.readline().split())

dist[start_node] = 0  # start_node 시작
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

print(dist[end_node])
