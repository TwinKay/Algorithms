'''
아이디어:
다익스트라를 통한 최단경로 찾기
다른 두 정점 사이에는 여러 개의 간선이 존재할 수도 있음 -> 기존 다익스트라 로직상으로는 문제 없음

'''
import sys
from heapq import heappush, heappop


def dijk(nodes):
    dist = [INF] * (V + 1)
    pq = []
    for node in nodes:
        dist[node] = 0
        heappush(pq, (0, node))  # weight,start_node
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

    return dist


V, E = map(int, sys.stdin.readline().split())

graph = []
for _ in range(V + 1):
    graph.append([])

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

M, x = map(int, sys.stdin.readline().split())
mac_nodes = list(map(int, sys.stdin.readline().split()))
S, y = map(int, sys.stdin.readline().split())
sbuck_nodes = list(map(int, sys.stdin.readline().split()))

INF = float('inf')

mac_arr = dijk(mac_nodes)
sbuck_arr = dijk(sbuck_nodes)

res = INF
for i in range(1, V+1):
    mac_dist = mac_arr[i]
    sbuck_dist = sbuck_arr[i]
    if mac_dist <= x and sbuck_dist <= y and mac_dist != 0 and sbuck_dist != 0:
        res = min(res, mac_dist + sbuck_dist)

if res == INF:
    print(-1)
else:
    print(res)
