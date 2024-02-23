import heapq as hq

def solution(N, road, K):
    INF = 1e9

    graph = []
    for _ in range(N+1):
        graph.append([])

    new_road = []
    for i in road:
        a,b,c = i
        new_road.append([a,b,c])
        new_road.append([b,a,c])
    new_road.sort()

    road = []
    for j,i in enumerate(new_road):
        a,b,c = i
        if j==0:
            road.append([a,b,c])
        else:
            if not (road[-1][0] == a and road[-1][1] == b):
                road.append([a,b,c])

    for i in road:
        graph[i[0]].append([i[1],i[2]])

    dist = [1e9]*(N+1)
    heap = []
    hq.heappush(heap,[0,1]) # cost,node
    dist[1] = 0
    while heap:
        cost, node = hq.heappop(heap)

        if dist[node] < cost:
            continue

        for i in graph[node]:
            if cost+i[1] < dist[i[0]]:
                dist[i[0]] = cost+i[1]
                hq.heappush(heap, [cost+i[1],i[0]])

    res = 0
    for i in dist:
        if i <= K:
            res += 1

    return res