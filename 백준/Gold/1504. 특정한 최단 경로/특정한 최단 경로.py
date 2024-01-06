import heapq as hq
import sys

v,e = map(int, sys.stdin.readline().split())

graph = []
for _ in range(v+1):
    graph.append([])

for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

m1,m2 = map(int, sys.stdin.readline().split())

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

dis_1_m1 = dijkstra(1,m1)
dis_1_m2 = dijkstra(1,m2)
dis_m1_m2 = dijkstra(m1,m2)
dis_m2_m1 = dijkstra(m2,m1)
dis_m1_v = dijkstra(m1,v)
dis_m2_v = dijkstra(m2,v)

route1 = dis_1_m1+dis_m1_m2+dis_m2_v
route2 = dis_1_m2+dis_m2_m1+dis_m1_v
res = min(route1,route2)
if res < 1e9:
    print(res)
else:
    print(-1)