import heapq as hq
import sys
import copy

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

graph = []
for _ in range(v+1):
    graph.append([])

for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])

start,end = map(int, sys.stdin.readline().split())

dis = [1e9]*(v+1)
route = []
for _ in range(v+1):
    route.append([])

heap = []
hq.heappush(heap, [0,start])
dis[start] = 0
route[start].append(start)

while heap:
    dist, point = hq.heappop(heap)

    if dis[point] < dist:
        continue

    for i in graph[point]:
        cost = dist + i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            
            route[i[0]] = copy.deepcopy(route[point])
            route[i[0]].append(i[0])
            hq.heappush(heap, [dis[i[0]], i[0]])

print(dis[end])
print(len(route[end]))
print(' '.join(list(map(str, route[end]))))