'''
아이디어:
다익스트라를 통한 최단경로 찾기
완탐으로 해도 아슬아슬하게 가능할 듯 -> 시간 초과
검문이 없을 때 사용되는 edge들만 검사
'''
import sys
from heapq import heappush, heappop

def dijk_path(node):
    path = []
    dist = [INF] * (V + 1)
    pq = []
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
                path.append((nw,nv))

    return [dist[V],path]

def dijk(node,ban_node):
    dist = [INF] * (V + 1)
    pq = []
    dist[node] = 0
    heappush(pq, (0, node))  # weight,start_node
    while pq:
        cur_node = heappop(pq)
        w, v = cur_node
        if dist[v] < w:  # 이미 최단거리가 더 작으면
            continue
        for next_node in graph[v]:  # 경유해서 가는 경우들
            if next_node == ban_node: # 간선 하나 밴
                continue
            nw, nv = next_node
            total_w = w + nw  # 가중치 누적
            if total_w < dist[nv]:  # 갱신할 수 있으면
                dist[nv] = total_w
                heappush(pq, (total_w, nv))

    return dist[V]


V, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

INF = float('inf')

graph = []
for _ in range(V + 1):
    graph.append([])

for edge in edges:
    s, e, w = edge
    graph[s].append((w, e))
    graph[e].append((w, s))

normal_time,path_nodes = dijk_path(1)

max_delay = -INF
for path_node in path_nodes:
    time = dijk(1,path_node)
    max_delay = max(max_delay, time - normal_time)

if max_delay in [-INF, INF]:
    print(-1)
else:
    print(max_delay)