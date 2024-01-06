import heapq as hq
import sys

v,e,house = map(int, sys.stdin.readline().split())

graph = []
for _ in range(v+1):
    graph.append([])

for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])

def dijkstra(start,end):
    dis = [1e9]*(v+1)
    heap = []
    hq.heappush(heap, [0,start])
    dis[start] = 0

    while heap:
        dist, point = hq.heappop(heap)

        if dis[point] < dist:
            continue

        for i in graph[point]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                hq.heappush(heap, [dis[i[0]], i[0]])
    
    return dis[end]

res = []
for i in range(1,v+1):
    res.append(dijkstra(i,house)+dijkstra(house,i))
print(max(res[1:]))